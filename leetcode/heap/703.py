class KthLargest:

    def __init__(self, k , nums):
        self.k = k
        self.n = len(nums)
        if self.n <= self.k:
            self.res = nums
            self.heapfy()
        else:
            self.res = nums[:k]
            self.heapfy()
            for i in range(self.k,self.n):
                if nums[i] > self.res[0]:
                    self.res[0] = nums[i]
                    self.heapfy()
        
    def add(self, val: int) -> int:
        if self.n < self.k:
            self.res.append(val)
            self.n += 1
            self.heapfy()
            if self.n == self.k:
                return self.res[0]
        else:
            if val > self.res[0]:
                self.res[0] = val
                self.heapfy()
                return self.res[0]
            else:
                return self.res[0]
            
    
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
