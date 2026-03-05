

# -----------------------------------------------------------------------------------
from basic.Test.Common import add, mul

res_a = add(1,4)
print(res_a)

res_m = mul(1,4)
print(res_m)



# -----------------------------------------------------------------------------------

from basic.Test.CommonModule import MyCalcClass

MyCalcClass.point
MyCalcClass.adds(4,5)

addr1 = MyCalcClass()
addr1.point
addr1.add(5,2)


# -----------------------------------------------------------------------------------

from basic.Test.Common import *
# 위험성: 만약 내 파일에도 똑같은 이름의 함수가 있다면,
#        어느 게 실행될지 꼬일 수 있습니다. (현업에선 지양합니다.)


import basic.Test.Common
# 사용할 때마다 basic.Test.Common.MyCalcClass() 처럼
# 전체 주소를 다 적어줘야 합니다.
# 코드가 길어지지만 출처는 가장 확실

''' 가장 좋은 방법은 필요한 것만 명시적으로 가져오는 것(ClassName 등) '''
# -----------------------------------------------------------------------------------


# 프로그램을 설치하고 나면 Python 기본 library에 잡힌다
import numpy as np
