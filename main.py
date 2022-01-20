
likes = []
dislikes = []

# with open("test/a.txt") as fl:
#     for line in fl:
#         t = line[0]
#         for i in range(int(t)):
#             n =



t = int(input())



for i in range(t):
    n = input()
    l1 = n.split()
    if int(n[0]) != 0:
        l1.pop(0)
        likes.extend(l1)
    k = input()
    l2 = k.split()
    if int(k[0]) != 0:
        l2.pop(0)
        dislikes.extend(l2)


final = [x for x in likes if x not in dislikes]
final = list(dict.fromkeys(final))
f = open('0.txt',"w")
ans = str( (len(final), " ".join(map(str, final))))
ans = ''.join(c for c in ans if c  not in '()\',')
print(ans)
f.write(ans)
f.close()