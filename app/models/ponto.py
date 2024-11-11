from .. import mysql

class Ponto:
    
    def __init__(self, nome, descricao, latitude, longitude, logradouro, bairro, cidade, coordenadas_idcoordenadas, telefone=None, site=None):
        self.nome = nome
        self.descricao = descricao
        self.latitude = latitude
        self.longitude = longitude
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.coordenadas_idcoordenadas = coordenadas_idcoordenadas 
        self.telefone = telefone or ''
        self.site = site or ''
    
    def save(self):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO Pontos_Turisticos (Nome_Ponto, Descricao_Ponto, Latitude, Longitude,
                                                Logradouro, Bairro, Cidade, Coordenadas_idCoordenadas, Telefone, Site)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (self.nome, self.descricao, self.latitude, self.longitude, self.logradouro, self.bairro, self.cidade, self.coordenadas_idcoordenadas, self.telefone, self.site))
            mysql.connection.commit()
            return True

        except Exception as e:
            print(e)  
            return False

        finally:
            cursor.close()

    @classmethod 
    def get_all(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Pontos_Turisticos")
        resultados = cursor.fetchall()
        cursor.close()

        return [{'ID_Ponto': ponto[0], 'Nome_Ponto': ponto[1], 'Descricao_Ponto': ponto[2],
                 'Latitude': ponto[3], 'Longitude': ponto[4], 'Logradouro': ponto[5],
                 'Bairro': ponto[6], 'Cidade': ponto[7], 'Coordenadas_idCoordenadas': ponto[8],
                 'Telefone': ponto[9], 'Site': ponto[10]} for ponto in resultados]

    @classmethod 
    def delete(cls, id):
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("DELETE FROM Pontos_Turisticos WHERE ID_Ponto=%s", (id,))
            mysql.connection.commit()
            return True
        
        except Exception as e:
            print(e)  
            return False
        
        finally:
            cursor.close()