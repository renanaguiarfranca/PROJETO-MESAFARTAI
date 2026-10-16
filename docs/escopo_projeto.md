Problema de Negócio Abordado
O projeto "Mesa Farta AI" resolve o descompasso entre o alto índice de desperdício de alimentos e a insegurança alimentar. Existe uma forte fricção logística e de comunicação que impede que alimentos excedentes em boas condições cheguem rapidamente a quem precisa antes de perderem a validade. O problema central é a ausência de um sistema automatizado de triagem e roteamento que conecte a oferta de doações à demanda das instituições de forma ágil, reduzindo a burocracia e otimizando o tempo de coleta.

Público-Alvo (Doadores vs. ONGs)

    Doadores (Oferta): Supermercados, restaurantes, padarias, organizadores de eventos e cidadãos que possuem alimentos excedentes (preparados ou in natura) próprios para consumo e buscam uma maneira rápida e sem atritos para repassá-los.

    ONGs e Receptores (Demanda): Bancos de alimentos, cozinhas solidárias, abrigos e instituições de assistência social que necessitam de um fluxo constante de insumos para alimentar populações vulneráveis e precisam de roteiros de coleta inteligentes baseados em proximidade.

Escopo das Intenções Tratadas e Dados Coletados no Chat

Intenções Tratadas (via módulo NLU e ML):

    Oferta de Doação: O usuário informa que tem alimentos disponíveis para repasse.

    Solicitação de Insumos: A ONG sinaliza a necessidade urgente de determinadas categorias de alimentos.

    Dúvidas e Suporte: Perguntas sobre o funcionamento da plataforma, regras de segurança alimentar ou itens permitidos.

Gestão de Ticket: Confirmação, alteração ou cancelamento de uma coleta já agendada.

    Dados Extraídos e Coletados no Chat (via Regex e Interação):

    Tipo de Alimento: Classificação do item (ex: perecível, não perecível, refeições prontas, hortifruti).

    Quantidade e Massa: Volume exato da doação capturado por expressões regulares (ex: "50 kg de carne", "30 marmitas").

    Validade e Tempo de Consumo: Datas de fabricação e prazo limite para consumo seguro, garantindo a viabilidade da doação.

    Localização (CEP/Endereço): Ponto de origem e destino para o algoritmo KNN calcular a menor distância e fazer o match ideal.

    Janela de Coleta: Horários disponíveis para a retirada ou entrega dos alimentos.


prompt logo do projeto: "Faça uma logo de um hambúrguer mordido igual da Apple, e troque a folha por uma azeitona"