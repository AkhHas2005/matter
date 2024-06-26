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

    def isSymmetric(self, root):
        # Special case...
        if not root:
            return true;
        # Return the function recursively...
        return self.isSame(root.left, root.right)
        
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)

    def countDigits(self, num: int) -> int:
        stringNum = str(num)
        digitsCount = 0
        for char in stringNum:
            digit = int(char)
            if num % digit == 0:
                digitsCount += 1
        return digitsCount

     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        LIS = []
        size = 0
        for (w, h) in envelopes:
            if not LIS or h > LIS[-1]:
                LIS.append(h)
                size += 1
            else:
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if LIS[m] < h:
                        l = m + 1
                    else:
                        r = m
                LIS[l] = h
        return size

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        prefix = [0, arr[0]]

        for i in range(1, len(arr)): 
            prefix.append(prefix[i] ^ arr[i])

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        h2l = defaultdict(list)
        for l, h in rectangles:
            h2l[h].append(l)
        cnt = [0] * len(points)
        for i, xy in enumerate(points):
            x, y = xy
            for h in range(y, 101):
                cnt[i] += len(h2l[h]) - bisect_left(h2l[h], x)
        return cnt

        for left, right in queries: 
            ans.append(prefix[left] ^ prefix[right + 1])

        return ans
