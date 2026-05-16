# Lobinho chatbot
Ele é um chatbot que fiz para estudar um pouco python, flask e subprocess para fazer projetos maiores no futuro quando eu souber mais

# o que ele incluí
ele inclui uma interface web onde dá de digitar em um ```<input>``` e ele será jogado num ollama que aparece a resposta na interface web.
ele consegue listar o histórico de conversas com sintaxe jinja2 e variáveis ```conversation``` e ```historico```

# licença
esse projeto é licenciado pelo mit, leia o arquivo license para mais detalhes.
# como instalar

primeiro instale o ollama e o venv
```bash
sudo apt update && sudo apt install python3-venv -y && curl -fsSL https://ollama.com/install.sh | sh
```
depois dê pull no modelo llama3.2:3b
```bash
ollama pull llama3.2:3b
```
após isso baixe o código do lobinho chatbot
```bash
git clone "https://github.com/pixelcatbr/lobinho-chatbot.git"
```
entre na pasta criada
```bash
cd lobinho-chatbot/
```
e crie um venv
```bash
python3 -m venv venv
```
após criar o venv entre no venv
```bash
source venv/bin/activate
```
instale as dependências
```bash
pip install flask
```
e após tudo isso execute o main.py
```bash
python3 main.py
```
# contribuição
contribua com meus projetos como este aqui fazendo pull requests e forks.

