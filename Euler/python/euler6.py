plus=0
expon=0
for i in range(1,101):
    plus=plus+i**2
for i in range(1,101):
    expon=expon+i
print((expon**2)-plus)