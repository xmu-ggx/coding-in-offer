class Solution:
    def __init__(self, nums):
        self.res = nums
        self.heapfy()
        
    def heap_sort(self):
        while len(self.res) > 0: 
            print(self.res[0])
            self.res[0] = self.res[-1]
            self.res = self.res[:-1]
            self.heapfy()
    
    def heapfy(self):
        n = len(self.res)
        for i in range(n):
            l = 2 * (i+1) - 1
            r = 2 * (i+1)
            if l < n:
                if self.res[l] < self.res[i]:
                    self.res[l], self.res[i] = self.res[i], self.res[l]
            if r < n:
                if self.res[r] < self.res[i]:
                    self.res[r], self.res[i] = self.res[i], self.res[r]

if __name__ == '__main__':
    nums = [1,5,9,3,78,2156,3,4,26,6]
    Solution(nums).heap_sort()
