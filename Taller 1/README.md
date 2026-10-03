# Taller · Cinco familias en LeetCode

**Curso:** Análisis de Algoritmos 
**Lenguaje:** Python 3  
**Cuenta LeetCode:** `https://leetcode.com/u/X4zdOgml15/`
**Jalvi Villegas**


| # | Problema | Familia | Solución | Evidencia |
| --- | --- | --- | --- | --- |
| 1 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Ordenamiento | [`merge-intervals/solution.py`](merge-intervals/solution.py) | [evidencia](evidencias/merge-intervals-accepted.png) |
| 2 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Grafos | [`number-of-islands/solution.py`](number-of-islands/solution.py) | [evidencia](evidencias/number-of-islands-accepted.png) |
| 3 | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Programación dinámica | [`longest-common-subsequence/solution.py`](longest-common-subsequence/solution.py) | [evidencia](evidencias/longest-common-subsequence-accepted.png) |
| 4 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Greedy | [`non-overlapping-intervals/solution.py`](non-overlapping-intervals/solution.py) | [evidencia](evidencias/non-overlapping-intervals-accepted.png) |
| 5 | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Backtracking | [`combination-sum/solution.py`](combination-sum/solution.py) | [evidencia](evidencias/combination-sum-accepted.png) |

---

## 1 · [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

**Familia:** ordenamiento  
**Idea:** la entrada no viene ordenada, así que primero se elige la **clave** (el `start`) y se ordenan los intervalos con `O(n log n)`. Después una sola pasada de izquierda a derecha mantiene el intervalo abierto actual: si el siguiente empieza antes o justo cuando termina el actual (`start ≤ end_actual`), se ensancha el `end` con `max`; si no, se cierra el actual y se abre otro. Es como el *merge* de dos corridas, pero sobre una sola corrida ya ordenada.

**Complejidad** (`n` = número de intervalos):

- Tiempo: **`O(n log n)`** — domina el sort. la pasada de fusión es `O(n)`.
- Espacio: **`O(n)`** para la salida (más lo que pida el sort).


---

## 2 · [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

**Familia:** grafos  
**Modelo:** el grafo está **implícito** en la grilla y es **no dirigido**: cada celda `'1'` es un **vértice**, hay **arista** entre dos celdas `'1'` vecinas arriba/abajo/izquierda/derecha (la diagonal no es vecina; las celdas `'0'` no son vértices). Una isla es una **componente conexa**, así que contar islas es contar componentes.  
**Idea:** recorrer las celdas; cada vez que aparece un `'1'` no visitado se suma una isla y se lanza un **DFS** que marca (hunde) toda la componente convirtiéndola en `'0'` para no volver a contarla.

**Complejidad** (`m` filas, `n` columnas):

- Tiempo: **`Θ(m·n)`** — cada celda se visita una sola vez.
- Espacio: **`O(m·n)`** en el peor caso (pila de recursión con toda la grilla en tierra).

---

## 3 · [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

**Familia:** programación dinámica
**Idea**  estado, recurrencia y base

- **Estado:** `dp[i][j]` = longitud del LCS de `text1[0..i)` y `text2[0..j)`.
- **Base:** `dp[0][j] = dp[i][0] = 0` (un prefijo vacío no tiene LCS).
- **Recurrencia:** si `text1[i-1] == text2[j-1]`, `dp[i][j] = 1 + dp[i-1][j-1]`; si no, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Como la fila `i` solo depende de la fila `i-1` y de la posición ya calculada de la fila actual, la tabla se comprime a **dos filas**.

**Complejidad** (`n = len(text1)`, `m = len(text2)`):

- Tiempo: **`Θ(n·m)`** — se llena toda la tabla.
- Espacio: **`Θ(min(n, m))`** con dos filas (`Θ(n·m)` sin comprimir).

---

## 4 · [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

**Familia:** greedy 
**Criterio greedy:** entre los intervalos que aún caben, quedarse con el que **termina antes**. Se ordenan los candidatos por `end`; se recorre y se acepta el siguiente cuyo `start ≥ end` del último aceptado (si uno empieza justo cuando el otro termina, **no** se solapan). Los que no se eligen son los que se «borran»: la respuesta es `n − (cuántos se quedaron)`. Maximizar cuántos caben sin solape es lo mismo que minimizar cuántos se tiran.

**Complejidad** (`n` = número de intervalos):

- Tiempo: **`O(n log n)`** — domina el sort; la pasada es `O(n)`.
- Espacio: **`O(1)`** extra si el sort es in-place (`O(n)` si el lenguaje copia).

---

## 5 · [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

**Familia:** backtracking  
**Qué se elige:** el candidato `candidates[i]`, que se puede **reutilizar** (el siguiente llamado sigue en el mismo `i`); para no repetir permutaciones no se vuelve a índices menores. **Qué se deshace:** al regresar, `path.pop()` quita el último elegido — eso es el *backtrack*. Si la suma iguala `target` se copia la combinación a la respuesta; si la supera, se corta la rama (**poda**).

**Complejidad** (`n = len(candidates)`, `t = target`, `mn = min(candidates)`):

- Tiempo: **`O(n^(t/mn))`** — exponencial en la profundidad: el peor caso es un árbol de profundidad `t/mn` donde cada nivel prueba los candidatos (hay que **enumerar** todas las combinaciones de la salida; un DP que solo cuenta, como Coin Change, no sustituye la lista).
- Espacio: **`O(t/mn)`** para la pila de recursión y la combinación actual, más lo que ocupe la salida.

