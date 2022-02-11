num = int(input("Enter A Number\n").strip())
for i in range(num):
    print(" "*(num-i-1),"*"*(2*i+1),sep="")