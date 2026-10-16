import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

# 1. BASE DE DADOS DE TREINO (Apenas as frases, sem os rótulos de intenção)
frases_treino = [
    # Doações
    "Quero doar 10 kg de arroz",
    "Posso contribuir com 15 litros de leite",
    "Tenho 30 kg de banana para doar",
    "Tenho 20 caixas de tomate para doar hoje",
    "Gostaria de oferecer refeições prontas para abrigo",
    "Tenho sobra de alimentos do meu restaurante",
    "Posso entregar 5 kg de feijão perto da validade",
    "Queremos cadastrar uma doação de legumes",
    
    # Solicitações
    "Nossa ONG precisa de doações de alimentos",
    "Estamos buscando marmitas e cestas básicas urgentemente",
    "Quais doações estão disponíveis para retirada na região?",
    "Preciso de suprimentos para o abrigo comunitário",
    "Como faço para solicitar comida para nossa cozinha social?",
    
    # Status
    "Onde está o meu pedido de doação?",
    "Gostaria de ver o histórico de matches das ONGs",
    "Qual o status do voluntário que vai retirar os alimentos?",
    "Como consultar se a doação já foi entregue?",
    
    # Fora de escopo
    "Qual é a previsão do tempo para hoje?",
    "Gosto de assistir filmes de ficção científica",
    "Quem venceu o jogo de futebol ontem?",
    "Como faço para trocar a senha da minha conta bancária?"
]

class MotorNLU:
    # Definimos n_clusters=4 pois temos 4 assuntos principais nas frases acima
    def __init__(self, n_clusters=4, limiar_threshold=0.60):
        self.limiar_threshold = limiar_threshold
        self.n_clusters = n_clusters
        
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=42, n_init=10)
        self.classifier = RandomForestClassifier(n_estimators=80, random_state=42)
        
        self._treinar_modelo()

    def _treinar_modelo(self):
        """Vetoriza os textos, descobre os grupos e treina o classificador."""
        # 1. Transforma os textos em números (vetorização)
        X_vec = self.vectorizer.fit_transform(frases_treino)
        
        # 2. K-Means descobre os grupos automaticamente (0, 1, 2, 3...)
        grupos_descobertos = self.kmeans.fit_predict(X_vec)
        
        # 3. Random Forest aprende a reproduzir esses grupos descobertos
        self.classifier.fit(X_vec, grupos_descobertos)
        
        print(f" [NLU] Modelo K-Means ({self.n_clusters} clusters) e Random Forest treinados com sucesso!")

    def processar_mensagem(self, texto_usuario):
        """
        Processa uma mensagem, prevê o grupo (cluster) com o Random Forest
        e aplica o Fallback caso a confiança seja baixa.
        """
        # 1. Vetorização da entrada
        vetor_texto = self.vectorizer.transform([texto_usuario])
        
        # 2. Predição de probabilidade via Random Forest
        probabilidades = self.classifier.predict_proba(vetor_texto)[0]
        max_confianca = float(np.max(probabilidades))
        grupo_predito = int(self.classifier.predict(vetor_texto)[0])
        
        # 3. Trava de Segurança por Threshold
        if max_confianca < self.limiar_threshold:
            return {
                "intencao": "fallback",
                "confianca": max_confianca,
                "resposta": (
                    "Desculpe, não consegui entender com clareza o seu pedido. \n"
                    "Você pode refazer a mensagem detalhando melhor o que precisa?"
                )
            }
        
        return {
            "intencao": f"Grupo_{grupo_predito}",
            "confianca": max_confianca,
            "resposta": f"Mensagem classificada no Grupo {grupo_predito} com {max_confianca*100:.1f}% de confiança."
        }

# --- TESTE DO MÓDULO EM TEMPO DE EXECUÇÃO ---
if __name__ == "__main__":
    nlu = MotorNLU(n_clusters=4, limiar_threshold=0.60)
    
    # Bateria de testes automatizados
    frases_teste = [
        "Tenho 30 kg de banana para doar",
        "Nossa instituição precisa de mantimentos",
        "Qual é a receita de bolo de cenoura?", 
        "coisa comida doar la" 
    ]
    
    print("\n--- BATERIA DE TESTES DE ESTRESSE NLU (K-MEANS + RANDOM FOREST) ---")
    for frase in frases_teste:
        resultado = nlu.processar_mensagem(frase)
        print(f"\nEntrada: '{frase}'")
        print(f"Intenção: {resultado['intencao']} | Confiança: {resultado['confianca']:.2f}")
        print(f"Retorno: {resultado['resposta']}")