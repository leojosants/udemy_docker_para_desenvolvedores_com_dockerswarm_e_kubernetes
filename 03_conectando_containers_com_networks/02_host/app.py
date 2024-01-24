from flask import Flask
from flask import request, json, jsonify

import requests

from flask_mysqldb import MySQL

# iniciar
app = Flask(__name__)

# exibicao de mensagens no terminal
app.config["DEBUG"] = True

# configuracao MySQL
app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'senha_do_db'
app.config['MYSQL_DB'] = 'flaskhost'

mysql = MySQL(app)

# rota para receber dados da api externa
@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

# rota para insercao de dados
@app.route("/inserthost", methods=["POST"])
def inserthost():
     data = requests.get('https://randomuser.me/api').json()
     username = data['results'][0]['name']['first']   
     cur = mysql.connection.cursor()
     cur.execute("""INSERT INTO users(name) VALUES(%s)""", (username,))
     mysql.connection.commit()
     cur.close()
     return username

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")