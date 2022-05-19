import os              #Para hacer llamados al sistema
import time            #Para poder programar la descarga de datos cada cierto tiempo
import csv             #Para gestionar archivos csv
import mysql.connector #Para realizar la conexion a la base de datos


nombre_archivo_google_forms =  "Formulario PYMEs.csv"


def solicitar_formulario_respuestas():
    limpiar_directorio_SYSTEM_COMMAND = "rm 'Formulario PYMEs.csv.zip' ; rm " + "'" + nombre_archivo_google_forms + "'"
    descargar_datos_SYSTEM_COMMAND = """   wget --header="Host: docs.google.com" --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" --header="Accept-Language: es-419,es;q=0.9" --header="Referer: https://docs.google.com/forms/d/1GyjOFTs8YtbJYSPJNH7xVFg0qTAYXkVCpHAjhT01-0M/edit" --header="Cookie: S=spreadsheet_forms=zNuRhAM_1aOJZ1z0Z5y1jsIHiOC2nZ_eQjMFeOGAxj0; COMPASS=spreadsheet_forms=CjIACWuJV7Y3r2mSy-WzZ7QDKy87z91dD6G9C0BxQK4445N9ag2zS-8qdeDZDAAIiXyxmxCXtYqUBho0AAlriVcLpBVlqzEGp2gSuQPNlaAMysiZBCaqa_Xcovl-V4uOwzvBQXfTqPzNaIFhc8aI9Q==; SID=Jwhy2coRSb0cD9OirMh52t5UGM_COpAS7rLfjzX6OvcUq9fQrWeucyKpOVrGBLzCDK_pWA.; __Secure-1PSID=Jwhy2coRSb0cD9OirMh52t5UGM_COpAS7rLfjzX6OvcUq9fQxWFwD43hlZu7MNQjYjB6bw.; __Secure-3PSID=Jwhy2coRSb0cD9OirMh52t5UGM_COpAS7rLfjzX6OvcUq9fQaZIUr1Wqc-Etyo-8r__P2Q.; HSID=A8EiaKO1NoxZ6xUwg; SSID=AvVjWTsMFhtoMpc7e; APISID=8hwb-cnMVRAmZAOj/AmIpXax9O62oszVLG; SAPISID=cvW3f5mNpqVnGKK5/AMSpv2aiWc6yp01Xj; __Secure-1PAPISID=cvW3f5mNpqVnGKK5/AMSpv2aiWc6yp01Xj; __Secure-3PAPISID=cvW3f5mNpqVnGKK5/AMSpv2aiWc6yp01Xj; SEARCH_SAMESITE=CgQIrZUB; 1P_JAR=2022-05-16-17; AEC=AakniGOxJ7U4eSlwQpASV1qqQ4zCVldkXCDpTHHeVRg4LLsxUeQUbwkxwA; NID=511=OIIv0nKUrMN8vF60CsVvX5liHhXdagz2OjzeiPTaKkOKI9BZqaujyy6v1BdIRB8iU3Xw1PCYTY4AYuLdo-vg9zw_I3tZK37vmv7BdMFHo3aB5HC5wxta8X50DwgJE13yQMH-qg7flWbVtvb4obuSSCBljs-xfIXw9OLBq1D0K4cMuViQqGV5WheuzLLbHs8Tqyo86QSXsGJX4_eR2TdQ2LSHkCPpLvkIbu3wNZd8VXHZTTAG9LdWgKfhREcVsOtn29UFTwqgH2K19WdPq6ilbQWQKh2t63Ag2WPVXkNDVI7JwGPx_zGQW702vYEr08SWg46ScbAkoKwhczWM6wfjNuUgMFRMttrBkNIjsbM0QWSz; OTZ=6506980_76_80_134400_76_436740; SIDCC=AJi4QfE6qqYVn5w6HFAnKzEneGAayGRQvteFkyqTwJQiVzNDRMs2-WkVerlaIiAx0_3QPvSdVrM; __Secure-3PSIDCC=AJi4QfFWLZgajKdnGp7JHLtmd8cr4RhPPVVqJwaZp_qgacC808QrmlKCIU3pHnJBvZc27ApVg-0" --header="Connection: keep-alive" "https://docs.google.com/forms/u/0/d/1GyjOFTs8YtbJYSPJNH7xVFg0qTAYXkVCpHAjhT01-0M/downloadresponses?tz_offset=-18000000&sort_by_timestamp=true" -c -O 'Formulario PYMEs.csv.zip'   """
    desempaquetar_datos_SYSTEM_COMMAND = " unzip 'Formulario PYMEs.csv.zip' "
    
    secuencia_de_comandos_SYSTEM_COMMAND = limpiar_directorio_SYSTEM_COMMAND + " ; " + descargar_datos_SYSTEM_COMMAND + " ; " + desempaquetar_datos_SYSTEM_COMMAND

    os.system(secuencia_de_comandos_SYSTEM_COMMAND)


def limpiar_BD():
    conexion_BD = mysql.connector.connect( 
        host='localhost', 
        user= 'root', 
        passwd='', 
        db='Encuesta_database'
    ) 
    cursor = conexion_BD.cursor()
    sql_statement = "DELETE FROM EncuestasRespondidas"
    cursor.execute(sql_statement)
    conexion_BD.commit()
    conexion_BD.close()


def procesar_formulario_respuestas_csv():
    with open(nombre_archivo_google_forms, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            print(line_count)
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                #line_count += 1
            print(row["Marca temporal"])
            agregar_registro_a_BD(row)
            line_count += 1
        print(line_count)
        print(f'Processed {line_count} lines.') 


def agregar_registro_a_BD(registro):
    conexion_BD = mysql.connector.connect( 
        host='localhost', 
        user= 'root', 
        passwd='', 
        db='Encuesta_database'
    ) 
    cursor = conexion_BD.cursor()
    sql_statement = "INSERT INTO EncuestasRespondidas (MarcaDeTiempo, Correo, NombreCompleto, Edad, Sexo, NombreNegocio, InicioOperaciones, DireccionNegocio, NumEmpleados, IngresosMensuales, EgresosMensuales) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = ( registro["Marca temporal"], 
            registro["Correo electrónico"],
            registro["Nombre completo"],
            registro["Edad (años)"],
            registro["Sexo"],
            registro["Nombre del negocio"],
            registro["Fecha de inicio de operaciones"],
            registro["Dirección de su negocio"],
            registro["Número de empleados"],
            registro["Ingresos mensuales"],
            registro["Egresos mensuales"]
    )

    cursor.execute(sql_statement, val)
    conexion_BD.commit()
    conexion_BD.close()
    
    print("Registro agregado a la base de datos exitosamente")



if __name__ == "__main__":

    while (True):
        solicitar_formulario_respuestas()
        limpiar_BD()
        procesar_formulario_respuestas_csv()
        time.sleep(1)
    
