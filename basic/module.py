# 모듈
# 함수, 변수, 클래스를 모아 놓은 파이썬 파일

# math 모듈 전체 import
# import math 
# import sys

# print(math.sqrt(16))
# print(math.sin(2))
# print(sys.builtin_module_names)

# math 모듈에서 사용할 함수만 가져오기
from math import sin, cos, floor, ceil
print(sin(1))
print(cos(1))
print(floor(1.5))
print(ceil(1.6))

from random import random, uniform, randrange, choice, shuffle, sample

print(random()) # 0 < random() <= 1
print(uniform(10, 20))  # 10 ~ 20 사이의 float 로 리턴
print(randrange(10, 20))
print(choice([1, 2, 3, 4, 5, 6, 7, 8]))
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(list1)
print(list1)
print(sample(list1, 2))


# from prt import prt1

# prt1()

# import sum1

# print(sum1.add(6, 7))

# number = sum1.number_input()

# print("둘레", sum1.get_circ(number))
# print("면적", sum1.get_area(number))

from calc import Calc

# calc = calc.Calc(5, 3)
calc = Calc(6, 5)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())
