from flask import Blueprint
from .controllers.auth_controller import register_user, login_user
from .controllers.ponto_controller import add_ponto_turistico, get_pontos_turisticos, delete_ponto_turistico
from .controllers.roteiro_controller import add_roteiro, get_roteiros, delete_roteiro

main = Blueprint('main', __name__)

# Rotas de autenticação.
main.route('/register', methods=['POST'])(register_user)
main.route('/login', methods=['POST'])(login_user)

# Rotas para pontos turísticos.
main.route('/pontos', methods=['POST'])(add_ponto_turistico)
main.route('/pontos', methods=['GET'])(get_pontos_turisticos)
main.route('/pontos/<int:id>', methods=['DELETE'])(delete_ponto_turistico)

# Rotas para roteiros.
main.route('/roteiros', methods=['POST'])(add_roteiro)
main.route('/roteiros', methods=['GET'])(get_roteiros)
main.route('/roteiros/<int:id>', methods=['DELETE'])(delete_roteiro)