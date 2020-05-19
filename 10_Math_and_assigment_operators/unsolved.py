# istifadəçinin doğulduğu ili soruşun və neçə yaşda olduğunu hesablayıb print edin
# ==============================================
birthyear = int(input('ili daxil edin'))
# ==============================================

# 2022-ci ildə neçə yaşı olacaq?
# ==============================================
future = 2022 - birthyear
print('future')
# ==============================================

# iki rəqəmin ən böyük ortaq bölünənini tapın
# ==============================================
l1=[]
l2=[]
for i in range(1,birthyear+1):
    birthyear%1==0
    l1.append(i)

for j in range(1,future+1):
    future%j==0
    l2.append(j)

for i in reversed(l1):
    for j in reversed(l2):
        if i==j:
            print(i)
            exit()

