from flask import request, jsonify
from ..models.ponto import Ponto

def ingestao_dados():
    data = request.get_json()
    
    nome = data.get('Nome_Ponto')
    descricao = data.get('Descricao_Ponto')
    latitude = data.get('Latitude')
    longitude = data.get('Longitude')
    logradouro = data.get('Logradouro')
    bairro = data.get('Bairro')
    cidade = data.get('Cidade')
    cep = data.get('CEP')

    ponto = Ponto(nome=nome, descricao=descricao, latitude=latitude, longitude=longitude,
                  logradouro=logradouro, bairro=bairro, cidade=cidade, cep=cep)
    
    if ponto.save():  # Salvar no banco de dados.
        return jsonify({"msg": "Ponto turístico adicionado com sucesso"}), 201
    
    return jsonify({"msg": "Erro ao adicionar ponto turístico"}), 400

def get_pontos_turisticos():
    pontos = Ponto.get_all()  # Método que busca todos os pontos turísticos.
    
    return jsonify(pontos)