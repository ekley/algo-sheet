def container_with_max_water(heights):
    max_water = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        width = right - left
        area = min(heights[left], heights[right]) * width
        max_water = max(max_water, area)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
        
    return max_water
        

          
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = container_with_max_water(heights); # 49
print(result)