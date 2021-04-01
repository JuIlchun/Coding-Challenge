for i in range(1,500):
    for j in range(1,500):
        for k in range(1,500):
            if i+j+k==1000:
                if i**2+j**2==k**2:
                    print(i*j*k)