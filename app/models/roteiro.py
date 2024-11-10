from datetime import datetime
from .. import mysql 

class Roteiro: 

   def __init__(self,nome,data_criacao=None,id_usuario=None): 
       self.nome=nome 
       self.data_criacao=data_criacao or datetime.now() 
       self.usuario_id_usuario=id_usuario 

   @classmethod 
   def get_all(cls): 
       cursor=mysql.connection.cursor() 
       cursor.execute("SELECT * FROM Roteiros") 
       resultados=cursor.fetchall() 
       cursor.close() 

       return [{'ID_Roteiro': roteiro[0],'Nome_Roteiro': roteiro[1],'Data_Criacao': roteiro[2],'Usuario_ID_Usuario': roteiro[3]} for roteiro in resultados] 

   def save(self): 
       cursor=mysql.connection.cursor() 

       try: 
           cursor.execute(""" 
               INSERT INTO Roteiros (Nome_Roteiro ,Data_Criacao ,Usuario_ID_Usuario) VALUES (%s,NOW(),%s)""", (self.nome,self.usuario_id_usuario)) 
           mysql.connection.commit() 
           return True 

       except Exception as e: 
           print(e)  
           return False 

       finally: 
           cursor.close() 