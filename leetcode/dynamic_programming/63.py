class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0,m):
            if obstacleGrid[i][0] == 1:
                for _ in range(i,m):
                    dp[_][0] = 0
                break
            else:
                dp[i][0] = 1
                
        for j in range(0,n):
            if obstacleGrid[0][j] == 1:
                for _ in range(j,n):
                    dp[0][_] = 0
                break
            else:
                dp[0][j] = 1
            

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
