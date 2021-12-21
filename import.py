"""
import 는 c언에서 include 와 비슷하다
import math 를 써도 되고
math의 fsum 기능만 쓰고 싶으면
from math import fsum 을 쓰고 사용하면 된다.
"""
from math import fsum as sexy_sum

print(sexy_sum([1, 2, 3, 4, 5, 6, 7]))
