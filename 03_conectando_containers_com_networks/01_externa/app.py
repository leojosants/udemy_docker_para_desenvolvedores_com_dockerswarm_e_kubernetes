# framework
import flask 

# libs
from flask import request, json, jsonify

# para uso em api externa
import requests

# iniciar
app = flask.Flask(__name__)

# exibicao de mensagens no terminal
app.config["DEBUG"] = True

# rota para receber dados da api externa
@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")