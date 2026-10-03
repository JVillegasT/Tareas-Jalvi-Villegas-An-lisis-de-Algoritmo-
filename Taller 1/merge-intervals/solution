class Solution:
    def merge(self, intervalos: List[List[int]]) -> List[List[int]]:

        intervalos.sort(key=lambda x: x[0])

        resultado = []

        for intervalo in intervalos:
            
            if not resultado or resultado[-1][1] < intervalo[0]:
                resultado.append(intervalo)
            else:
               
                resultado[-1][1] = max(resultado[-1][1], intervalo[1])

        return resultado
