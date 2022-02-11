num = int(input("Enter A Number\n").strip())
for i in range(num):
    print(" "*(i),"*"*(num-i),sep="")