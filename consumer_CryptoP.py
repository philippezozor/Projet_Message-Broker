from kafka import KafkaConsumer
import json
import pprint
import threading
import time
import datetime
from pymongo import MongoClient

client = MongoClient('mongo', 27017)
cCryptoPanic = KafkaConsumer('CryptoPanic', bootstrap_servers=['kafka101:9092'])#, api_version=(2,6,0))

#Création de db
db = client.database

#Création de post 
postCryptoPanic = db.posts
postXRP = db.coursXRP
postBTC = db.coursBTC
postETH = db.coursETH

#Fonction définissant si un post est bon ou mauvais
def isGood(votes):
    good = votes["positive"]+votes["saved"]
    bad = votes["disliked"]+votes["negative"]+votes["toxic"]

    if good>bad:
        return 'good'
    else:
        'bad'


def addDataBaseCrypto(msg):
    #récupération du message
    msg.offset
    post = json.loads(msg.value)

    #insértion dans un dataset
    for i in post["post"]:
        ts = time.mktime(datetime.datetime.strptime(i["published_at"], "%Y-%m-%dT%H:%M:%SZ").timetuple())
        if ts >= ((time.time())-(1*3600)):
            i["votes"] = isGood(i["votes"])
            i["published_at"] = ts
            postCryptoPanic.insert_one(i)

    print(db.list_collection_names())
    for postCrypto in postCryptoPanic.find():
        pprint.pprint(postCrypto)

print("Répondez par 'oui' ou 'non' - Voulez vous supprimez les tables déjà présente dans la bd mongo - cette action est irréversible :")
rep = input()

if rep=="oui":
    postXRP.drop()
    postBTC.drop()
    postETH.drop()
    postCryptoPanic.drop()

for msg in cCryptoPanic:
    addDataBaseCrypto(msg)