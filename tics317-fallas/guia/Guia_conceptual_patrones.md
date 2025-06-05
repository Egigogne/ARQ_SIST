![Logo](../mvc/assets/UAI.png)
# Arquitectura de Sistemas: TICS317

---
# Resumen de Patrones de Diseño de Software

Los patrones de diseño son soluciones reutilizables a problemas comunes en el diseño de software. Ayudan a mejorar la mantenibilidad, reutilización y escalabilidad de los sistemas.

Se dividen en tres grandes categorías:

---

##  1. Patrones Creacionales

Estos patrones se enfocan en el proceso de creación de objetos, encapsulando la lógica de instanciación y promoviendo la flexibilidad.

###  Singleton
- **Propósito:** Asegura que una clase solo tenga una instancia y proporciona un punto de acceso global a ella.
- **Ejemplo:** Un gestor de configuración de aplicación.

###  Factory Method
- **Propósito:** Define una interfaz para la creación de un objeto, pero permite que las subclases decidan qué clase instanciar. El Factory Method permite que una clase delegue la instanciación en sus subclases.

###  Abstract Factory
- **Propósito:** Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.
- **Ejemplo:** Una fábrica de interfaces para múltiples plataformas (Windows, MacOS, Linux).

###  Builder
- **Propósito:** Separa la construcción de un objeto complejo de su representación, de modo que el mismo proceso de construcción pueda crear diferentes representaciones.
- **Ejemplo:** Construcción de un documento con múltiples secciones opcionales.

###  Prototype
- **Propósito:** Especifica los tipos de objetos a crear utilizando una instancia prototípica, y crea nuevos objetos copiando este prototipo.
- **Ejemplo:** Clonar configuraciones de usuario en una aplicación.

---

##  2. Patrones Estructurales

Estos patrones se enfocan en la composición de clases y objetos para formar estructuras más grandes y flexibles.

###  Adapter
- **Propósito:** Convierte la interfaz de una clase en otra interfaz que los clientes esperan. El patrón Adapter permite que clases con interfaces incompatibles puedan trabajar juntas.
- **Ejemplo:** Adaptar una API antigua a una nueva interfaz.

###  Bridge
- **Propósito:** Desacopla una abstracción de su implementación de modo que ambas puedan variar independientemente.

###  Composite
- **Propósito:** Compone objetos en estructuras de árbol para representar jerarquías de parte-todo. El patrón Composite permite a los clientes tratar objetos individuales y composiciones de objetos de manera uniforme.
- **Ejemplo:** Árbol de componentes gráficos o archivos/carpetas.

###  Decorator
- **Propósito:** Adjunta responsabilidades adicionales a un objeto de manera dinámica. Los decoradores ofrecen una alternativa flexible a la subclasificación para extender funcionalidades.
- **Ejemplo:** Agregar cifrado o compresión a una transmisión de datos.

###  Facade
- **Propósito:** Proporciona una interfaz unificada a un conjunto de interfaces en un subsistema. La fachada define una interfaz de más alto nivel que hace que el subsistema sea más fácil de usar.
- **Ejemplo:** Un único punto de acceso a un sistema complejo de subsistemas (ej. una librería multimedia).

###  Flyweight
- **Propósito:** Usa el uso compartido (sharing) para soportar de manera eficiente grandes cantidades de objetos de grano fino (fine-grained).

###  Proxy
- **Propósito:** Proporciona un sustituto o representante (placeholder) para otro objeto con el fin de controlar el acceso a este.
- **Ejemplo:** Control de acceso a recursos remotos o pesados (como servidores de video externos).

---

##  3. Patrones de Comportamiento

Estos patrones se enfocan en cómo los objetos interactúan y se comunican entre sí.

###  Observer
- **Propósito:** Define una dependencia de uno a muchos entre objetos, de modo que cuando un objeto cambia de estado, todos sus dependientes son notificados y actualizados automáticamente.
- **Ejemplo:** Suscriptores a cambios de estado (como listeners de eventos).

###  Strategy
- **Propósito:** Define una familia de algoritmos, encapsula cada uno y haz que sean intercambiables. El patrón Estrategia permite que el algoritmo varíe independientemente de los clientes que lo utilicen.
- **Ejemplo:** Algoritmos de ordenamiento intercambiables.

###  Command
- **Propósito:** Encapsula una solicitud como un objeto, lo que permite parametrizar a los clientes con diferentes solicitudes, poner en cola o registrar solicitudes, y soportar operaciones deshacer.
- **Ejemplo:** Comandos de deshacer/rehacer en un editor.

###  State
- **Propósito:** Permite que un objeto altere su comportamiento cuando su estado interno cambia. El objeto parecerá cambiar de clase.
- **Ejemplo:** Máquina de estados para una transacción bancaria.

###  Chain of Responsibility
- **Propósito:** Evita acoplar al remitente de una solicitud con su receptor, permitiendo que más de un objeto tenga la oportunidad de manejar la solicitud. Se encadenan los objetos receptores y se pasa la solicitud a lo largo de la cadena hasta que un objeto la maneje.
- **Ejemplo:** Procesamiento de peticiones HTTP con middleware. Sistema de validaciones encadenadas donde cada validador decide si maneja o pasa la solicitud al siguiente.

###  Mediator
- **Propósito:** Define un objeto que encapsula cómo un conjunto de objetos interactúa. El Mediador promueve un acoplamiento débil al evitar que los objetos se refieran entre sí explícitamente, y permite variar su interacción de manera independiente.
- **Ejemplo:** Chat centralizado entre múltiples usuarios. Un sistema de chat donde los usuarios no se comunican directamente entre sí, sino a través de un servidor central que actúa como mediador.

###  Template Method
- **Propósito:** Define la estructura de un algoritmo en una operación, delegando algunos pasos a las subclases. El Método Plantilla permite que las subclases redefinan ciertos pasos de un algoritmo sin cambiar la estructura del algoritmo.
- **Ejemplo:** Flujo de procesamiento de un documento.

###  Iterator
- **Propósito:** Proporciona una forma de acceder a los elementos de un objeto agregado de manera secuencial sin exponer su representación subyacente.
- **Ejemplo:** Iterador sobre una lista personalizada.

###  Visitor
- **Propósito:** Representa una operación que se debe realizar sobre los elementos de una estructura de objetos. Visitor permite definir una nueva operación sin cambiar las clases de los elementos sobre los que opera.
- **Ejemplo:** Recorrido y operación sobre nodos de un AST (Abstract Syntax Tree o Árbol de Sintaxis Abstracta).

###  Interpreter
- **Propósito:** Dado un lenguaje, define una representación para su gramática junto con un intérprete que utiliza la representación para interpretar oraciones en el lenguaje.

---

##  Conclusión

Cada patrón resuelve un tipo específico de problema de diseño. Conocerlos permite escribir software más limpio, escalable y mantenible.

> Aprender patrones de diseño no es para aplicarlos siempre, sino para reconocer cuándo un problema se parece a uno conocido — y resolverlo de forma eficaz.

## Referencia
Todas las definiciones fueron extraídas de l libro:

> Gamma, E. (1995). Design patterns: elements of reusable object-oriented software. Pearson Education India.

---
<center>TICS 317 - Arquitectura de Sistemas</center>


