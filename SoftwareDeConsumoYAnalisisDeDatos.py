import csv             #Para gestionar archivos csv
import mysql.connector #Para realizar la conexion a la base de datos


global conexion_BD

def conenectar_BD():
    global conexion_BD
    conexion_BD = mysql.connector.connect(
        host='localhost', 
        user= 'root', 
        passwd='', 
        db='Encuesta_database'
    )


def desconectar_BD():
    global conexion_BD
    conexion_BD.close()


def solicitar_registros_EncuestasRespondidas_BD():
    global conexion_BD
    if conexion_BD is None:
        print ("La base de datos no ha sido conectada")
        exit

    sql_statement = "SELECT * FROM EncuestasRespondidas"
    cursor = conexion_BD.cursor()
    cursor.execute(sql_statement)

    return cursor.fetchall()


def recomponer_archivo_csv(registros_EncuestasRespondidas):
    f = open('RegistrosRecompuesto.csv', 'w')
    writer = csv.writer(f)
    writer.writerow([
        "Marca temporal",
        "Correo electrónico",
        "Nombre completo",
        "Edad (años)",
        "Sexo",
        "Nombre de su negocio",
        "Fecha de inicio de operaciones",
        "Dirección de su negocio",
        "Número de empleados",
        "Ingresos mensuales",
        "Egresos mensuales"
    ])
    for registro in registros_EncuestasRespondidas:
        writer.writerow(registro)
    f.close()

def get_edad_promedio_encuestados(registros_EncuestasRespondidas):
    suma_edades = 0
    for registro in registros_EncuestasRespondidas:
        suma_edades = suma_edades + int(registro[3])
    promedio = suma_edades / len(registros_EncuestasRespondidas)
    return promedio 

def get_cantidad_encuestados_femenino(registros_EncuestasRespondidas):
    encuestados_femenino = 0
    for registro in registros_EncuestasRespondidas:
        if (registro[4] == "Femenino"):
            encuestados_femenino = encuestados_femenino + 1
    return encuestados_femenino

def get_cantidad_encuestados_masculino(registros_EncuestasRespondidas):
    encuestados_masculino = 0
    for registro in registros_EncuestasRespondidas:
        if (registro[4] == "Masculino"):
            encuestados_masculino = encuestados_masculino + 1
    return encuestados_masculino



if __name__ == "__main__":
    conenectar_BD()
    registros_EncuestasRespondidas = solicitar_registros_EncuestasRespondidas_BD()
    desconectar_BD()
    
    #GENERAR ARCHIVO
    recomponer_archivo_csv(registros_EncuestasRespondidas)

    #ESTADISTICAS
    promedio = get_edad_promedio_encuestados(registros_EncuestasRespondidas)
    print("Edad promeido de emprendedores: " + str(promedio) + " años")
    encuestados_femenino = get_cantidad_encuestados_femenino(registros_EncuestasRespondidas)
    print("Total de encuestados de género femenino: " + str(encuestados_femenino))
    encuestados_masculino = get_cantidad_encuestados_masculino(registros_EncuestasRespondidas)
    print("Total de encuestados de género masculino: " + str(encuestados_masculino))



   

    