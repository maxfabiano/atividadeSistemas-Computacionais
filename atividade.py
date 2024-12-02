# Código para ESP32 para medir e enviar a intensidade do sinal Wi-Fi

import network
import machine
import time
import ubinascii
from umqtt.simple import MQTTClient

# Configurações de rede
SSID = 'Seu_SSID'
PASSWORD = 'Sua_Senha'

# Configurações MQTT
MQTT_SERVER = 'broker.exemplo.com'
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b'casa/sinal_wifi'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando-se à rede...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print('Conexão estabelecida:', wlan.ifconfig())

def connect_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_SERVER)
    client.connect()
    print('Conectado ao broker MQTT')
    return client

def medir_sinal():
    wlan = network.WLAN(network.STA_IF)
    return wlan.status('rssi')

def main():
    connect_wifi()
    client = connect_mqtt()
    while True:
        rssi = medir_sinal()
        mensagem = '{"sensor_id": "' + CLIENT_ID.decode() + '", "rssi": ' + str(rssi) + '}'
        client.publish(TOPIC, mensagem)
        print('Mensagem enviada:', mensagem)
        time.sleep(60)  # Envia dados a cada 60 segundos

if __name__ == '__main__':
    main()
