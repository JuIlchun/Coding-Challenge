# num=1
# cnt=0
# ans=0
# for i in range(1,1001):
#     num=2*num
# cnt=len(str(num))-1
# for i in range(len(str(num))):
#     ans+=int(str(num)[cnt])
#     cnt-=1
# print (ans)

#correct

print(sum(map(int,str(2**1000))))