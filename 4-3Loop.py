#Break and Continue
Str="Python"
for c in Str:
    if c=="t":
        continue
    print(c,end='')
print("\n")
while Str!="":
    for c in Str:
        if  c=='t':
            break
        print(c,end='')
    Str=Str[:-1]