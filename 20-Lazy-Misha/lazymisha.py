t1 = int(input('enter number:'))
t2 = int(input('enter number 2:'))
t3 = int(input('enter number 3:'))
if t1<t2 and t1<t3:
    print(t1)
elif t2<t1 and t2<t3:
    print(t2)
else:
    print(t3)