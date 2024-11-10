import os
import pandas as pd
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

# Configurações do banco de dados.
app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
app.config['MYSQL_USER'] = os.getenv("DB_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB_NAME")

mysql = MySQL(app)

def ingestao_dados():
    # Lê o arquivo CSV.
    df = pd.read_csv('C:/Users/rlsor/Desktop/mangue_tour/data/arquivo_combinado.csv')

    # Substitui NaN por None para evitar erros de inserção no MySQL.
    df = df.where(pd.notnull(df), None)

    # Conexão com o banco de dados.
    conn = mysql.connection
    cursor = conn.cursor()

    for index, row in df.iterrows():
        try:
            # Inserir na tabela Pontos_Turisticos
            cursor.execute("""
                INSERT INTO Pontos_Turisticos (Nome_Ponto, Descricao_Ponto, Bairro, Latitude, Longitude, Logradouro, Telefone, Site)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row['nome'],
                row['descricao'],
                row['bairro'],
                row['latitude'],
                row['longitude'],
                row['logradouro'],
                row['telefone'],
                row['site']
            ))
            print(f"Adicionado: {row['nome']} na tabela Pontos_Turisticos")

            # Inserir na tabela categoria_turismo
            cursor.execute("""
                INSERT INTO categoria_turismo (Nome_Categoria)
                VALUES (%s)
            """, (row['categoria'],))
            print(f"Adicionado: {row['categoria']} na tabela categoria_turismo")

        except Exception as err:
            print(f"Erro: {err}")
    
def inserir_dados_coordenadas():
    with app.app_context():
        conn = mysql.connection
        cursor = conn.cursor()
        
        # Inserir dados na tabela coordenadas
        try:
            cursor.execute("""
                INSERT INTO coordenadas (idCoordenadas, latitude, longitude)
                VALUES (%s, %s, %s)
            """, (1, -8.071313, -34.880809))
            conn.commit()
            print("Dados inseridos com sucesso na tabela coordenadas.")
        except Exception as err:
            print(f"Erro ao inserir dados: {err}")

        cursor.close()

def inserir_dados_coordenadas():
    with app.app_context():
        conn = mysql.connection
        cursor = conn.cursor()
        
        # Lê o arquivo CSV
        df = pd.read_csv('C:/Users/rlsor/Desktop/mangue_tour/data/arquivo_combinado.csv')

        # Itera sobre cada linha do DataFrame
        for index, row in df.iterrows():
            try:
                # Insere os dados de coordenadas na tabela
                cursor.execute("""
                    INSERT INTO coordenadas (idCoordenadas, latitude, longitude)
                    VALUES (%s, %s, %s)
                """, (index + 1, row['latitude'], row['longitude']))
                conn.commit()
                print(f"Dados inseridos com sucesso para o índice {index}.")
            except Exception as err:
                print(f"Erro ao inserir dados para o índice {index}: {err}")

        cursor.close()
        
    conn.commit()
    cursor.close()

if __name__ == "__main__":
    with app.app_context():
        ingestao_dados()
        