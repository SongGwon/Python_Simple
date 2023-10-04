# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = int(input("단수: "))


# for i in range(1,10):
#    print(f"{dan}x{i}={dan*i}")

# 문제2) 2단부터 9단까지 출력(중첩 for문)
for i in range(2,10):
      for j in range(1,10):
          print(f"{i}x{j}={j*i}")



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

# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]

print(num_min) # 1 출력