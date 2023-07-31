# 2941. 크로아티아 알파벳
text = list(input())
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0

while True:
    if "".join(text[0:3]) in croatia:
        cnt += 1
        del text[0:3]
    elif "".join(text[0:2]) in croatia:
        cnt += 1
        del text[0:2]
    else:
        cnt += 1
        del text[0]

    if len(text) == 0: # text 길이가 0이면 while문 종료
        break


print(cnt)