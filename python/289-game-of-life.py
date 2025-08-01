from collections import Counter


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def get_neighbors_values(i, j):
            neighbors_coordinates = []
            neighbors_coordinates.append((i - 1, j - 1))
            neighbors_coordinates.append((i, j - 1))
            neighbors_coordinates.append((i + 1, j - 1))
            neighbors_coordinates.append((i - 1, j))
            neighbors_coordinates.append((i + 1, j))
            neighbors_coordinates.append((i - 1, j + 1))
            neighbors_coordinates.append((i, j + 1))
            neighbors_coordinates.append((i + 1, j + 1))
            filtered = filter(
                lambda pair: pair[0] >= 0
                and pair[0] < m
                and pair[1] >= 0
                and pair[1] < n,
                neighbors_coordinates,
            )
            valid = list(filtered)
            neighbor_values = []
            for coordinate in valid:
                i, j = coordinate
                neighbor_values.append(board[i][j])
            return neighbor_values

        def compute_cell(cell_value, neighbors_values):
            counts = Counter(neighbors_values)
            if cell_value == 1:
                if counts[1] < 2:
                    return 0
                if counts[1] > 3:
                    return 0
                return 1
            if counts[1] == 3:
                return 1
            return 0

        def gen_morph_dict():
            res = {}
            for i in range(m):
                for j in range(n):
                    key = f"{i}#{j}"
                    neighbors_values = get_neighbors_values(i, j)
                    cell_value = board[i][j]
                    res[key] = compute_cell(cell_value, neighbors_values)
            return res

        morph_dict = gen_morph_dict()
        for pair in morph_dict.items():
            key, value = pair
            i, j = key.split("#")
            board[int(i)][int(j)] = value
        print(board)


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
s = Solution()
s.gameOfLife(board)

# Algo
# Create a function that given a cell returns all the values of the neighbors
# use that function to  make a dictionary that has the coordinate as a key
# and the value + neighbors as a value
# For each coordinate compute the result value based on the conditions of the game
# For each coordinate update the value with the computed value
