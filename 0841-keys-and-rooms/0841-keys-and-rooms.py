class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = {0}
        stack = [0]

        while stack:
            curr = stack.pop()

            for i in rooms[curr]:
                if i not in visit:
                    visit.add(i)
                    stack.append(i)

        return len(visit) == len(rooms)

