from .. import mysql

class Ponto:
    
    def __init__(self, nome, descricao, latitude, longitude, logradouro, bairro, cidade, cep):
        self.nome = nome
        self.descricao = descricao
        self.latitude = latitude
        self.longitude = longitude
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
    
    @classmethod
    def get_all(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Pontos_Turisticos")
        resultados = cursor.fetchall()
        cursor.close()
        
        return [{'ID_Ponto': ponto[0], 'Nome_Ponto': ponto[1], 'Descricao_Ponto': ponto[2],
                 'Latitude': ponto[3], 'Longitude': ponto[4], 'Logradouro': ponto[5],
                 'Bairro': ponto[6], 'Cidade': ponto[7], 'CEP': ponto[8]} for ponto in resultados]

    def save(self):
        cursor = mysql.connection.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO Pontos_Turisticos (Nome_Ponto, Descricao_Ponto, Latitude, Longitude,
                                                Logradouro, Bairro, Cidade, CEP)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (self.nome, self.descricao, self.latitude,
                  self.longitude, self.logradouro,
                  self.bairro, self.cidade,
                  self.cep))
            mysql.connection.commit()
            return True
        
        except Exception as e:
            print(e)  # Log de erro em produção.
            return False
        
        finally:
            cursor.close()