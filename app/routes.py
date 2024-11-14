from flask import Blueprint
from .controllers.ponto_controller import get_pontos_turisticos
from .controllers.roteiro_controller import add_roteiro, get_roteiros, delete_roteiro

main = Blueprint('main', __name__)

# Rotas para pontos turísticos.
main.route('/pontos', methods=['GET'])(get_pontos_turisticos)

# Rotas para roteiros.
main.route('/roteiros', methods=['POST'])(add_roteiro)
main.route('/roteiros', methods=['GET'])(get_roteiros)
main.route('/roteiros/<int:id>', methods=['DELETE'])(delete_roteiro)