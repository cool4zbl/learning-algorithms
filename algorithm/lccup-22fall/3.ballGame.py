from typing import List


def ballGame(num: int, plate: List[str]) -> List[List[int]]:
    matrix = [
        [s for s in row] for row in plate
    ]
    m = len(plate)
    n = len(plate[0])

    # o position
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O':
                positions.append([i, j])

    res = []
    print('O pos', positions)

    for pos in positions:
        i, j = pos
        dirs = ['up', 'down', 'left', 'right']
        count = 0
        for dir in dirs:
            while count < num:
                # while m > i >= 0 and n > j >= 0 and count <= num:
                if dir == 'up':
                    i -= 1
                if dir == 'down':
                    i += 1
                if dir == 'left':
                    j -= 1
                if dir == 'right':
                    j += 1

                cur = matrix[i][j]
                if cur == 'E':
                    dir = 'left'
                if cur == 'W':
                    dir = 'right'
                count += 1
            if [i, j] != [0, 0] or [i, j] != [m-1, 0] or [i, j] != [0, n-1] or [i, j] != [m-1, n-1]:
                res.append([i, j])
            # up = matrix[i - 1][j]
            # down = matrix[i + 1][j]
            # left = matrix[i][j - 1]
            # right = matrix[i][j + 1]

    return res


num = 4
plate = ["..E.", ".EOW", "..W."]
print(ballGame(num, plate))
