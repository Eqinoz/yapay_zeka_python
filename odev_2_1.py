import math
global sayac 
def asal(x):
    sayac = 0
    for sayi in range(1,x):
        if x % sayi==0 :
            sayac+=1
    
    if sayac >= 3:
        print(x, ", Asal Değildir.")
    else:
        print(x,"Asaldır")


asal(int(input("Bir Sayı Değeri Giriniz ")))

