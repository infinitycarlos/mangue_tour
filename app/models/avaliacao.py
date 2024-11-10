from .. import mysql

class Avaliacao:
    
    def __init__(self, nota, comentario=None, usuario_id_usuario=None, id_roteiro=None):
        self.nota = nota
        self.comentario = comentario or ''
        self.usuario_id_usuario = usuario_id_usuario or None 
        self.id_roteiro = id_roteiro or None 

    @classmethod 
    def get_all(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Avaliacao")
        resultados = cursor.fetchall()
        cursor.close()

        return [{'ID_Avaliacao': avaliacao[0], 'Nota_Avaliacao': avaliacao[1],
                 'Comentario': avaliacao[2], 'Data_Avaliacao': avaliacao[3],
                 'Usuario_ID_Usuario': avaliacao[4], 'Id_Roteiro': avaliacao[5]} for avaliacao in resultados]

    
    def save(self):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO Avaliacao (Nota_Avaliacao, Comentario,
                                        Data_Avaliacao,
                                        Usuario_ID_Usuario,
                                        Id_Roteiro)
                VALUES (%s,%s,NOW(),%s,%s)
            """, (self.nota,self.comentario,self.usuario_id_usuario,self.id_roteiro))
            mysql.connection.commit()
            return True
            
        except Exception as e:
            print(e)  
            return False
            
        finally:
            cursor.close()