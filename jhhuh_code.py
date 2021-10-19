"""
0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성하기.

numbers	          result
[1,2,3,4,6,7,8,0]	14
[5,8,4,0,6,7,9]	    6

"""

def solution(numbers):
    return sum(range(1,10)) - sum(numbers)