# Microservicio _flights-ms_

Este microservicio se enfoca en las funcionalidades para los vuelos, principalmente las siguientes:

* Permitir a los usuarios buscar vuelos.
* Permitir que los usuarios puedan filtrar vuelos de acuerdo a las fechas de partida (_departure_), origen y destino.
* Manejar la información acerca de estos vuelos.

## Instrucciones de Uso

1. Se debe clonar el repositorio de GitHub usando el siguiente comando:

```
git clone https://github.com/jubedoyat/flights-ms.git
```

2. Posteriormente, la carpeta donde se haya clonado debe ser abierta desde un editor de código como Visual Code Studio (VSCode), o bien acceder a la carpeta desde una terminal.

3. (Opcional) Una vez en la terminal del editor o del sistema operativo, se debe crear un entorno virtual con el siguiente comando:

```
python -m venv venv
```

Y tras esto activarlo así:

```
source venv/bin/activate
```

4. Luego se instalan los paquetes necesarios para ejecutar el microservicio:

```
pip install -r requirements.txt
```

5. Después, para ejcutar el microservicio, se debe usar el siguiente comando:

```
uvicorn app.main:app --reload --port 8001
```

6. Por último se accede al servidor usando la siguiente dirección en un navegador web:

```
http://127.0.0.1:8001
```

## Endpoints

- `/flights/`: obtiene todos los vuelos almacenados en la base de datos de MongoDB sin hacer distinción.
- `/flights/{flight_id}`: busca un vuelo que tenga una `_id` en específico.
- `flights/search/`: busca todos los vuelos que cumplan con algún criterio de búsqueda (ciudad de origen, destino y/o fecha de partida).

### Uso

Para usar estos endpoints se recomienda hacer uso de la página de _Swager_ accediendo a través del camino `/docs/`, allí aparecerán todos los endpoints ya mencionados, además de campos de texto para ingresar los parámetros necesarios para cada petición, los cuales vienen definidos continuación junto con el resultado esperado de cada endpoint.

#### Parámetros

- `/flights/`: Ninguno. 
- `/flights/{flight_id}`: un id del vuelo que se quiere buscar. En caso de no existir, se retornará una lista vacía.
- `flights/search/`:
    * `date`: cadena de caracteres que representa la fecha deseada para el vuelo que se busca.
    * `origin`: cadena de caracteres que contiene el nombre de la ciudad de origen deseada para el vuelo.
    * `destiny`: cadena de caracteres que contiene el nombre de la ciudad de destino.

### Resultados

- `/flights/`: lista con todos los vuelos registrados en la base de datos. Devuelve una lista vacía en caso de no encontrar ninguno.
- `/flights/{flight_id}`: lista con un único registro del vuelo que tenga el id provisto. Devuelve una lista vacía en caso de no encontrar ninguno.
- `flights/search/`: lista con todos los vuelos que cumplan con las condiciones dadas de fecha, origen y/o destino. Retorna una lista vacía en caso de no encontrarse ninguno.