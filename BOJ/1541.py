# 1541. 잃어버린 괄호
expression = input().split('-')

minus = []
for item in expression:
    tmp = 0
    if '+' in item:   # 플러스가 있는 애들은 다 더 함
        plus = list(map(int, item.split('+')))
        for p in plus:
            tmp += p
        minus.append(tmp)
    else:
        minus.append(int(item))

result = minus[0]
for i in range(1, len(minus)):
    result -= minus[i]


print(result)

