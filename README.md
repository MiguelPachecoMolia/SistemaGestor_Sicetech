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


## Explicación de la Estructura:
* main.py: Es el archivo principal de tu programa.

* clases/: Directorio que contiene las definiciones de tus clases.
  - persona_class.py: Define la clase abstracta Persona con atributos comunes como nombre, dirección, teléfono, y correo.
  - cliente_class.py: Define la clase Cliente, que hereda de Persona, con atributos específicos como id_cliente, servicios (lista de servicios solicitados), y fecha_registro.
  - empleado_class.py: Define la clase Empleado, que hereda de Persona, con atributos como id_empleado,  fecha_ingreso, y historial_servicios.
  - servicios_class.py: Define la clase Servicio con atributos relacionados con los servicios.
  - inventario_class.py: Define la clase Inventario con atributos relacionados con el inventario de productos.

* menú/: Directorio que contiene scripts para manejar diferentes menús y operaciones específicas.
  - servicios.py: Funcionalidades relacionadas con los servicios.
  - empleados.py: Funcionalidades relacionadas con los empleados.
  - clientes.py: Funcionalidades relacionadas con los clientes.
  - inventario.py: Funcionalidades relacionadas con el inventario.
  - analisis.py: Funcionalidades relacionadas con las consultas de datos.

* database.py: Script para manejar la conexión y operaciones con la base de datos (MongoDB).

* utils.py: Funciones de utilidad como limpiar la pantalla y la generacion de ids no repetidos.
