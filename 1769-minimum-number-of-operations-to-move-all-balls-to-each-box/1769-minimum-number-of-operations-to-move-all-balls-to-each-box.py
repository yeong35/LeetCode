class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer= [0] * len(boxes)

        count = 0
        balls = 0

        for i in range(len(boxes)):
            answer[i] += count

            if boxes[i] == '1':
                balls+=1

            count += balls


        balls = 0
        count = 0

        for i in range(len(boxes)):
            answer[len(boxes)-i-1] += count

            if boxes[len(boxes)-i-1] == '1':
                balls+=1

            count += balls


            
            

        print(answer)

        return answer
