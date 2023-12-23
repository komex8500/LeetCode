class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x = y = 0
        visited.add((x, y))
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False
            
        
        