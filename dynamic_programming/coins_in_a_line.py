from pprint import pprint
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        cache = {}
        board = A[:]
        
        score = get_best_score(board, 0, len(board)-1,cache, sum(board))
        return score

def get_cache_key(board):
    return ','.join(map(str, board))
    
def get_best_score(board, st, en, cache, allSum):
    if st == en:
        return allSum
    
    cache_key = get_cache_key([st, en])
    if cache_key in cache:
        return cache[cache_key]
        
    bestScore = allSum - min(get_best_score(board, st+1, en, cache, allSum - board[st]), get_best_score(board, st, en-1, cache, allSum - board[en]))
    
    cache[cache_key] = bestScore    
    return bestScore
