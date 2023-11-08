n=int(input("Enter the no of 4-letter prompts: "))
a=[]

for i in range(n):
    prompt = input("Enter prompt ",i+1,": ")
    if len(prompt) != 4:
        print("Prompt should be 4 letters long")
        exit(1)
    a.append(prompt)

b=[]
c=[]

for i in range(len(a) - 1):
    for j in range(len(a[0])):
        if a[i][j:]==a[i+1][:-j]:
            c.append(a[i])
            c.append(a[i+1])
            b.append(a[i][j:])

d=''.join([ele for ele in b])
n=len(b[0])
d=c[0][:-n]+d
final=d+c[len(c)-1][n:]

print("\n")
print("The common elements are: ", b)
print("The final word is: ", final)

for i in a:
    if i not in final:
        print("Other Word : ",i)