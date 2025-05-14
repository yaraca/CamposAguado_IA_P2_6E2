# Inteligencia Artificial - Campos Aguado - P2 6E2

Este repositorio contiene la implementación de diversos algoritmos fundamentales en **Inteligencia Artificial**, organizados según **tres grandes enfoques** de razonamiento y aprendizaje:

---

## Enfoques Principales

### 1. Enfoque de Grafos
El enfoque de grafos representa problemas como un conjunto de nodos (estados) conectados por aristas (transiciones). Se utiliza en:
- **Búsqueda de caminos óptimos**
- **Planificación de rutas**
- **Juegos y resolución de acertijos**

**Ejemplos de algoritmos:**
- **Búsqueda en amplitud (BFS):** Explora todos los vecinos antes de profundizar. Útil en laberintos, redes sociales o juegos.
- **Búsqueda en profundidad (DFS):** Explora caminos hasta el final antes de retroceder. Aplicado en rompecabezas o análisis de conectividad.
- **Búsqueda A* (A-Star):** Encuentra la ruta más corta usando una heurística. Ideal para navegación y mapas.
- **Algoritmos genéticos en grafos:** Simulan evolución para encontrar soluciones óptimas en rutas, horarios, etc.

---

### 2. Enfoque de Probabilidad
Utiliza modelos probabilísticos para razonar bajo incertidumbre. Es esencial en tareas donde la información es incompleta o ambigua.

**Aplicaciones:**
- Diagnóstico médico
- Reconocimiento de voz
- Predicciones con incertidumbre

**Ejemplos de algoritmos:**
- **Razonamiento probabilístico:** Usa reglas de probabilidad para inferir conclusiones.
- **Redes Bayesianas:** Representan dependencias causales entre variables. Usado en diagnóstico médico o predicción.
- **Reconocimiento del habla con HMM:** Modela secuencias temporales con incertidumbre.
- **Aprendizaje probabilístico:** Ajusta modelos en base a datos con ruido para hacer predicciones más confiables.

---

### 3. Enfoque de Lógica
Se basa en representar el conocimiento mediante proposiciones, reglas y relaciones lógicas. Permite:
- Inferencia automática
- Toma de decisiones simbólicas
- Representación estructurada del conocimiento

**Ejemplos de algoritmos:**
- **Ontologías y taxonomías:** Organizan conceptos jerárquicamente. Se usan en conocimiento general y clasificación.
- **Redes semánticas:** Relacionan conceptos con aristas. Útiles en procesamiento de lenguaje natural.
- **Razonamiento por defecto:** Permite hacer suposiciones si no se tienen todos los datos.
- **Aprendizaje inductivo (ID3, Boosting, K-DT, etc.):** Aprende reglas o árboles a partir de ejemplos. Se aplica en clasificación y predicción.

---

## Librerías Utilizadas

A continuación se describen las librerías utilizadas y su propósito en los algoritmos implementados:

| **Librería**       |                                  **Propósito**                                                   |
|--------------------|--------------------------------------------------------------------------------------------------|
| `numpy`            | Permite operar con vectores y matrices de forma eficiente. Útil para cálculos matemáticos.       |
| `pandas`           | Manejo de datos en forma de tablas (DataFrames). Ideal para cargar, explorar y transformar datos.|
| `sklearn`          | Conjunto de algoritmos de aprendizaje automático (ID3, Boosting, etc.).                          |
| `math`             | Funciones matemáticas básicas (logaritmos, raíces, etc.).                                        |
| `networkx`         | Creación y visualización de grafos.                                                              |
| `collections`      | Estructuras como `deque`, usadas para colas o pilas.                                             |
| `heapq`            | Implementa colas de prioridad para obtener el siguiente nodo más prometedor (como en A*).        |
| `random`           | Generación de números aleatorios (usado en algoritmos genéticos).                                |
| `copy`             | Permite copiar objetos complejos (listas de listas, diccionarios anidados, etc.).                |
| `itertools`        | Herramientas para manejar combinaciones, permutaciones, etc.            |

---