
likes = []
dislikes = []
# Taking input for the first line
# t represents the initial number of customers
t = int(input())

# Lopping through each t, such that we want to append each customers likes and dislikes
for i in range(t):
    # Taking  in liked ingredients
    n = input()
    # Then spliting the list cuz it has spaces and stuff
    l1 = n.split()
    # Removing the initial item cuz it contains an int as string which we don't want
    if int(n[0]) != 0:
        l1.pop(0)
        likes.extend(l1)
    # Doing the same like the Likes
    k = input()
    l2 = k.split()
    if int(k[0]) != 0:
        l2.pop(0)
        dislikes.extend(l2)

# Python list comprehension,
final = [x for x in likes if x not in dislikes]
# filtering the list
final = list(dict.fromkeys(final))
f = open('0.txt',"w")
ans = str( (len(final), " ".join(map(str, final))))
# Removing unnecessary stuffs
ans = ''.join(c for c in ans if c  not in '()\',')
print(ans)
f.write(ans)
f.close()