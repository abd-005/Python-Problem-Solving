n = int(input())
arr = list(map(int, input().split()))

unique_arr = list(set(arr))
unique_arr.sort(reverse=True)
print(unique_arr[1])


###
# Diff Approach
# i = n - 1
# newArr = []
# while i >= 0:
#     if (arr[i-1] != arr[i]):
#         newArr.append(arr[i])
#     i = i - 1
# print(newArr[1])

###
