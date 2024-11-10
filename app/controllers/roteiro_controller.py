from datetime import datetime
from flask import request,jsonify 
from ..models.roteiro import Roteiro 

def criar_roteiro(): 
   data=request.get_json() 
   nome=data.get('Nome_Roteiro') 
   usuario_id=data.get('Usuario_ID_Usuario') 
   roteiro=Roteiro(nome=nome,data_criacao=datetime.now(),usuario_id_usuario=usuario_id) 

   if roteiro.save(): 
       return jsonify({"msg":"Roteiro criado com sucesso"}),201 

   return jsonify({"msg":"Erro ao criar roteiro"}),400 

def get_roteiros(): 
   roteiros=Roteiro.get_all() 
   return jsonify(roteiros) 