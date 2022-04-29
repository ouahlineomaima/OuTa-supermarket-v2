import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="root",
                             database="gestionstock")
cursor = db.cursor()
cursor.execute("select * from gestionnaire")