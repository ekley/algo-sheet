def trapped_water(height):
    water = 0
    left = 0
    right = len(height) - 1

    max_left = height[left]
    max_right = height[right]

    while left < right:
        if height[left] <= height[right]:
            if height[left] < max_left:
                water += max_left - height[left]
            else:
                max_left = height[left]
            left += 1

        else:
            if height[right] < max_right:
                water += max_right - height[right]
            else:
                max_right = height[right]
            right -=1
    return water

