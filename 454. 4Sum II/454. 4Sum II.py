class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        comp = {}
        count = 0
        for num in nums1:
            for num1 in nums2:
                t = num + num1
                comp[t] = comp.get(t, 0) + 1

        for num in nums3:
            for num1 in nums4:
                t = -(num + num1)
                count = count + comp.get(-(num + num1), 0)

        return count