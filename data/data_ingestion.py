import csv
import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='turismo_db'
)
cursor = conn.cursor()

# Criação da tabela se não existir para usuários e pontos turísticos.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    ID INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PontosTuristicos (
    IDPonto INT NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Descricao LONGTEXT NOT NULL,
    Latitude DECIMAL(9,6) NOT NULL,
    Longitude DECIMAL(9,6) NOT NULL,
    PRIMARY KEY (IDPonto)
);
""")

# Leitura do CSV e inserção no banco de dados.
with open('data/pontos_turisticos.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
        INSERT INTO PontosTuristicos (Nome, Descricao, Latitude, Longitude)
        VALUES (%s, %s, %s, %s)
        """, (row['Nome'], row['Descricao'], row['Latitude'], row['Longitude']))

conn.commit()
cursor.close()
conn.close()