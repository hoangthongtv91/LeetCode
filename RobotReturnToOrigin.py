class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for i in moves:
            if i == "L":
                x -= 1
            elif i == "R":
                x += 1
            elif i == "U":
                y += 1
            else:
                y -= 1

        if x == 0 and y == 0:
            return True
        else:
            return False