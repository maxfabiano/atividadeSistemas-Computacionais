# Código em Python para analisar os dados de sinal Wi-Fi

import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="avaliacao_wifi"
)

cursor = db.cursor()

# Consulta para obter os dados
query = "SELECT sensor_id, rssi, timestamp FROM sinais_wifi"
cursor.execute(query)
result = cursor.fetchall()

# Criação de DataFrame
df = pd.DataFrame(result, columns=['Sensor_ID', 'RSSI', 'Timestamp'])

# Mapeamento dos sensores para cômodos
sensor_to_room = {
    'sensor_1': 'Garagem',
    'sensor_2': 'Sala',
    'sensor_3': 'Cozinha',
    'sensor_4': 'Quarto 1',
    'sensor_5': 'Quarto 2',
    'sensor_6': 'Quarto 3',
    'sensor_7': 'Quarto 4'
}

df['Cômodo'] = df['Sensor_ID'].map(sensor_to_room)

# Plotagem dos resultados
plt.figure(figsize=(12, 8))
sns.lineplot(data=df, x='Timestamp', y='RSSI', hue='Cômodo')
plt.title('Intensidade do Sinal Wi-Fi por Cômodo ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('RSSI (dBm)')
plt.legend(title='Cômodo')
plt.show()
