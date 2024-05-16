from typing import List 

def combinationSum(candidates: List[int], target: int) -> List[List[int]]: 
    res = []

    def dfs(i, cur, total):
        if total == target: 
            res.append(cur.copy())
            return
        
        if i >= len(candidates) or total > target:
            return
        
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


candidates = [2,3,6,7] ; target=7
print(combinationSum(candidates, target))
