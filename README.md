# Organizador de Notas Fiscais em XML

Este repositório contém um programa desenvolvido para organizar notas fiscais eletrônicas (NFe) no formato XML. A solução foi criada com o objetivo de automatizar o processo de separação, triagem e processamento de notas fiscais, facilitando a gestão de informações essenciais para o controle de vendas e análise de dados.

## Por que desenvolvi isso?

Eu tinha uma rotina diária de envio de Notas Fiscais para um sistema de pagamento para Diferenças de Alíquotas entre estados (DIFAL). Contudo, apenas algumas naturezas de operação deveriam gerar a guia GNRE para pagamento. 

Eu demorava em torno de 45 minutos todos os dias para separar quais as notas tinham ou não que ir para o sistema de pagamento (ele não fazia essa distinção sozinho, se eu jogasse um XML indevido ali, ele seria pago do mesmo jeito...)

Mas existia um padrão dessas notas. Com um conjunto de regras claras eu pude idealizar esse script **à prova de erros humanos** e que **me devolveu 40 minutos do meu tempo produtivo** todos os dias. 

## Como funciona?

Você só precisa criar uma pasta nomeada com o dia do mês e colocar os arquivos XML lá dentro. Em seguida, execute o `main.py` 

### 1. Separador de XMLs (Módulo `org.py`)

O módulo **org.py** é responsável por realizar a organização dos arquivos XML recebidos diariamente. Ele realiza as seguintes etapas:

- Extrai os arquivos XML compactados em .zip para uma pasta específica do dia.
- Separa os arquivos XML de acordo com as "Naturezas de Operação" permitidas, movendo aqueles indevidos para uma pasta separada e consolidando os restantes em uma pasta destinada aos arquivos válidos.

Com isso, a triagem manual de arquivos é eliminada, tornando o processo de organização mais rápido e eficiente.

### 2. Análise de Vendas (Módulo `stats.py`)

Embora não incluído neste repositório, o módulo **stats.py** é mencionado para fins de referência. Esse módulo foi desenvolvido para processar informações como faturamento, quantidade de itens vendidos e calcular indicadores de desempenho. O módulo gerava relatórios detalhados sobre as vendas, que ajudavam na tomada de decisões estratégicas.

### 3. Processamento de Produtos Estratégicos (Módulo `VAR.py`)

O módulo **VAR.py** é utilizado para realizar a busca de vendas de produtos específicos considerados estratégicos. Ele é configurável para determinar quais produtos devem ser acompanhados e quantificar as vendas ao longo do período analisado.

### 4. Envio dos XMLs para a Aplicação de pagamentos

O último passo consistia em enviar os XMLs separados e validados para upload na plataforma de pagamento das guias GNRE. Esse processo nesse momento do projeto era manual.

## Estrutura do Projeto

- **main.py**: Ponto de entrada do programa. Coordena a execução dos diferentes módulos, exibindo as informações necessárias de maneira organizada e intuitiva.
- **org.py**: Contém a lógica de separação dos XMLs, identificando e organizando arquivos conforme as regras predefinidas.
- **VAR.py**: Realiza o processamento de produtos estratégicos, permitindo identificar produtos de destaque nas vendas.

## Como Utilizar

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/organizador-xml.git
   ```

2. Navegue até a pasta do projeto:

   ```bash
   cd organizador-xml
   ```

3. Execute o script principal:

   ```bash
   python main.py
   ```

Certifique-se de que os arquivos XML estejam em uma pasta com o nome correspondente ao dia do mês atual (ex.: "15" para o dia 15).

## Exemplo de Uso

- Ao executar o script principal, o programa irá organizar os XMLs do dia, identificar e mover arquivos indevidos, processar estatísticas de vendas e quantificar produtos estratégicos.

## Tecnologias Utilizadas

- **Python 3.9+**
- **Bibliotecas**: pathlib, xml.etree.ElementTree, shutil, zipfile

## Considerações Finais

Os próximos passos desse projeto eram automatizar mais ainda, implementando o seguinte:

- Script vai até o ERP e baixa sozinho esses XMLs consolidados do dia, cria a pasta do dia de "hoje" e inicia o script `org.py`.
- Após todos os scripts em `main.py` serem executados, ele pegaria os XMLs e faria o upload automático na plataforma de pagamento das GNREs.

Esse projeto não foi continuado pois a aplicação que estávamos usando para pagar as guias GNREs estava dando muito problema e a triagem de XMLs não era mais necessária.

Mas, para quem precisa separar arquivos XML, essa solução é muito útil!

Fique à vontade para entrar em contato, sugerir melhorias ou mesmo copiar e usar! Estou sempre aberto a novas ideias e oportunidades para desenvolver soluções que tragam valor real para as empresas.

---

Qualquer sugestão ou dúvida, estou à disposição!

