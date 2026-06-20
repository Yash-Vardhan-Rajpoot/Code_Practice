def solve():
    word=input()
    u=""
    l=""
    for i in range(len(word)):
        if word[i].isupper(): u+=word[i]
        else: l+=word[i]
    u=''.join(sorted(u))
    l=''.join(sorted(l))
    i=j=cnt=0
    while i<len(u) and j<len(l):
        s=u[i].lower()
        if s==l[j]:
            cnt+=1
            i+=1
            j+=1
        else:
            if s>l[j]: j+=1
            else: i+=1
    return cnt
print(solve())