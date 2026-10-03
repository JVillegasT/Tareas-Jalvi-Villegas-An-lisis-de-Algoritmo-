class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int, resto: int) -> None:
            if resto == 0:                    
                result.append(path.copy())
                return
            if resto < 0:                       
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])     
                backtrack(i, resto - candidates[i]) 
                path.pop()                     

        backtrack(0, target)
        return result
