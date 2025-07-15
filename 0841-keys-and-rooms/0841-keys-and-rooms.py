class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def find(x):
            if x == parents[x]:
                return parents[x]
            else:
                return find(parents[x])
        
        def union(x, y):
            x = find(x)
            y = find(y)
            
            if x<y:
                parents[y] = x
            else:
                parents[x] = y

        parents = [i for i in range(len(rooms))]

        stack = [0]

        while stack:
            room = stack.pop()

            for key in rooms[room]:
                if find(room) != find(key):
                    union(room, key)
                    stack.append(key)
        
        for i in range(len(rooms)):
            find(i)

        return len(set(parents)) < 2

        