# 1759. 암호만들기
result = []


def make_password(idx, string):
    global result
    tmp = ""
    cnt = 0
    j_cnt = 0
    for i in idx:
        tmp += string[i]
        if string[i] in ["a", "e", "i", "o", "u"]:
            cnt += 1
        else:
            j_cnt += 1
    if cnt >= 1 and j_cnt >= 2:
        result.append(tmp)


# nCr
def comb(n, r):
    if r == 0:
        make_password(comb_list, string)
    elif n < r:
        return
    else:
        comb_list[r - 1] = numbers[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


L, C = map(int, input().split())
string = sorted(list(input().split()))
numbers = [i for i in range(C)]
comb_list = [0] * L

comb(C, L)
result.sort()

for res in result:
    print(res)
