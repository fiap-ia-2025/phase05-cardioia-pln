from flask import Flask, render_template, request, jsonify
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)

# Configurações do Watson
API_KEY = '0jpvFpfGbttkV7Rd9PGVSmCw7S-NIHmQdm3pOs5GK-q1'
URL = 'https://api.us-east.assistant.watson.cloud.ibm.com/instances/842e5dd4-40ec-49ba-8c38-258e14abf90c'
ASSISTANT_ID = '10337352-b865-4b32-acc3-7825d06d528d'
ENVIRONMENT_ID = 'ccd33a7a-b676-447b-a7c4-eafb38dc7b12'

# Autenticação na IBM
authenticator = IAMAuthenticator(API_KEY)
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=authenticator
)
assistant.set_service_url(URL)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message', '')

    try:
        response = assistant.message_stateless(
            assistant_id=ASSISTANT_ID,
            environment_id=ENVIRONMENT_ID,
            input={
                'message_type': 'text',
                'text': user_message
            },
            user_id='usuario_web'
        ).get_result()

        generic_responses = response['output']['generic']
        bot_reply = ""
        for resp in generic_responses:
            if resp['response_type'] == 'text':
                bot_reply += resp['text'] + "\n\n"

        return jsonify({'response': bot_reply.strip()})

    except Exception as e:
        error_msg = e.message if hasattr(e, 'message') else str(e)
        return jsonify({'response': f"Erro na conexão com o assistente: {error_msg}"}), 500

if __name__ == '__main__':
    app.run(debug=True)