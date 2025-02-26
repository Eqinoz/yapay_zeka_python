import math
def hesapla(x,y,z):
    if type(x)!=int or type(y)!=int:
        print("İlk 2 Değişken Sayı Değil")
        return
    if z=="+":
        print(f"{x}+{y}=",x+y)
    elif z=="/":
        if y == 0:
            print("Bölme İşlemi İçin İkinci Sayı 0 Olamaz!")
        else:
             print(f"{x}/{y}=",x/y) 
    elif z=="-":
         print(f"{x}-{y}=",x-y)
    elif z=="*":
         print(f"{x}*{y}=",x*y)
    else:
        print("Lütfen Geçerli Bir İşlem Seçiniz: +, *, -, /")

hesapla("2",2,"+")