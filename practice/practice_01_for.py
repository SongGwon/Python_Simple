# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = int(input("단수: "))


# for i in range(1,10):
#    print(f"{dan}x{i}={dan*i}")
print("="*100)
# 문제2) 2단부터 9단까지 출력(중첩 for문)
for i in range(2,10):
      for j in range(1,10):
          print(f"{i}x{j}={j*i}")


print("="*100)
# 문제3) list a의 평균값을 계산하세요
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# a길이 -> len(a)
sum = 0
#print(len(a))
for i in range(len(a)):
    sum += a[i]
#print(sum)
result = sum / len(a)
print(result)  # 평균값


for num in a:
    sum += num
result = sum / len(a)
# round(값, 자리수) : 자리수만큼 반올림
print(round(result, 2))
print("="*100)
# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]
num_min = sorted(b)[0]           # num_min = b[0]
print(num_min) # 1 출력           #  for x in b:
                                  #    if x < num_min:
                                            # num_min = x       +) #정렬하는 코드 짜보기
print("="*100)
# 문제5) list c의 최소값, 최대값 찾기
c = [2, 5, 7, 1, 8]
c_min = sorted(c)[0]
c_max = sorted(c)[int(len(c))-1]
print(c_min)
print(c_max)