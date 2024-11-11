from datetime import datetime
from flask import request,jsonify 
from ..models.roteiro import Roteiro 

def add_roteiro(): 
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

def delete_roteiro(id): 
   roteiro_deleted=Roteiro.delete(id) 
    
   if roteiro_deleted: 
       return jsonify({"msg":"Roteiro deletado com sucesso"}),200 
    
   return jsonify({"msg":"Erro ao deletar roteiro"}),400 