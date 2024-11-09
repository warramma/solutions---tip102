lst = [2,3,4,5,6,9]
def binary_search(target, lst):
   low = 0
   high = len(lst) - 1
   while low <= high:
      mid = (low + high) // 2
      if target == lst[mid]:
         return mid
      elif target <= lst[mid]:
         high = mid - 1
      else:
         low = mid + 1
   return -1

print(binary_search(3, lst))
print(binary_search(8, lst))