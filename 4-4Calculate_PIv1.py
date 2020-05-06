PI=0
N=90000
for k in range(N):
    PI += 1/pow(16,k) *(4/(8*k+1)-2/(8*k+4)-\
        1/(8*k+5)-1/(8*k+6))
print("PI is {}".format(PI))