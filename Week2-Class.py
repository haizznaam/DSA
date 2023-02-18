def binom_search(A: list, n: int):
    start = 0 
    end = len(A)-1
    while(start <= end):
        mid = (start + end) // 2
        if A[mid] == num:
            return mid
        elif A[mid] > num:
            end = mid - 1
        else:
            end = mid + 1
    return -1


alist = [1,3,5,6,7,9]
num = 5
print(binom_search(alist,num))
