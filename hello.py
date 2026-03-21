# task 1
from ctypes.wintypes import HRESULT


def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=' ')
print_1_to_n(5)
# task 2
def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=' ')
    print_n_to_1(n - 1)
print_n_to_1(5)
#task 3
def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)
print(sum_n(5))
#task 4
def fac_n(n):
    if n==0:
        return 1
    return n*fac_n(n-1)
print(fac_n(5))
#task 5
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,3))
#task 6
def sum_digits(n):
    if n<10:
        return n
    return n%10+sum_digits(n//10)
print(sum_digits(572))
#task 7
def count_digits(n):
    if n<10:
        return 1
    return 1+count_digits(n//10)
print(count_digits(572))
#task 8
def reverse_number(n,result=0):
    if n==0:
        return result
    return reverse_number(n//10,result*10+n%10)
print(reverse_number(1234))
#task 9;
def fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
#task 10
# task 10
def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print("Palindrome" if is_palindrome("level") else "Not palindrome")  # Palindrome
print("Palindrome" if is_palindrome("hello") else "Not palindrome")  # Not palindrome
#task 11
def sum_array(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i]+sum_array(arr,i + 1)
print(sum_array([3,5,2,7]))
#task 12
def max_array(arr,i=0):
    if i == len(arr)-1:
        return arr[i]
    return max(arr[i], max_array(arr,i+1))
print(max_array([4,9,1,7,3]))
#task 13
def count_occurrences(arr, target, i=0):
    if i == len(arr):
        return 0
    match=1 if arr[i] == target else 0
    return match+count_occurrences(arr,target,i+1)
print(count_occurrences([1,2,3,2,2,5],2))
#task 14
def linear_search(arr,target,i=0):
    if i == len(arr):
        return False
    if arr[i] == target:
        return True
    return linear_search(arr,target,i+1)
print("Found" if linear_search([4,7,1,9,3],9)else "Not found")
#task 15
def is_sorted(arr,i=0):
    if i>=len(arr)-1:
        return True
    if arr[i]>arr[i+1]:
        return False
    return is_sorted(arr,i+1)
print("Sorted" if is_sorted([1,2,4,7,9])else "Not sorted")
print("Sorted" if is_sorted([1,5,3,8])else "Not sorted")



