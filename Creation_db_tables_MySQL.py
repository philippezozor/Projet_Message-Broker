import mysql.connector


#connexion a MYSQL
db = mysql.connector.connect(
  host = "localhost",
  port=3306,
  user = "root",
  password = "example",
)
#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()

#exécuter le curseur avec la méthode execute() et transmettre la requête SQL
# Creation de la database binance
cur.execute("CREATE DATABASE IF NOT EXISTS Binance_db")

cur.execute("USE Binance_db")

#Creation de  3tables BTC, XRP et ETH
cur.execute("CREATE TABLE IF NOT EXISTS Bitcoin (datetime datetime, Open Double, High Double, Low Double, Close Double, Volume Double)")
#XRP
cur.execute("CREATE TABLE IF NOT EXISTS Ripple (datetime datetime, Open Double, High Double, Low Double, Close Double, Volume Double)")
#ETH
cur.execute("CREATE TABLE IF NOT EXISTS Ethereum (datetime datetime, Open Double, High Double, Low Double, Close Double, Volume Double)")

# cur.execute("DROP TABLE ...")