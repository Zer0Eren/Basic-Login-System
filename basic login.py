nm = "zero" #kullanıcı adı
sf = "29517048" #şifre 123
def sh(pw): #şifreyi hesaplayan fonksiyon
    return str(int(pw) * 2 * 12 * 9999)

dh = 3 #deneme hakkı

while dh > 0:
    ka = input("Kullanıcı adınızı giriniz: ")
    pw = input("Şifrenizi giriniz: ")

    if ka == nm and sh(pw) == sf:
        print("Giriş yaptınız.")
        break
    else:
        dh -= 1
        if dh > 0:
            print(f"Giriş yanlış. Kalan deneme hakkın: {dh}")
        else:
            print("Deneme hakkın kalmadı. Giriş başarısız.")