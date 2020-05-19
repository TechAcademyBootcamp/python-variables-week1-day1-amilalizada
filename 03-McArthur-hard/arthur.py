print('Oyun haqda qısa məlumatı istifadəçiyə print etməlidir')
month= int(input('doğulduğu ay:'))
age= int(input('yash?:'))
if 0<month and month<13:
    special=(month*2+5)*50+age-365
    print(special)
    summa=special+115
    print('ay:',summa//100,'age:',summa%100)
    
else:
    print('duzgun daxil edilmedi')    