def fib(x):
    sum=0
    a=0
    b=1
    if x<0:
        print("invalid input")
    else:
        if x==1:
          print(a)
        else:
            print(b)
            for i in range(2,x):
                    sum=a+b
                    a=b
                    b=sum
                    print(sum)

x=int(input("enter a no"))
fib(x)