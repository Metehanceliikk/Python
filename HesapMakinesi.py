def hesapla(a,b,islem):
    if islem not in "+ - / *":
        return print("lütfen ( + - * / )seçeneklerinden birini seçiniz")
    if(islem=="+"):
     return (str(a)+"+"+str(b)+"="+str(a+b))
    if(islem=="-"):
     return (str(a)+"-"+str(b)+"="+str(a-b))
    if(islem=="/"):
     return (str(a)+"/"+str(b)+"="+str(a/b))
    if(islem=="*"):
     return (str(a)+"*"+str(b)+"="+str(a*b))
    else:
        print("Tekrar deneyin")
        hesapla(a,b,islem)

while True:
    try:
        a=int(input("Lütfen 1. sayıyı giriniz"))
        b=int(input("Lütfen 2. sayıyı giriniz"))
        islem=input("Yapılmasını istediğiniz işlemi seçiniz (+ / - *)")
        print(hesapla(a,b,islem))
    except:
        print("Lütfen sayıları düzgün giriniz")