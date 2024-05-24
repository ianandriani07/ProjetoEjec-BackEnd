from flask import Flask, request, jsonify
from helpers import listaMembros

app = Flask(__name__)

@app.route('/listaMembros')
def listaMembros():
    membros = listaMembros()
    return membros

@app.route('/listaMembros/<int:id>')
def listarMembros(id):
    membros = listarMembros(id)
    return membros

@app.route("/novoMembro")
def novoMembro(data_json):
    data_json = request.get_json()
    lista_atualizada = novoMembro(data_json)
    return jsonify(lista_atualizada)
    
if __name__ == '__main__':
    app.run()