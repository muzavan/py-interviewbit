# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        ins = sorted(intervals, key=lambda x : x.start)
        # print([(i.start, i.end) for i in ins])
        result = []
        
        while len(ins) > 0:
            # print([(i.start, i.end) for i in result])
            nxt = ins.pop(0)
            if len(result) > 0:
                cur = result.pop(-1)
                
                if max(cur.start, nxt.start) <= min(cur.end, nxt.end):
                    result.append(Interval(min(cur.start, nxt.start), max(cur.end, nxt.end)))
                else:
                    result.append(cur)
                    result.append(nxt)
                    
            else:
                result.append(nxt)
                
        return result
                
        
