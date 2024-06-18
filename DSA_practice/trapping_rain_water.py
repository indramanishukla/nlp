class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        collect = []
        for i in range(1,len(height)-1):
            left_max = 0
            right_max = 0
            for j in range(i, -1, -1):
                if left_max<height[j]:
                    left_max = height[j]
            for k in range(i, len(height)):
                if right_max<height[k]:
                    right_max = height[k]

            water = min(left_max, right_max)-height[i]
            collect.append(water)
        print(collect)   
        return sum(collect)
    
    # optimum solution sudo code

#     int rain_water_trapping(int height[], int n)
# {
#     int trappedWater = 0
#     int left_maxHeight = 0, right_maxHeight = 0
#     int left = 0, right = n - 1
#     while (left <= right)
#     {
#         if (height[left] < height[right])
#         {
#             if (height[left] > left_maxHeight)
#                 left_maxHeight = height[left]
#             else
#                 trappedWater = trappedWater + left_maxHeight 
#                                             - height[left]
#             left = left + 1
#         }
#         else
#         {
#             if (height[right] > right_maxHeight)
#                 right_maxHeight = height[right]
#             else
#                 trappedWater = trappedWater + right_maxHeight 
#                                             - height[right]
#             right = right - 1
#         }
#     }
#     return trappedWater
# }


