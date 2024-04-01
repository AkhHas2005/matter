#Bank for storing leetcode problem solutions
class Solutions:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:

        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                bad_idx = i

            if num == mink:
                left_idx = i

            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res
        
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k-1)
    
    def at_most(self, nums, k):
        hm = {}
        l = 0
        cnt = 0
        for r in range(len(nums)):
            hm[nums[r]] = hm.get(nums[r], 0) + 1
            while len(hm) > k:
                hm[nums[l]] -= 1
                if hm[nums[l]] == 0:
                    hm.pop(nums[l])
                l += 1
            cnt += r - l + 1
        return cnt
        
    def isGood(self, nums: List[int]) -> bool:
        result = False
        numToCheck = max(nums)
        appMaxNums = nums.count(numToCheck)
        nums.sort()
        if len(nums) - 1 == numToCheck and appMaxNums == 2:
            if len(nums) > 2:
                for i in range(len(nums)-2):
                    if nums[i] == nums[i+1]:
                        result = False
                        break
                    result = True
            else:
                result = True
        else:
            result = False
        return result