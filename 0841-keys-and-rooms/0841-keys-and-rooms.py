class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()

        stack = [0]
        visit.add(0)

        while stack:
            curr = stack.pop()

            for key in rooms[curr]:
                if key not in visit:
                    stack.append(key)
                    visit.add(key)

        return len(visit) == len(rooms)