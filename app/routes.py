from flask import Blueprint
from .controllers.auth_controller import register_user, login_user
from .controllers.ponto_controller import ingestao_dados, get_pontos_turisticos
from .controllers.avaliacao_controller import avaliar_ponto, get_avaliacoes

main = Blueprint('main', __name__)

# Rotas de autenticação.
main.route('/register', methods=['POST'])(register_user)
main.route('/login', methods=['POST'])(login_user)

# Rotas para pontos turísticos.
main.route('/pontos', methods=['POST'])(ingestao_dados)
main.route('/pontos', methods=['GET'])(get_pontos_turisticos)

# Rotas para avaliações.
main.route('/avaliacao', methods=['POST'])(avaliar_ponto)
main.route('/avaliacoes', methods=['GET'])(get_avaliacoes)