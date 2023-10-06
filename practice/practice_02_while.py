# 문제1) 로그인(pw) -> 3번 이상 암호를 틀리면 프로그램 종료!
pw = 1234


count = 0  # 틀린 횟수
#while True:
# if count >= 3:
#       print("종료: 암호를 3회 이상 틀리셨습니다.")
#        break
#    input_pw = int(input("암호: "))
#    if pw == input_pw:
#        print("hello")
#        break
#    else:
#       print("경고: 올바른 암호를 입력해주세요")        CTRL+/
#       count += 1

print("="*100)
# 문제2) 1~100까지 더해서 총합을 계산하세요
# - for문
a = list(range(1,101))
sum = 0
for x in a:
    sum += x
print(sum)

print("="*100)
# - while문
num = 1
sum2 = 0
while True:
    if num>100:
        break
    sum2 += num
    num += 1
print(sum2)