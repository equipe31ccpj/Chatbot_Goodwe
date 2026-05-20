# GoodWe ChargeGrid Intelligence ⚡🤖

## 📋 Descrição do Projeto
O **GoodWe ChargeGrid Intelligence** é um assistente virtual inteligente integrado ao sistema residencial e comercial "HCA G2" da GoodWe. O objetivo do chatbot é atuar como um suporte técnico e operacional de primeira linha, ajudando usuários a compreenderem dados de carregamento de veículos elétricos, regras de segurança contra sobrecarga e tabelas complexas de tarifação dinâmica com base no fluxo da rede e incentivos de energia solar.

---

## 👥 Integrantes
* **[Akin Alexandre Mendes Martins]** - RM: [572773]
* **[Maria Eduarda Rocha Benjamim]** - RM: [570544]
* **[Pedro Henrique Neves]** - RM: [571382]

---

## ⚠️ Problema Abordado
Com a expansão dos eletropostos e carregadores residenciais de alta potência, os usuários enfrentam dificuldades em entender fatores técnicos e financeiros de suas recargas. Os principais problemas identificados são:
1.  **Complexidade na Tarifação:** O valor do kWh varia de acordo com o horário (Pico, Mediano, Baixa) e a incidência de energia solar (Incentivo Solar GoodWe).
2.  **Falta de Clareza em Falhas:** Quando o carregador interrompe o funcionamento por segurança (limite de 8.8 kW no modelo HCA G2), o usuário comum muitas vezes não compreende o motivo da parada técnica.
3.  **Monitoramento Térmico:** Dificuldade em correlacionar a temperatura de operação com a potência consumida pelo veículo.

---

## 💡 Proposta do Chatbot
O chatbot foi projetado para responder de forma **técnica, direta e exclusiva** sobre o ecossistema do carregador HCA G2 e do PowerGrid. 

### Principais Funcionalidades:
* **Cálculo e Explicação de Tarifas:** Detalha como o preço-base (R$ 1.50/kWh) é modificado pelos fatores de pico ou descontos solares das 10h às 14h.
* **Suporte de Segurança:** Explica alertas de sobrecarga e orienta o usuário em caso de interrupção preventiva de recarga.
* **Interface Fluida e Responsiva:** Um chat moderno, totalmente adaptável a telas de computadores e notebooks, que processa e formata automaticamente respostas complexas vindas da IA.

---

## 🛠️ Tecnologias Selecionadas e Justificativa Técnica

O projeto foi construído utilizando uma arquitetura leve, moderna e escalável:

### 1. Python & Flask (Backend)
* **Justificativa:** O **Flask** foi escolhido por ser um micro-framework Web extremamente leve e rápido para prototipar APIs. Ele gerencia as rotas do aplicativo (como o envio de mensagens) e serve o front-end sem a necessidade de configurações complexas de servidores que frameworks maiores (como o Django) exigiriam.

### 2. Groq API (LLM)
* **Justificativa:** A plataforma **Groq** foi integrada por fornecer o processamento de modelos de linguagem de grande porte (LLMs) com a menor latência do mercado através de seus chips LPU (*Language Processing Units*). Isso garante que o usuário receba respostas instantâneas no chat, simulando uma conversa humana em tempo real com excelente precisão técnica guiada por *System Prompt*.

### 3. HTML5, CSS3 Customizado & JavaScript Puro (Frontend)
* **Justificativa:** Optou-se por construir a interface do chat do zero usando **CSS Flexbox** dinâmico e **JavaScript Vanilla**. O CSS foi otimizado para ajustar a altura com base na tela do usuário (`vh`), garantindo que o campo de input nunca suma. O JavaScript trata a conversão de textos puros e Markdown da IA em tags HTML estruturadas (`innerHTML`), permitindo negritos e listas limpas sem carregar bibliotecas pesadas de terceiros.

### 4. Python-Dotenv
* **Justificativa:** Utilizado para gerenciar variáveis de ambiente de forma segura (`.env`). Ele impede que dados sensíveis, como a chave privada da API da Groq (`GROQ_API_KEY`), fiquem expostos diretamente no código-fonte ou no repositório do GitHub.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado na sua máquina.

### 1. Clonar o Repositório e Instalar Dependências
No terminal, instale as bibliotecas listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt

### 2. Configurar a Chave da API

GROQ_API_KEY=sua_chave_da_api_aqui

### 3. Iniciar o Servidor Flask

python app.py