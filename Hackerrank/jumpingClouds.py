def JumpingOnClouds(arr):
    curr = 0
    step = -1
    stop = len(arr)
    while curr < stop:
        if curr + 2 < stop and arr[curr + 2] == 0:
            curr = curr + 2
        else:
            curr = curr + 1
        step += 1
    return step


size = int(input())
clouds = [int(i) for i in input().split()]
print(JumpingOnClouds(clouds))

