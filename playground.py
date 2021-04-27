from copy import deepcopy
import math
class Solution:
    def imageSmoother(self, M: list[list[int]]) -> list[list[int]]:
        result = deepcopy(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                #print(j)
                divby = 1
                value = M[i][j]
                if i > 0:
                    #top
                    value += M[i-1][j]
                    divby += 1
                if j > 0:
                    #left
                    value += M[i][j-1]
                    divby += 1
                if j < len(M[0])-1:
                    #right
                    value += M[i][j+1]
                    divby += 1
                if i < len(M)-1:
                    #bottom
                    value += M[i+1][j] 
                    divby += 1
                if j > 0 and i > 0:
                    #top left
                    value += M[i-1][j-1]
                    divby += 1
                if i > 0 and j < len(M[0])-1:
                    #top right
                    value += M[i-1][j+1]
                    divby += 1
                if i < len(M)-1 and j > 0:
                    #bottom left
                    value += M[i+1][j-1]
                    divby += 1
                if i < len(M)-1 and j < len(M[0])-1:
                    #bottom right
                    value += M[i+1][j+1]
                    divby += 1
                #print(i, j, value, divby)
                result[i][j] = math.floor(value/divby)
        return result
                
                
                
run = Solution()
result = run.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
print(result)