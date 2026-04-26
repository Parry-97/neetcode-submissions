class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products: List[int] = []
        right_products: List[int] = []

        left_max = nums[0]
        left_products.append(left_max)
        for i in range(1, len(nums)):
            left_max *= nums[i]
            left_products.append(left_max)

        right_max = nums[-1]
        right_products.append(right_max)
        for i in range(len(nums) - 2, -1, -1):
            right_max *= nums[i]
            right_products.append(right_max)

        right_products.reverse()

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(right_products[i + 1])
            elif i == len(nums) - 1:
                result.append(left_products[i - 1])
            else:
                result.append(left_products[i - 1] * right_products[i + 1])
        return result



        