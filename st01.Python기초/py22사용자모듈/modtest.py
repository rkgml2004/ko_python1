# modtest.py
# 모듈 import 테스트

# import 모듈이름
import mod
print("mod.add(3,4) = ", mod.add(3, 4))

# from 모듈이름 import 모듈함수
from mod import sum

print("sum(3,4)            = ", sum(3,4))