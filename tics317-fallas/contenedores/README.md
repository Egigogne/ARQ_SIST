![Logo](../mvc/assets/UAI.png)
# Arquitectura de Sistemas: TICS317

---
¡Bienvenidos al repositorio de Arquitectura!. Acá haremos algunos ejercicios complementarios a las clases para profundizar los aprendizajes




# ¿Que necesitamos?
| **Categoría**                  | **Biblioteca**                                                                                          | **Descripción**                                                        |
|-------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| **1. Manejo de archivos**     | [![json](https://img.shields.io/badge/json-estándar-yellow)](https://docs.python.org/3/library/json.html) | Lectura y escritura de archivos `.json` para almacenar las tareas.     |
| **2. Sistema de archivos**    | [![os](https://img.shields.io/badge/os-estándar-yellow)](https://docs.python.org/3/library/os.html)       | Interacción con el sistema de archivos (opcional, si lo usaste).       |
| **3. Tipado estático**        | [![typing](https://img.shields.io/badge/typing-estándar-yellow)](https://docs.python.org/3/library/typing.html) | Anotaciones de tipo para mayor claridad y validación estática.         |



### El proyecto se desarrolla en:

* Enviroment de Python [![versions](https://img.shields.io/badge/python-3.13-white)](https://www.python.org/downloads/)

* Entorno de Desarrollo Integrado (IDE) [![versions](https://img.shields.io/badge/PyCharm-2024.3.4-white)](https://www.jetbrains.com/help/pycharm/installation-guide.html)

---
## 📦 Contenedor (Container)

### Definición

> **Un contenedor es simplemente el término que se utiliza para una instancia en ejecución de una imagen.**
> 
> Boettiger, C. (2015). 


Un contenedor es una unidad estándar de software que empaqueta el código y todas sus dependencias para que la aplicación se ejecute de manera rápida y confiable en diferentes entornos computacionales.

A diferencia de las máquinas virtuales, los contenedores comparten el mismo sistema operativo del host pero se ejecutan de forma aislada, lo que permite eficiencia, portabilidad y consistencia entre entornos de desarrollo, prueba y producción.

| Característica              | Máquina Virtual (VM)                              | Contenedor                                      |
|----------------------------|---------------------------------------------------|------------------------------------------------|
| **Aislamiento**            | Aíslan a nivel de sistema operativo completo      | Aíslan a nivel de proceso                       |
| **Kernel**                 | Cada VM tiene su propio kernel                    | Comparten el kernel del sistema anfitrión       |
| **Peso**                   | Pesadas (incluyen SO completo)                    | Ligeros (solo incluyen lo necesario para correr)|
| **Velocidad de arranque**  | Lenta (requiere iniciar un SO completo)           | Rápida (solo inicia un proceso)                 |
| **Uso de recursos**        | Alto                                              | Bajo                                            |
| **Portabilidad**           | Menos portables (dependen del hipervisor)         | Muy portables (se ejecutan en cualquier sistema con Docker) |
| **Casos de uso comunes**   | Entornos con múltiples SO, servidores virtuales   | Microservicios, despliegue ágil de aplicaciones |

### ¿Por qué usar contendores?

Los contenedores son:

**Autónomos** Cada contenedor tiene todo lo que necesita para funcionar sin depender de ninguna dependencia preinstalada en la máquina anfitriona.

**Aislados** Como los contenedores se ejecutan de forma aislada, tienen una influencia mínima en el anfitrión y en otros contenedores, lo que aumenta la seguridad de tus aplicaciones.

**Independientes** Cada contenedor se gestiona de forma independiente. Eliminar un contenedor no afectará a los demás.

**Portátiles** ¡Los contenedores pueden ejecutarse en cualquier lugar! El contenedor que se ejecuta en tu máquina de desarrollo funcionará de la misma manera en un centro de datos o en cualquier lugar de la nube.


 ---
<p>
  <img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" alt="Docker Logo" width="50" style="vertical-align: middle;"/>
  <strong style="font-size: 1.2em; vertical-align: middle;"> DOCKER </strong>
</p>

---
> Los contenedores ofrecen un mecanismo lógico de empaquetado en el que las aplicaciones pueden abstraerse del entorno en el que realmente se ejecutan. Esta desvinculación permite que las aplicaciones basadas en contenedores se implementen de forma fácil y consistente, sin importar si el entorno de destino es un centro de datos privado, la nube pública o incluso el computador personal de un desarrollador. Esto les da a los desarrolladores la capacidad de crear entornos predecibles que están aislados del resto de las aplicaciones y que pueden ejecutarse en cualquier lugar. 


### Docker-File

> Un Dockerfile es un archivo de texto simple que contiene una lista de comandos que el cliente de Docker ejecuta al crear una imagen. Es una forma sencilla de automatizar el proceso de creación de imágenes. La mejor parte es que los comandos que escribes en un Dockerfile son casi idénticos a sus equivalentes en Linux. Esto significa que no necesitas aprender una nueva sintaxis para crear tus propios dockerfiles. 


---

## Actividad en clase

### Paso 1. Instalar Docker

Para usar la herramienta la descargamos de:

- https://docs.docker.com/desktop/setup/install/windows-install/

Sigue los pasos de instalación que se indican en la documentacón de Docker.


### Paso 2. Crear Dockerfile en tu IDE

Crea una copia de la carpeta monolitic (previamente creada) y genera un archivo Dockerfile:

```Dockerfile
# Iniciamos nuestra imagen con la de python 3.13 ligera
FROM python:3.13.3-slim

# Definimos el directorio que servirá como el directorio principal de la app.
WORKDIR /app

# Copiamos nuestro código en la imagen.
COPY main.py /app/
#COPY tasks.json /app/

# Comando para ejecutar el código.
CMD ["python", "main.py"]
```


### Paso 3. Usar la aplicación con Docker:

1. Construya la imagen docker, en este ejemplo la llamamos "task-manager":
```shell
docker build -t task-manager .
```
2. Ejecute el contenedor con la imagen previamente creada:
```shell
docker run -it task-manager
```
**Nota**: Las opciones `-it` indican que el código requiere inputs interactivos del usuario.

**Nota**: tenga en cuenta que el código genera un archivo *tasks.json* dentro del contenedor
y este desaparecerá una vez que el contenedor se detenga.
Para persistir el documento, puede montar un volumen en el contenedor
ejecutándolo con el siguiente comando:
```shell
docker run -it -v $(PWD):/app task-manager
```
Esto hará el que archivos *tasks.json* se guarden en la ruta donde se ejecuta el comando.

NOTA: es posible que falle el `docker run -it -v $(PWD):/app task-manager`; El problema está en cómo el sistema interpreta la variable de entorno `$(PWD)` para el directorio actual. Hay varias formas de solucionarlo, por ejemplo, se puede probar con otras alternativas:

**Alternativa 1:**

> ```shell
> docker run -it -v ${PWD}:/app task-manager
> ```

**Alternativa 2:**

> ```shell
> docker run -it -v "$(pwd)":/app task-manager
> ```

**Alternativa 3:**

> ```shell
> docker run -it -v "$(PWD):/app" task-manager
> ```

**Alternativa n:**

⋮
---


---
### Compartir la imagen

Paso 1: Guarda la imagen en un archivo
```shell
docker save -o task-manager.tar task-manager
```

Paso 2 (en el otro equipo): Importar la imagen
```shell
docker load -i task-manager.tar
```

Paso 3 ejecutar desde el terminal de Docker Destkop

```shell
docker run -it task-manager
```

# Recursos complementarios 
- https://docs.docker.com/guides/python/containerize/
- https://docs.docker.com/guides/python/
- https://www.fullstackpython.com/docker.html
- https://docs.docker.com/desktop/setup/install/windows-install/
- https://docs.docker.com/desktop/setup/install/mac-install/
---

# Referencias

> Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.
---
<center>TICS 317 - Arquitectura de Sistemas</center>


