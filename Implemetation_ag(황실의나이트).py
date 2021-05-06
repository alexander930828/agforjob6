input_data = input()

row = int(input_data[1])

column = int(ord(input_data[0])) - int(ord('a')) + 1 #컴퓨터의 처음 시작은 숫자가 0으로 시작하기때문에

# 나이트가 이동하는 8가지 방향을 제시

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인

result = 0
for step in steps:
    # 이동하고자하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_column >=1 and next_row <= 8 and next_column <=8:
        result += 1

print(result)