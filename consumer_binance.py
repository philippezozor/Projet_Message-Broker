from kafka import KafkaConsumer
import json
import pprint
import threading
import time
from datetime import datetime
import mysql.connector



cBinance = KafkaConsumer('Binance', bootstrap_servers=['kafka101:9092'])#, api_version=(2,6,0))


#connexion a MYSQL
db = mysql.connector.connect(
  host = "mysql_db",
  port=3306,
  user = "root",
  password = "example",
  database = "Binance_db"
)
#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
    
    
def addDataBaseBinance(msg):
    #récupération du message
  msg.offset
  datas = json.loads(msg.value)

    # print(data)
    # #insértion dans un dataset
  for data in datas["BTC"]:
    date = datetime.fromtimestamp(data[0]/1000)
    req = "INSERT INTO Bitcoin (Datetime, Open, High, Low, Close, Volume) VALUES(%s, %s, %s, %s, %s, %s)"
    data = (date,data[1],data[2],data[3],data[4],data[5])
    cur.execute(req,data)
    db.commit()
# recuperation et chargement des données de XRP dans MySQL
  for data in datas["XRP"]:
    date = datetime.fromtimestamp(data[0]/1000)
    req_xrp = "INSERT INTO Ripple (Datetime, Open, High, Low, Close, Volume) VALUES(%s, %s, %s, %s, %s, %s)"
    data_xrp = (date,data[1],data[2],data[3],data[4],data[5])
    cur.execute(req_xrp,data_xrp)
    db.commit()
# recuperation et chargement des données de XRP dans MySQL
  for data in datas['ETH']:
    date = datetime.fromtimestamp(data[0]/1000)
    req_eth = "INSERT INTO Ethereum (Datetime, Open, High, Low, Close, Volume) VALUES(%s, %s, %s, %s, %s, %s)"
    data_eth = (date,data[1],data[2],data[3],data[4],data[5])
    cur.execute(req_eth,data_eth)
    db.commit()
# Timer de 5 min avant de relancer la boucle     
    # time.sleep(10)]
    
for msg in cBinance:
    addDataBaseBinance(msg)  
    
    
    
