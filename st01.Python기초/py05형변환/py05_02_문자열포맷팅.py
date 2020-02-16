# %s : 문자열, %d : 10진 정수

#문자열 포매팅
print( " I eat %d apples." %3) # 'I eat 3 apples.'

number = 10
day = "three"
print( "I ate %d apples. I was sick for %s days." % (number, day) )
# 'I ate 10 apples. so I was sick for three days.'

#정렬과 공백
print( "%10s" % "hi" )    # '             hi'
print( "%-10sjane." % "hi" )   #'hi           jane.'

#소수점 표현
"%0.4f" % 3.42134234   # ' 3.4213'
"%10.4f" % 3.42134234    # '                   3.4213'

