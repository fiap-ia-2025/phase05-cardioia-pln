# 🌐 Fase 5 – Assistente Cardiológico Inteligente: Experiência do Paciente

## 👥 Grupo 61

## 👨‍🎓 Integrantes

- Amanda Vieira Pires (RM566330)
- Ana Gabriela Soares Santos (RM565235)
- Bianca Nascimento de Santa Cruz Oliveira (RM561390)
- Milena Pereira dos Santos Silva (RM565464)
- Nayana Mehta Miazaki (RM565045)

## 👩‍🏫 Professores

### Tutor

- Caique Nonato

### Coordenador(a)

- André Godoi

---

## 🎯 Visão Geral

Após o monitoramento, análise visual e a prototipação, nessa fase vamos construir um assistente inteligente (chatbot) com o objetivo de realizar atendimentos iniciais, orientar sobre exames e triar sintomas cardiológicos.

O foco será a comunicação inteligente e a experiência do paciente através de diálogos entre o chatbot e o paciente. Utilizando o Processamento de Linguagem Natural (PLN) para interpretação das mensagens e apresentação de forma clara e segura as orientações sobre exames, classificação dos sintomas cardiológicos, identificação de situações de risco e direcionamento adequado ao quadro do paciente.

# 📊 Parte 1 – Assistente Conversacional com NLP

## 🎯 Objetivo

A primeira etapa é a estruturação do assistente conversacional do IBM Watson Assistant com Processamento de Linguagem Natural (PLN) e conectá-lo a infraestrutura do CardioIA.

## ☁️ Criando Watson Assistant 

Através do [CloudIBM](https://cloud.ibm.com/) criamos um watsonx Assistant e configuramos o nome do assistente como **"CardioIA"** com sua mensagem de saudação:

> Olá! Sou o CardioIA, seu assistente virtual de orientação em saúde cardiovascular. Como posso te ajudar hoje?

E as primeiras sugestões de perguntas para o paciente fazer:

1. Quais são os sintomas de infarto?
2. Como funciona triagem de sintomas?
3. Em caso de emergência, o que fazer?

## 🚀 Criando Ações  

A cada sugestão de perguntas, configuramos variações que o paciente pode fazer da mesma pergunta e a resposta que o assistente virtual deverá fornecer em todos os casos.

*Por exemplo:* na pergunta **"Em caso de emergência, o que fazer?"**

O paciente também pode perguntar:

- O que fazer em caso de emergência?
- Qual o número do SAMU?
- Preciso de ajuda médica urgente
- Emergência médica

E para todas essas opções de perguntas, o assistente virtual terá a mesma resposta:

> Em qualquer situação de emergência médica ou suspeita de infarto, ligue imediatamente para o SAMU no número 192 ou dirija-se ao pronto-socorro mais próximo.
Atenção: Não tente dirigir se estiver passando mal. Mantenha a pessoa calma e em repouso até a chegada do socorro.

Finalizando assim a ação do assistente virtual.

Acesse a documentação `RELATORIO.md` para ver todas as possibilidades de diálogo entre o assistente virtual e o paciente.

## 🛠️ Arquitetura do Backend (`app.py`)

### Estruturação
```
phase05-cardioia-pln/
│
├── app.py                  # Servidor Flask e integração com IBM watsonx Assistant
├── requirements.txt        # Lista de dependências Python para instalação
├── README.md               # Documentação técnica e guia de execução
├── RELATORIO.md            # Documentação das ações do watson assistant
│
├── static/                 # Arquivos estáticos servidos pelo Flask
│   └── img/
│       ├── avatar.png      # Foto de perfil do assistente CardioIA
│       └── background.png  # Imagem de fundo temática de cardiologia
│
└── templates/
    └── index.html          # Interface do usuário 
```

### 1. Autenticação e Inicialização
- Com a `IAMAuthenticator` é possível validar a `API KEY`.
- Aponta para o endpoint regional da IBM em `us-east` (região selecionada na configuração do assistente virtual) através da função `set_service_url()`.

### 2. Rotas de Aplicação

- `@app.route('/')`: para renderizar a página principal do assistente virtual `index.html`.
- `@app.route('/send_message', methods=['POST'])`: endpoint JSON que recebe a mensagem do paciente via frontend, enviando a API da IBM e retornando com a resposta cofigurada previamente no assistente virtual.

### 3. Comunicação Stateless
- `assistant_id`: identificação da instância da aplicação.
- `environment_id`: identificador do ambiente, nesse caso já publicado `LIVE_ID`.
- `user_id`: identificador de controle e autoria do paciente usuário.

### 4. Identificação de Erros

- Captura de falhas de comunicação ou inconsistências de paramêtros com `try-except`.

# 🧠 Parte 2 – Interface de Interação com o Usuário

## 🎯 Objetivo

O objetivo é criar a interface web (*frontend*) do paciente usuário da CardioIA, a fim de oferecer uma experiência de chat limpa e responsiva. Sua principal função é capturar as mensagens do paciente e enviá-las ao *backend*, exibindo as respostas de triagem da IBM em tempo real e sem recarregar a página.

### Design

- Layout clean em formato de card centralizado na tela.
- Tom de vermelho assemelhando à área da saúde de cardiologia.
- Fonte com legibilidade.
- Integração com a imagem do avatar.
- Rotulagem das mensagens quando é o assistente virtual e o paciente.
- Balões de diálog em alinhamentos opostos para identificação da fonte da mensagens, assemelhando a outros chats utilizados no dia-a-dia.

### Comunicação ao backend

- Envio dinâmico da mensagem ao backend sem recarregar a página.
- Mantém histórico da conversa enquanto mantém na página.

# 🚀 Instruções de Execução

## 📋 Pré-requisitos
`Python 3.8+` devidamente instalado.

## 📌 Passos
### 1. Clonar repositório do github 
```bash
git clone https://github.com/fiap-ia-2025/phase05-cardioia-pln.git
cd phase05-cardioia-pln
```

### 2. Instalar bibliotecas necessárias
```bash
pip install -r requirements.txt
```

### 3. Iniciar a aplicação Flask
```bash
python app.py
```

### 4. Acessar a interface web
Copie e cole no seu navegador: **http://127.0.0.1:5000**

### 5. Faça perguntas ao assistente virtual

Exemplo de perguntas: 

1. Quais são os sintomas de infarto?
2. Como funciona triagem de sintomas?
3. Em caso de emergência, o que fazer?

Acesse a documentação `RELATORIO.md` para ver todas as possibilidades de diálogo entre o assistente virtual e o paciente.

## 🏁 Conclusão

O **CardioIA** foi desenvolvido para demonstrar como a integração entre uma arquitetura web leve em Flask e os serviços avançados em **Processamento de Linguagem Natural** (PLN) da **IBM Cloud (watsonx Assistant)** pode proporcionar uma ferramente de triagem médica eficiente, acessível e segura.

Através de uma interface responsiva, o assistente virtual atua como um canal de comunicação direto para responder a dúvidas frequentes sobre saúde cardíaca.

## 🎬 Vídeo explicativo

[Link do vídeo](https://youtu.be/aojf98vFXQo)