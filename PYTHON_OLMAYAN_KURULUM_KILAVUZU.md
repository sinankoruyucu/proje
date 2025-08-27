# 🚀 Python Olmayan Bilgisayara Kurulum Kılavuzu

## 📋 Genel Bakış

Bu kılavuz, Python yüklü olmayan bilgisayarlara **Diyetisyen Türkmen KURT** programını kurmak için hazırlanmıştır.

## 🎯 Kurulum Yöntemleri

### **Yöntem 1: EXE Dosyası (Önerilen)**

#### **Gereksinimler:**
- Windows 10/11 işletim sistemi
- 50 MB boş disk alanı
- USB bellek (opsiyonel)

#### **Adımlar:**

##### **1. Dosyaları Hazırlama:**
```
📦 Kurulum Paketi/
├── DiyetisyenTurkmenKurt.exe     # Ana program (21.8 MB)
├── KURULUM_PAKETI.bat            # Kurulum scripti
├── customers.db                  # Veritabanı (opsiyonel)
├── nircmd.exe                    # Ses kontrolü
├── nircmdc.exe                   # Ses kontrolü (alternatif)
└── README.md                     # Bu kılavuz
```

##### **2. Kurulum:**
1. **Kurulum paketini hedef bilgisayara kopyalayın**
2. **`KURULUM_PAKETI.bat` dosyasına çift tıklayın**
3. **Kurulum otomatik olarak tamamlanacak**

##### **3. Sonuç:**
- Program `C:\DiyetisyenTurkmenKurt\` klasörüne kurulur
- Masaüstünde kısayol oluşur
- Başlat menüsünde kısayol oluşur

### **Yöntem 2: Manuel Kurulum**

#### **Adımlar:**

##### **1. Klasör Oluşturma:**
```batch
# Komut satırında:
mkdir C:\DiyetisyenTurkmenKurt
```

##### **2. Dosyaları Kopyalama:**
```batch
# EXE dosyasını kopyala
copy DiyetisyenTurkmenKurt.exe C:\DiyetisyenTurkmenKurt\

# Veritabanını kopyala (varsa)
copy customers.db C:\DiyetisyenTurkmenKurt\

# Ses dosyalarını kopyala (varsa)
copy nircmd.exe C:\DiyetisyenTurkmenKurt\
copy nircmdc.exe C:\DiyetisyenTurkmenKurt\
```

##### **3. Kısayol Oluşturma:**
```batch
# Masaüstünde .bat dosyası oluştur:
@echo off
chcp 65001 >nul
title Diyetisyen Türkmen KURT
cd /d "C:\DiyetisyenTurkmenKurt"
start DiyetisyenTurkmenKurt.exe
exit
```

### **Yöntem 3: USB ile Taşınabilir Kurulum**

#### **Adımlar:**

##### **1. USB Hazırlama:**
1. **USB belleği FAT32 olarak formatlayın**
2. **Kurulum dosyalarını USB'ye kopyalayın**
3. **USB'yi hedef bilgisayara takın**

##### **2. Kurulum:**
1. **USB'deki `KURULUM_PAKETI.bat` dosyasına çift tıklayın**
2. **Kurulum tamamlanacak**

##### **3. Avantajlar:**
- Taşınabilir kurulum
- Birden fazla bilgisayara kurulum
- Kolay yedekleme

## 📁 Kurulum Sonrası Dosya Yapısı

```
C:\DiyetisyenTurkmenKurt\
├── DiyetisyenTurkmenKurt.exe     # Ana program
├── customers.db                  # Veritabanı
├── nircmd.exe                    # Ses kontrolü
├── nircmdc.exe                   # Ses kontrolü (alternatif)
└── __pycache__\                  # Program cache (otomatik oluşur)
```

```
Masaüstü\
└── Diyetisyen Türkmen KURT.bat   # Kısayol
```

```
Başlat Menüsü\
└── Diyetisyen Türkmen KURT\
    └── Diyetisyen Türkmen KURT.bat   # Kısayol
```

## 🚀 Programı Başlatma

### **Yöntem 1: Masaüstü Kısayolu**
- Masaüstündeki "Diyetisyen Türkmen KURT.bat" dosyasına çift tıklayın

### **Yöntem 2: Doğrudan Çalıştırma**
- `C:\DiyetisyenTurkmenKurt\DiyetisyenTurkmenKurt.exe` dosyasına çift tıklayın

### **Yöntem 3: Başlat Menüsü**
- Başlat menüsünden "Diyetisyen Türkmen KURT" seçin

### **Yöntem 4: Komut Satırı**
```batch
cd C:\DiyetisyenTurkmenKurt
DiyetisyenTurkmenKurt.exe
```

## 🔧 Sorun Giderme

### **Sorun 1: Program Açılmıyor**
**Çözüm:**
1. Windows Defender'ı geçici olarak kapatın
2. Programı yönetici olarak çalıştırın
3. Antivirüs programını kontrol edin

### **Sorun 2: Ses Çalışmıyor**
**Çözüm:**
1. `nircmd.exe` dosyasının mevcut olduğunu kontrol edin
2. Windows ses ayarlarını kontrol edin
3. Programı yeniden başlatın

### **Sorun 3: Veritabanı Hatası**
**Çözüm:**
1. `customers.db` dosyasının mevcut olduğunu kontrol edin
2. Dosya izinlerini kontrol edin
3. Programı yönetici olarak çalıştırın

### **Sorun 4: Karakter Kodlaması Hatası**
**Çözüm:**
1. Windows dil ayarlarını kontrol edin
2. Türkçe karakter desteğini etkinleştirin
3. Programı yeniden başlatın

## 📊 Sistem Gereksinimleri

### **Minimum Gereksinimler:**
- **İşletim Sistemi:** Windows 10 (64-bit)
- **İşlemci:** Intel Core i3 veya AMD eşdeğeri
- **RAM:** 4 GB
- **Disk Alanı:** 50 MB
- **Ekran:** 1024x768 çözünürlük

### **Önerilen Gereksinimler:**
- **İşletim Sistemi:** Windows 11 (64-bit)
- **İşlemci:** Intel Core i5 veya AMD eşdeğeri
- **RAM:** 8 GB
- **Disk Alanı:** 100 MB
- **Ekran:** 1920x1080 çözünürlük

## 🔒 Güvenlik Notları

### **Antivirüs Uyarıları:**
- EXE dosyası PyInstaller ile oluşturulmuştur
- Bazı antivirüs programları yanlış uyarı verebilir
- Program güvenlidir, güvenilir kaynaklardan indirin

### **Dosya İzinleri:**
- Program yönetici izni gerektirebilir
- Veritabanı dosyası yazma izni gerektirir
- Ses dosyaları çalıştırma izni gerektirir

## 📞 Destek

### **Teknik Destek:**
- **Geliştirici:** Diyetisyen Türkmen KURT
- **E-posta:** [E-posta adresi]
- **Telefon:** [Telefon numarası]

### **Yaygın Sorunlar:**
1. **Program açılmıyor:** Windows Defender'ı kontrol edin
2. **Ses çalışmıyor:** Ses dosyalarını kontrol edin
3. **Veritabanı hatası:** Dosya izinlerini kontrol edin
4. **Karakter hatası:** Dil ayarlarını kontrol edin

## 🎉 Kurulum Tamamlandı!

Kurulum başarıyla tamamlandıktan sonra:

1. **Programı başlatın**
2. **Müşteri ekleyin**
3. **Sipariş oluşturun**
4. **Bildirimleri test edin**
5. **Ses sistemini kontrol edin**

**Program kullanıma hazır!** 🚀

---

**© 2025 Diyetisyen Türkmen KURT. Tüm hakları saklıdır.** 