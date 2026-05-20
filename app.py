import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key_groq = os.environ.get("GROQ_API_KEY")

if not api_key_groq:
    raise ValueError("ERRO: A variável GROQ_API_KEY não foi encontrada. Verifique se o arquivo .env está configurado corretamente.")

client = Groq(api_key=api_key_groq)
SYSTEM_PROMPT = """
Você é o assistente virtual integrado ao "Sistema HCA G2" da GoodWe (Carregador Residencial/Comercial conectado ao PowerGrid). Seu papel é auxiliar os usuários cadastrados no sistema a entenderem o relatório de recarga, o funcionamento dos totens e a lógica de precificação.

Você deve responder com base EXCLUSIVA nas seguintes especificações técnicas do nosso sistema:

1. ESPECIFICAÇÕES DO SISTEMA HCA G2:
- Potência Nominal do Carregador: 22 kW.
- Limite de Segurança/Sobrecarga: Se a potência real ultrapassar 8.8 kW, o sistema sofre uma interrupção por sobrecarga e interrompe o carregamento para manutenção.
- Temperatura Operacional: Varia entre 30.0°C e 45.0°C em condições regulares (potência menor ou igual a 7.15 kW) e de 70.0°C a 95.0°C sob alta performance (potência maior que 7.15 kW).

2. LÓGICA DE TARIFAÇÃO INTELIGENTE (Preço Base: R$ 1.50 por kWh):
O preço final depende do fluxo da rede elétrica e do "Incentivo Solar GoodWe":
- Horário de PICO: Fator multiplicador de 1.40. Se o Incentivo Solar estiver ativo, o fator cai para 1.25.
- Horário MEDIANO: Fator multiplicador de 1.00. Se o Incentivo Solar estiver ativo, cai para 0.85.
- Horário de BAIXA: Fator multiplicador de 0.90. Se o Incentivo Solar estiver ativo, cai para 0.70.
- Horário REGULAR: Fator multiplicador de 1.00. Se o Incentivo Solar estiver ativo, cai para 0.85.

3. INCENTIVO SOLAR GOODWE (Janela de Geração):
- Fica ativo exclusivamente para recargas realizadas entre 10h00 e 14h00. Ele concede descontos nos fatores multiplicadores de todas as faixas de fluxo por utilizar energia solar excedente.

DIRETRIZES DE COMPORTAMENTO:
- Responda apenas a dúvidas sobre o faturamento inteligente, proteção contra sobrecarga, o incentivo solar, o status do HCA G2 e o PowerGrid.
- Se o usuário perguntar algo fora do escopo do sistema de carregamento GoodWe, recuse cordialmente.
- Mantenha um tom técnico, prestativo e direto.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar_mensagem", methods=["POST"])
def enviar_mensagem():
    try:
        data = request.get_json()
        mensagem_usuario = data.get("mensagem", "")
        
        if not mensagem_usuario:
            return jsonify({"resposta": "Por favor, digite uma mensagem válida."}), 400

        chat_completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": mensagem_usuario}
            ],
            temperature=0.3, 
            max_tokens=512
        )
        
        resposta_ia = chat_completion.choices[0].message.content
        return jsonify({"resposta": resposta_ia})

    except Exception as e:
        print(f"Erro na requisição: {e}")
        return jsonify({"resposta": "Desculpe, ocorreu um erro ao processar sua resposta na API do Groq."}), 500

if __name__ == "__main__":
    app.run(debug=True)