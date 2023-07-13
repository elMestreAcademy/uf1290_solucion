# MF965_3 - UF1290

## Práctica

**Lenguaje**: Python
**Plataforma**: GitHub

*Nota:* Debe realizar como mínimo un commit para cada pregunta (exceptuando la 1ª)

### **Pregunta 1** *(20 minutos)*

---
1.1 Clonar el repositorio proporcionado: `https://github.com/elMestreAcademy/uf1290_NOMBRE_DE_USUARIO_GITHUB`. Asegúrate de reemplazar `NOMBRE_DE_USUARIO_GITHUB` con tu nombre de usuario de GitHub.

### **Pregunta 2** *(30 minutos)*

---
2.1 Crear un script Python llamado `componente.py` que defina una clase `Componente`. Esta clase deberá tener las siguientes propiedades:

- `nombre` (string)
- `version` (float)
- `fecha_creacion` (datetime)

La clase debe tener un constructor que acepte y establezca estos valores.

2.2 Agregue métodos para obtener y establecer cada una de las propiedades.

2.3 Crear un método `__str__` para imprimir los detalles del componente en el formato: `nombre (version) - fecha de creación`.

### **Pregunta 3** *(30 minutos)*

---
3.1 Crear una segunda clase Python en el mismo script llamada `Sistema`. Esta clase deberá tener las siguientes propiedades:

- `nombre` (string)
- `componentes` (lista de objetos `Componente`)

3.2 El constructor de la clase `Sistema` deberá aceptar y establecer el nombre, pero la lista de componentes deberá ser inicializada como vacía.

3.3 Crear un método `añadir_componente` que tome un objeto `Componente` y lo añada a la lista de componentes.

3.4 Crear un método `obtener_componentes` que devuelva la lista de componentes.

3.5 Crear un método `__str__` que imprima los detalles del sistema y sus componentes en el formato: `nombre - [componente1, componente2,...]`.

### **Pregunta 4** *(30 minutos)*

---
4.1 Crear un script Python llamado `main.py` que importe las clases `Componente` y `Sistema` de `componente.py`.

4.2 Crear al menos dos objetos `Componente` con distintos nombres, versiones y fechas de creación.

4.3 Crear un objeto `Sistema` e insertar los dos componentes creados en el paso anterior utilizando el método `añadir_componente`.

4.4 Imprimir los detalles del sistema y sus componentes utilizando el método `__str__`.
