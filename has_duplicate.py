def has_duplicate(nums):
    seen = set()

    for i, num in enumerate(nums):
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

