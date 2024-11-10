from flask import request, jsonify
from ..models.avaliacao import Avaliacao

def avaliar_ponto():
    data = request.get_json()
    
    nota_avaliacao = data.get('Nota_Avaliacao')
    comentario = data.get('Comentario')
    usuario_id_usuario = data.get('Usuario_ID_Usuario')
    id_roteiro = data.get('Id_Roteiro')
    
    avaliacao = Avaliacao(nota=nota_avaliacao,
                          comentario=comentario,
                          usuario_id_usuario=usuario_id_usuario,
                          id_roteiro=id_roteiro)
    
    if avaliacao.save():  # Salvar no banco de dados.
        return jsonify({"msg": "Avaliação adicionada com sucesso"}), 201
    
    return jsonify({"msg": "Erro ao adicionar avaliação"}), 400

def get_avaliacoes():
    avaliacoes = Avaliacao.get_all()  # Método que busca todas as avaliações.
    
    return jsonify(avaliacoes)