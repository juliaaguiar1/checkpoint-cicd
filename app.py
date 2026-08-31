from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Checkpoint CI/CD funcionando com sucesso!"

@app.route("/sobre")
def sobre():
    return "Projeto desenvolvido para o checkpoint de Integração e Entrega Contínua."

@app.route("/status")
def status():
    return "Sistema online e funcionando corretamente!"

if __name__ == "__main__":
    app.run(debug=True)