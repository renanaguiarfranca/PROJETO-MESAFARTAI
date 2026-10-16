1.	Informe quantos número de árvores foram utilizados no motor NLU.
2.	Informa qual o valor de threshold foi utilizado no processo de limiar de confiança
3.	Coloque o resultado da primeira execução
4.	Descreva como você poderia fazer para os resultados de testes serem melhores, aumento o grau de confiança dos resultados
5.	Descreva por que o Random Forest foi o melhor método de Machine Learning para essa fase.

1 - 4
2 - 0.60
3 -   [NLU] Modelo K-Means (4 clusters) e Random Forest treinados com sucesso!

--- BATERIA DE TESTES DE ESTRESSE NLU (K-MEANS + RANDOM FOREST) ---

Entrada: 'Tenho 30 kg de banana para doar'
Intenção: Grupo_1 | Confiança: 0.84
Retorno: Mensagem classificada no Grupo 1 com 83.8% de confiança.

Entrada: 'Nossa instituição precisa de mantimentos'
Intenção: Grupo_3 | Confiança: 0.74
Retorno: Mensagem classificada no Grupo 3 com 73.8% de confiança.

Entrada: 'Qual é a receita de bolo de cenoura?'
Intenção: Grupo_3 | Confiança: 0.82
Retorno: Mensagem classificada no Grupo 3 com 82.5% de confiança.

Entrada: 'coisa comida doar la'
Intenção: fallback | Confiança: 0.59
Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
Você pode refazer a mensagem detalhando melhor o que precisa?

4 - aumentando os clusters, melhorando o contexto, adicionando mais dados de entrada para treino.

5 - pela precisão na confiança(resposta), é mais focado nas palavras chave, tem logica mais robusta, entende melhor o contexto tendo mais precisão na resposta

CHECKLIST DE FINALIZAÇÃO DA ETAPA DE HOJE
Para garantir a nota da etapa (0,25 ponto na AC-3), verifique:
•	[X] Arquivo src/nlu.py salvo e executado sem erros no terminal.
•	[X] Trava de Threshold (< 0.60) funcionando nos testes para mensagens incertas/fora de escopo.
•	[X] Arquivo requirements.txt atualizado na raiz do repositório.
•	[X] Comandos git add, git commit e git push executados com sucesso (verificar na página do repositório no GitHub se o último commit aparece atualizado).
•	[X] Inserção de dados no regras.txt e relatório de execução construído.
