class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroes.append([i, j])

        #[1,1], [0, 1]

        for indices in zeroes:
            for j in range(len(matrix[indices[0]])):
                matrix[indices[0]][j]=0
            
            for i in range(len(matrix)):
                matrix[i][indices[1]]=0
        
        

        


                
        
        