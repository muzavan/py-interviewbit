# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def merge(self, intervals):
        ins = intervals
        # ins = sorted(intervals, key=lambda x : x.start)
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
  
    def insert(self, intervals, new_interval):
        if len(intervals) == 0:
            return [new_interval]
            
        if new_interval.start < intervals[0].start:
            return self.merge([new_interval] + intervals)
        elif new_interval.start > intervals[-1].start:
            return self.merge(intervals + [new_interval])
        
        
        result = []
        for i in range(len(intervals)):
            it = intervals[i]
            if max(it.start, new_interval.start) > min(it.end, new_interval.end):
                if it.start > new_interval.start:
                    result.append(new_interval)
                result.append(it)
                continue
            else:
                if it.start < new_interval.start:
                    result.extend(self.merge([it, new_interval] + intervals[i+1:]))
                else:
                    result.extend(self.merge([new_interval, it] + intervals[i+1:]))
                break
            
            
            
        
        return result
            
               
                
        
        
                
            
