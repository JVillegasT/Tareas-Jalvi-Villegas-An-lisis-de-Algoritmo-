# Tareas-Jalvi-Villegas-Analisis-de-Algoritmo-


Lemonade Change

Enlace: https://leetcode.com/problems/lemonade-change/

Criterio greedy: cuando toca dar cambio de $20, conviene usar un billete de $10 más
uno de $5, en lugar de gastar tres de $5. La razón es que el billete de $10 solo
sirve para un caso para dar $15 de vuelta, mientras que el de $5 se puede usar en
cualquier situación, así que conviene guardarlo el mayor tiempo posible. La idea es
ir revisando la fila de clientes una sola vez, sin devolverme a cambiar una decisión
que ya tomé antes.

Complejidad: O(n)

-------------------------------------------------------------

Assign Cookies

Enlace: https://leetcode.com/problems/assign-cookies/description/

Criterio greedy: primero ordeno tanto los niños (g) como las galletas (s) de menor
a mayor. Luego voy recorriendo ambas listas con dos punteros, tratando de darle a
cada niño la galleta más pequeña que le alcance. Así evito gastar una galleta
grande en un niño poco exigente, dejando esa galleta disponible por si más
adelante aparece un niño que sí la necesite.

Complejidad: O(n log n + m log m) 
