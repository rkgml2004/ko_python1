#################################
# time 모듈의 사용법을 익힌다.
#
# time.sleep(초)	동작 중인프로세스를 주어진 초만큼 정지
#################################

# 모듈을 읽어 들입니다.

import time
import datetime

now = time.time()
print(now)

print(datetime.datetime.now(), "5초동안 정지")
time.sleep(5)
print(datetime.datetime.now(), "프로그램 종료")
