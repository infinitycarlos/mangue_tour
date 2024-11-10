from .. import mysql

class Ponto:
    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Pontos_Turisticos")
        resultados = cursor.fetchall()
        cursor.close()
        
        return [{'IDPonto': ponto[0], 'Nome': ponto[1], 'Descricao': ponto[2], 'Latitude': ponto[3], 'Longitude': ponto[4]} for ponto in resultados]