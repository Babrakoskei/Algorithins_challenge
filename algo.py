# - Given an integer array `arr`, count how many elements `x` there are, such that `x+1` is also in `arr`.
# If there are duplicates in `arr`, count them separately.
# > Example 1:
#     Input: arr = [1,2,3]
#     Output: 2
#     Explanation:  There are 2 such elements: 1 and 2 because 2 and 3 are also in the array

# I took two aprroaches in finding a solution to this problem

#1 ST APPROACH
def checkArr(arr):
  newArr=[i+1 for i in arr]
  while newArr != []:
    poppedItem = newArr.pop()
    if poppedItem in arr:
        lastArr=[]
        lastArr.append(poppedItem)
        print(len(lastArr))
checkArr([1,2,3,4])

# 2ND APPROACH
def checkArr(arr):
  count = 0
  for i in arr:
    if i+1 not in arr:
      pass
    else:
      count+=1
  print(count)
checkArr([1,2,3,4,1,2])