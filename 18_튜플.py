# chapter03_4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) #한번 선언하면 불변(리스트와 차이)

# 선언
a = ()
b = (1,) #튜플에서 값이 하나일땐 쉼표 꼮 찍기
c = (11, 12, 13, 14)
d = (100, 1000, 'Jay', 'Bae', 'Hello')
e = (100, 1000, ('Jay', 'Bae', 'Hello'))

# 인덱싱
print('>>>>>>')
print('d = ', d[1])
print('d = ', d[0] + d[1] + d[1])
print('d = ', d[-1])
print('d = ', e[-1])
print('d = ', e[-1][1])
print('d = ', list(e[-1][1]))

# 수정 x
#d[0] = 1500

#슬라이싱
print(">>>>>>>>>>>")
print('d = ', d[0:3])
print('d = ', d[2:])
print('e = ', e[2][1:3])

# 튜플 연산
print('>>>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
