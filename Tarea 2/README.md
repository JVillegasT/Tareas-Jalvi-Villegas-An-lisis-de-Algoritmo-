Tarea 2 - Algoritmos de Ordenamiento


JVillegasT
Lenguaje: Python

--
 Ejercicio 1: 88. Merge Sorted Array


[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)


Para resolver este problema utilicé el algoritmo de fusión de dos arreglos previamente ordenados.

La solución compara los elementos de `nums1` y `nums2` desde el final. Esto permite colocar los valores más grandes en las últimas posiciones disponibles de `nums1` sin sobrescribir elementos que todavía deben ser comparados.


Este proceso continúa hasta fusionar los elementos de ambos arreglos.

--Complejidad

 O(m + n)

Donde:

-`m` representa la cantidad de elementos válidos de `nums1`.
-`n` representa la cantidad de elementos de `nums2`.


-Evidencia de Accepted

![Accepted - Merge Sorted Array](Tareas-Jalvi-Villegas-An-lisis-de-Algoritmo-/Tarea 2
/Evidencia)

-----------------------------------------

 Ejercicio 2: 75. Sort Colors


[75. Sort Colors](https://leetcode.com/problems/sort-colors/)


Para resolver este problema utilicé el algoritmo conocido como Bandera Holandesa, el cual permite ordenar un arreglo que únicamente contiene los valores `0`, `1` y `2`.


Inicialmente, `j` e `i` comienzan en la primera posición del arreglo, mientras que `k` comienza en la última posición.

Durante el recorrido se presentan tres casos:

- Cuando `nums[i] == 0`

El valor `0` se intercambia con el elemento ubicado en la posición `j`. Posteriormente, se incrementan tanto `j` como `i`.


-Cuando `nums[i] == 1`

El valor `1` ya pertenece a la zona central, por lo tanto, únicamente se avanza el índice `i`.


-Cuando `nums[i] == 2`

El valor `2` se intercambia con el elemento ubicado en la posición `k`. Después, se disminuye `k`.


En este caso, el índice `i` no aumenta inmediatamente porque el nuevo valor que llega desde la posición `k` debe ser analizado.

--Complejidad
 `O(n)`.
 `O(1)`.

Donde `n` representa la cantidad de elementos del arreglo.


- Evidencia de Accepted

![Accepted - Sort Colors](Tareas-Jalvi-Villegas-An-lisis-de-Algoritmo-/Tarea 2
/Evidencia)

