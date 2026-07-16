class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Trick: flip over the horizontal and then transpose over the topL -> bottomR diagonal
        # Step 1:
        # 7 8 9
        # 4 5 6
        # 1 2 3

        # Step 2:
        # 7 4 1
        # 8 5 2
        # 9 6 3

        for row in range(len(matrix) // 2):
            matrix[row], matrix[len(matrix)-row-1] = matrix[len(matrix)-row-1], matrix[row]

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        