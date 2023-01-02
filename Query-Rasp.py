
import mysql.connector

cnx = mysql.connector.connect(user='adrianlan', password='1234',
                                 host='192.168.100.158',
                                 database='coviddetector')
cursor = cnx.cursor()
query = ("SELECT id, nombre, temp FROM registro WHERE temp>40")


cursor.execute(query)

for (id, nombre, temp) in cursor:
  print(id, nombre, temp)

cursor.close()
cnx.close()
