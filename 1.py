import random
numbei = random.randint(1,10)
aa = True
cc = False
i =1
for i in range(1):
    a= int(input("请输入整数:"))
#    b =isinstance(a,int)
    while aa:
        a= int(input("答错了，请重新输入:"))
        i+=1
        if a< numbei and i<3:
            print ("太小了",a,i)
        elif a > numbei and i<3:
            print ("太大了",a,i)
        elif i ==3:
            print ("NO chose")
            break
        elif b ==numbei:
            print ("很好\n"*5,numbei,i)
            b =False
print ('game over!!!')
