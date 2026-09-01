from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n = len(classroom), len(classroom[0])

        litCount, start_pos = 0, tuple()

        grid = []

        for i, row in enumerate(classroom):
            r = list(row)

            for j, x in enumerate(r):

                if x == 'L':
                    r[j] = "L" + str(litCount)
                    litCount += 1

                elif x == 'S':
                    start_pos = (i, j)

            grid.append(r)

        if litCount == 0:
            return 0

        fullMask = (1 << litCount) - 1

        queue = deque()

        bst_erg = [
            [
                [-1 for _ in range(2 ** litCount)]
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        queue.append(
            (start_pos[0], start_pos[1], 0, energy, 0)
        )

        bst_erg[start_pos[0]][start_pos[1]][0] = energy

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while queue:

            row, col, mask, curr_erg, moves = queue.popleft()

            for di, dj in directions:

                nr, nc = row + di, col + dj

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                curr_chr = grid[nr][nc]

                if curr_chr == "X":
                    continue

                new_erg = curr_erg - 1

                if new_erg < 0:
                    continue

                newMask = mask

                if curr_chr == "R":
                    new_erg = energy

                if curr_chr.startswith("L"):
                    bit = int(curr_chr[-1])
                    newMask = mask | (1 << bit)

                if newMask == fullMask:
                    return moves + 1

                if new_erg <= bst_erg[nr][nc][newMask]:
                    continue

                bst_erg[nr][nc][newMask] = new_erg

                queue.append(
                    (nr, nc, newMask, new_erg, moves + 1)
                )

        return -1