from flask import request, jsonify
from ..models.ponto import Ponto

def get_pontos_turisticos():
    pontos = Ponto.get_all()  # Método que busca todos os pontos turísticos.
    return jsonify(pontos)