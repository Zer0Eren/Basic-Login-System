# 🔐 Güvenli Kullanıcı Kimlik Doğrulama Sistemi – Argon2 + Salt + Pepper + MongoDB (v1.3) 🚀

Bu proje, **güvenli ve ölçeklenebilir bir kullanıcı kimlik doğrulama sistemi** oluşturmayı amaçlamaktadır.  
**Argon2 hashing algoritması, Salt ve Pepper teknikleri** kullanılarak **şifre güvenliği en üst düzeye çıkarılmıştır.**  
**MongoDB ile entegre** çalışarak kullanıcı verilerini güvenli bir şekilde saklar ve doğrular.  

---

## 📌 **Özellikler**
✔ **Güçlü Şifreleme:** `Argon2 + Salt + Pepper` kullanarak güvenli bir hashleme sistemi.  
✔ **MongoDB Entegrasyonu:** Kullanıcı verilerini güvenli şekilde saklama.  
✔ **Şifre Doğrulama:** Giriş işlemlerinde şifrelerin güvenli bir şekilde karşılaştırılması.  
✔ **Deneme Hakkı Yönetimi:** 3 başarısız giriş denemesinden sonra erişim engellenir.  
✔ **PEPPER Yönetimi:** Şifreleme için kullanılan PEPPER anahtarı, `pepper.key` dosyasında tutulur.  

---

## 🏢 **Değişiklikler & Güncellemeler (v1.3)**  

- **👉 PEPPER Artık Dosyadan Okunuyor!** (`pepper.key`)
  - PEPPER kod içinde sabit değil, harici bir dosyadan yükleniyor.
  - Dosya yoksa hata verir.

- **👉 Argon2 + Salt + Pepper ile Daha Güçlü Şifreleme**
  - Kullanıcı şifreleri Argon2 hashleme algoritmasıyla saklanıyor.
  - Salt kullanımı eklendi, her kullanıcı için benzersiz hashleme sağlandı.
  - Girişte şifre, Salt ve PEPPER ile doğrulanıyor.

- **👉 MongoDB Entegrasyonu Tamamlandı**
  - Kullanıcı bilgileri güvenli bir şekilde MongoDB'ye kaydediliyor.
  - Kırsat ve Giriş işlemleri MongoDB tabanlı çalışıyor.


- **👉 Kod Daha Temiz ve Modüler Hale Getirildi**
  - PEPPER dosyadan okunuyor, varsayılan değer belirlendi.
  - Kod okunabilirliği arttırıldı, gereksiz tekrarlar kaldırıldı.
  - Hata yönetimi iyileştirildi.

---

## 📂 **Kurulum & Çalıştırma**
### **1️⃣ Gerekli Bağımlılıkları Yükleyin**
```sh
pip install pymongo argon2-cffi
```

### **2️⃣ MongoDB'yi Başlatın**
```sh
mongod --dbpath /veri/yolu
```

### **3️⃣ PEPPER Anahtarını Ayarlayın**
```sh
echo "30a2b9c47f3c8e4d9b88d5b1a6e8f7c3209847fd92a1b85e35c7d3f4e6a8b9d2" > pepper.key
```

### **4️⃣ Kullanıcı Kaydet**
```sh
python basic-register-system.py
```

### **5️⃣ Kullanıcı Girişi**
```sh
python basic-login-system.py
```

---

## 🚀 **Sonraki Sürüm (v1.4) Planları**

- **👉 Flask ile web arayüzü eklenecek!** (Giriş & Kayıt sayfaları)
- **👉 Şifre sıfırlama mekanizması eklenecek.**
- **👉 Kullanıcı dostu hata mesajları geliştirilecek.**

---

## ⚠ **Güvenlik Önlemleri**
✔ PEPPER dosyanızı `.gitignore` içine ekleyin!  
✔ MongoDB veritabanını dış dünyaya açık hale getirmeyin.  
✔ Şifre sıfırlama işlemi için iki aşamalı doğrulama (2FA) eklenebilir.  

---

## 🛠 **Kullanılan Teknolojiler**
- **Python 3.8+**
- **MongoDB**
- **Argon2 Hashing (argon2-cffi)**
- **PEPPER Anahtarı**
- **Salt ile Rastgele Hashleme**

---

## ⚠ Kullanım Şartları

Bu proje, geliştiricisinin izni olmadan **kopyalanamaz, dağıtılamaz veya ticari amaçla kullanılamaz.**  
Kod yalnızca **kişisel ve eğitim amaçlı kullanım** içindir.  
Herhangi bir yeniden dağıtım veya ticari kullanım için geliştiriciden **önceden yazılı izin alınmalıdır.**

