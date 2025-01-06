class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []

        for interval in intervals:

            # empty
            if len(result)==0:
                result.append(interval)
            # check
            else:
                start, end = interval
                peek_s, peek_e = result[-1]

                if peek_s <= start <= peek_e:
                    if end > peek_e:
                        peek_e = end
                        result[-1] = [peek_s, peek_e]
                else:
                    result.append(interval)
            

        return result