import mysql.connector


print ("Resultados de mysql.connector:")
miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='Encuesta_database')
cur = miConexion.cursor()
cur.execute( "SELECT * FROM EncuestasRespondidas" )
for NombreCompleto in cur.fetchall() :
    print (NombreCompleto)
miConexion.close()