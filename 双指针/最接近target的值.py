def search_target(l:list, target:int):
    n = len(l)
    if n < 2:
        return -1

    l.sort()
    left = 0
    right = n - 1

    diff = float("inf")

    while left < right:
        if l[left] + l[right] > target:
            right -= 1
        else:
            diff = min(diff, target-l[left] - l[right])
            left += 1

    if diff == float("inf"):
        return -1

    return target - diff
        