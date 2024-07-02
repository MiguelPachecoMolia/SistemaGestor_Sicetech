# SistemaGestor_Sicetech
Desarrollo de un sistema de gestión integral diseñado para una empresa que brinda servicios de seguridad al hogar.

## Prueba del codigo
* Descargar o clonar los archivos de mi repositorio.
* Asegurar de tener docker e inicializar la imagen de MongoDB: docker run -d --name miguel_proyecto -p 27017:27017 mongo:latest
* Ejecutar el archivo principal: python main.py

## Funciones del programa
= MENU PRINCIPAL =
1. Servicios
   * Consulta todos los servicios
   * Registrar un nuevo servicio: se solicita el id del cliente al que se realizara el servico (Se valida si existe ese cliente), posteriormente se pedira los detalles del servicio.
   * Agregar un empleado a un servicio: ingresaras el id del servicio para posteriormente ingresar los id de los empleados. (Se valida si existe ese servicio y los empleados)
   * Elimiar servicio: Se solicita el id del servicio a eliminar, este tambien desaparecera del historial de servicios de tanto clientes como empleados

2.- Empleados
  * Consultar todos los empleados: Muestra todos los empleados registrados en la bd
  * Eliminar un empleado: Se solicita el id del empleado a eliminar (Se valida si existe ese id)
  * Registrar un nuevo tecnico: El programa pedira ingresar sus datos
  * Registrar un nuevo ayudante general: El programa pedira ingresar sus datos

3.- Clientes
  * Consultar todos los clientes: Muestra todos los clientes registrados en la bd
  * Eliminar un cliente: Se solicita el id del cliente a eliminar (Se valida si existe ese id)
  * Registrar un nuevo cliente: El programa pedira ingresar sus datos

4.- Inventario
  * Pendiente

5.- Consultas
  * Servicios por cliente: Muestrar todos los servicios solicitas por cada cliente
  * Servicios Totales por cliente: Calcula el costo total de todos los servicios solicitas por cada cliente
  * Servicios por region: Muestra los serivicios realizados por region deseada:
      - Estado: Se muestran el total con los ids de los servicios realizados por estado
      - Municipio: Se solicita el nombre del estado y se muestran el total de servicios realizados con sus ids por cada municipio de ese estado
      - Colonia: Se solicita el nombre del estado y municipo, se muestran el total de servicios realizados con sus ids por cada colonia de ese municipio
