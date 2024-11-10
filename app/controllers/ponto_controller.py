from flask import jsonify
from ..models.ponto import Ponto

def get_pontos():
    pontos = Ponto.get_all()
    return jsonify(pontos)