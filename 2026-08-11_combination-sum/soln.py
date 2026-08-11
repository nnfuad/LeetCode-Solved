class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sorting enables early termination when sum exceeds target
        res = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                # Since candidates are sorted, break early if current candidate exceeds remaining
                if candidates[i] > remaining:
                    break
                # Include candidates[i] in current combination
                path.append(candidates[i])
                # Recurse with the same index to allow reuse
                backtrack(i, path, remaining - candidates[i])
                # Backtrack: remove the last added candidate
                path.pop()
        
        backtrack(0, [], target)
        return res