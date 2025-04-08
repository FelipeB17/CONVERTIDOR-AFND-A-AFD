# Proyecto: Generación de AFD a partir de Expresiones Regulares  
Autores:  
- **Andrés Felipe Beltrán Assaf** - 1152262  
- **Omar Alexis Palencia Claro** - 1152270  

## Descripción del Proyecto

Este programa permite la creación de un Autómata Finito Determinista (AFD), a partir de una expresión regular que representa un lenguaje formal dado un alfabeto. Para lograrlo, se implementa el algoritmo de Thompson para construir un Autómata Finito No Determinista (AFN), seguido de su conversión a AFD.  

El sistema es capaz de procesar expresiones regulares que incluyen las operaciones básicas de unión (`|`), concatenación (`.`) y cierre de Kleene (`*`), con un alfabeto alfanumérico.

---

## Manual de Usuario

### Requisitos
- NetBeans IDE (cualquier versión reciente compatible con Java)
- JDK instalado y configurado

### Ejecución del Programa

1. **Importar Proyecto:**
   - Abrir NetBeans IDE
   - Seleccionar `New Project > With Existing Sources`
   - Importar la carpeta del proyecto

2. **Ubicar Clase Principal:**
   - Navegar al paquete `com.mycompany.main`
   - Abrir la clase `MainAutomata.java`

3. **Ejecutar Programa:**
   - Clic derecho sobre la clase `MainAutomata.java`
   - Seleccionar `Run File...`
   - Confirmar el método principal

4. **Interacción:**
   - El usuario puede ingresar expresiones regulares directamente en consola
   - Para salir del programa, ingresar el comando: `salir`

---

## Reglas y Recomendaciones

- **Escriba la expresión regular manualmente**, sin copiar y pegar de otras fuentes para evitar errores de codificación de caracteres.
- **No deje espacios en la expresión.**
- **Utilice el punto (`.`)** como símbolo de concatenación explícito.
- **Los símbolos permitidos** en el alfabeto pueden ser letras o números.

---

## Operaciones de Thompson Implementadas

- **Símbolo simple:**  
  Convierte cualquier símbolo individual en un AFN básico.

- **Unión (`|`)**  
  Combina dos subexpresiones en paralelo con un nuevo estado inicial y final.

- **Concatenación (`.`)**  
  Conecta dos subexpresiones secuencialmente, uniendo el estado final del primero con el inicial del segundo.

- **Cierre de Kleene (`*`)**  
  Permite que una subexpresión se repita cero o más veces. Se añaden transiciones épsilon para permitir repeticiones o saltar directamente al final.

---

## Ejemplos de Expresiones Regulares desde el Lenguaje

1. **Lenguaje:** { w ∈ Σ\* | w contiene `00` como subcadena }  
   - **Σ = {0, 1}**  
   - **Expresión regular:** `(0|1)*.00.(0|1)*`

2. **Lenguaje:** { w inicia en `a` y termina en `b` }  
   - **Σ = {a, b, c}**  
   - **Expresión regular:** `a.(a|b|c)*.b`

3. **Lenguaje:** { w no contiene más de una `c` }  
   - **Σ = {a, b, c}**  
   - **Expresión regular:** `(a|b)*.c.(a|b)*`

---

## Comando de Salida

- Para salir del programa en cualquier momento, escriba:
