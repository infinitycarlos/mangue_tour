from flask import Blueprint
from .controllers.ponto_controller import get_pontos
from .controllers.rota_controller import calcular_rota
from .controllers.localizacao_controller import atualizar_localizacao

main = Blueprint('main', __name__)

main.route('/pontos', methods=['GET'])(get_pontos)
main.route('/rota', methods=['GET'])(calcular_rota)
main.route('/localizacao', methods=['POST'])(atualizar_localizacao)