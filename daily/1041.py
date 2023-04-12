class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, direction = 0, 0, 0
        for _ in range(4):
            for char in instructions:
                if char == "G":
                    if direction == 0:
                        y += 1
                    elif direction == 1:
                        x += 1
                    elif direction == 2:
                        y -= 1
                    elif direction == 3:
                        x -= 1
                elif char == "R":
                    if direction == 0:
                        direction = 1
                    elif direction == 1:
                        direction = 2
                    elif direction == 2:
                        direction = 3
                    elif direction == 3:
                        direction = 0
                elif char == "L":
                    if direction == 0:
                        direction = 3
                    elif direction == 1:
                        direction = 0
                    elif direction == 2:
                        direction = 1
                    elif direction == 3:
                        direction = 2
            if x == 0 and y == 0:
                return True
        return False
        # x_pos, y_pos, d = 0, 0, 0
        # for _ in range(4):
        #     if d == 0:
        #         x_pos += x
        #         y_pos += y
        #         d = (d + direction) % 4


    def advanced(self, instructions: str) -> bool:
        d = 0
        pos = [0] * 4
        for c in instructions:
            if c == 'L':
                d = (d + 1) % 4
            elif c == 'R':
                d = (d + 3) % 4
            else:
                pos[d] += 1
        return True if pos[0] == pos[2] and pos[1] == pos[3] else False


if __name__ == '__main__':
    z = "GLRLLGLL"
    so = Solution()
    print(so.isRobotBounded(z))
