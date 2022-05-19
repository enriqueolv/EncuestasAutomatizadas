
############################################################################################
##Creación de un usuario nuevo




############################################################################################
##Creación de la base de datos y sus tablas


CREATE DATABASE IF NOT EXISTS Encuesta_database;
USE Encuesta_database;
CREATE TABLE EncuestasRespondidas(
    MarcaDeTiempo     varchar(500),
    Correo            varchar(500),
    NombreCompleto    varchar(500),
    Edad              varchar(500),
    Sexo              varchar(500),
    NombreNegocio     varchar(500),
    InicioOperaciones varchar(500),
    DireccionNegocio  varchar(500),
    NumEmpleados      varchar(500),
    IngresosMensuales varchar(500),
    EgresosMensuales  varchar(500)
);


############################################################################################
##Insertando un registro en la tabla
USE Encuesta_database;
INSERT INTO EncuestasRespondidas(
    MarcaDeTiempo,
    Correo,
    NombreCompleto,
    Edad,
    Sexo,
    NombreNegocio,
    InicioOperaciones,
    DireccionNegocio,
    NumEmpleados,
    IngresosMensuales,
    EgresosMensuales
)
VALUES(
    "2022/04/15 3:23:56 PM EST",
    "kevinenriqueoogm@gmail.com",
    "Kevin Enrique Ortega Olvera",
    "23",
    "Masculino",
    "Tacos Supremos",
    "2022-01-01",
    "Carretera México-Toluca Km 23",
    "8",
    "20000",
    "10000"
);



############################################################################################
##Consultando registros y borrando registros

SELECT * FROM EncuestasRespondidas;
DELETE FROM EncuestasRespondidas;