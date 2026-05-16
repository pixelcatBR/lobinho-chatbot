import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

conversation = []

@app.route('/')
def home():
    return render_template('index.html', conversation=conversation)

@app.route('/user_input')
def generate_text():
    user_input = request.args.get('user_input', '')
    
    if user_input:
        conversation.append({'role': 'user', 'content': user_input})
        
        historico = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation[:-1]])

        prompt = f"""Você é um chatbot chamado Lobinho. Você fala de forma descontraída e informal, 
mas sem muitas gírias. Evite ficar muito formal.
        
Histórico da conversa:
{historico}

Usuário disse agora: {user_input}

Lobinho, responda de forma natural e amigável:"""

        try:
            resultado = subprocess.run(
                ['ollama', 'run', 'llama3.2:3b', prompt],
                capture_output=True,
                text=True,
                timeout=30
            )
            ai_response = resultado.stdout.strip()

            if not ai_response and resultado.stderr:
                ai_response = f"Erro: {resultado.stderr[:200]}"
            elif not ai_response:
                ai_response = "Como posso ajudar você hoje?"
                
        except subprocess.TimeoutExpired:
            ai_response = "Desculpe, demorei muito para responder. Pode repetir?"
        except Exception as e:
            ai_response = f"Desculpe, tive um erro: {str(e)}"
        
        conversation.append({'role': 'ai', 'content': ai_response})
    
    return render_template('index.html', conversation=conversation)
@app.route('/clear')
def clear():
    global conversation
    conversation = []
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
