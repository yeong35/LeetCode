class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def checkSeat(cand1, cand2, cand3):
            if cand1 and cand3:
                return 2
            elif cand1 or cand2 or cand3:
                return 1
            else:
                return 0

        reservedSeats = sorted(reservedSeats)
        cnt = n*2
        curr = reservedSeats[0][0]

        cand1 = True
        cand2 = True
        cand3 = True

        for row, seat in reservedSeats:
            if row != curr:
                cnt -= 2-checkSeat(cand1, cand2, cand3)
                curr = row
                cand1 = True
                cand2 = True
                cand3 = True
            
            if seat >= 2 and seat <=5:
                cand1 = False
            if seat >= 4 and seat <= 7:
                cand2 = False
            if seat >= 6 and seat <= 9:
                cand3 = False
        cnt -= 2-checkSeat(cand1, cand2, cand3)
        return cnt
