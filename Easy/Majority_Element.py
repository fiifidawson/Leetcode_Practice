"""
The idea behind this algorithm is that the majority element in a list appears more than n / 2 times, 
where n is the length of the list. Therefore, if the input list is sorted, the majority element
will always be at the middle position (index n), regardless of the specific values of the elements in the list.
"""


# class Solution:
#     def majorityElement(self, nums) -> int:
#         nums.sort()
#         n = int(len(nums) / 2)
#         return nums[n]
    

class Solution:
    def majorityElement(self, nums) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res
    

if __name__ == "__main__":
    nums = [2,2,1,1,1,3,3]
    print(Solution().majorityElement(nums))