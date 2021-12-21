"""
그냥 input().split() 을 사용하면 받은 값들이 모두 문자열로 저장된다.
하지만 map(input().split()) 를 사용하면 정수로 변환하여 저장된다.
split에 기준문자열이 없다면 공백을 기준으로 입력값을 분리하여 변수에 차례대로 저장한다.
"""
a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")