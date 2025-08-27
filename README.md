# 🎯 Diyetisyen Türkmen KURT - Müşteri Yönetim Sistemi

## 📋 Proje Hakkında

Bu proje, diyetisyenlik hizmetleri için geliştirilmiş kapsamlı bir müşteri ve sipariş yönetim sistemidir. Python, SQLite ve Tkinter kullanılarak geliştirilmiştir.

## ✨ Özellikler

### 🔧 Temel Özellikler
- **Müşteri Yönetimi:** Danışan kayıt, düzenleme, silme, arama
- **Sipariş Yönetimi:** Sipariş ekleme, düzenleme, takip
- **Gelir Takibi:** Toplam gelir ve müşteri istatistikleri
- **Ödeme Kontrolü:** Yaklaşan ve gecikmiş ödemelerin takibi

### 🔔 Bildirim Sistemi
- **Otomatik Bildirimler:** Program kapalıyken çalışan sistem
- **Ses Bildirimleri:** Modern, ayarlanabilir ses seviyesi
- **Görsel Bildirimler:** Windows mesaj kutuları
- **Zamanlanmış Kontroller:** Her 5 dakikada bir otomatik kontrol

### 🎨 Kullanıcı Arayüzü
- **Modern Tasarım:** Temiz ve kullanıcı dostu arayüz
- **Sekmeli Yapı:** Danışan Kayıt, Siparişler, Gelir ve Müşteriler, Ödeme Kontrol
- **Takvim Entegrasyonu:** Tarih seçimi için takvim widget'ı
- **Arama Fonksiyonu:** Hızlı müşteri ve sipariş arama

## 🚀 Hızlı Başlangıç

### 📦 Kurulum

#### Otomatik Kurulum (Önerilen):
```bash
# 1. Kurulum dosyasını çalıştır
KURULUM.bat

# 2. Kurulum sihirbazını takip et
# 3. Programı başlat
```

#### Manuel Kurulum:
```bash
# 1. Python bağımlılıklarını yükle
pip install -r requirements.txt

# 2. Ana programı çalıştır
python main.py

# 3. Otomatik bildirim sistemini test et
python test_bildirim_kontrol.py
```

### 🎯 İlk Kullanım

1. **Programı Başlatın:**
   - Masaüstü kısayolunu kullanın
   - Veya `python main.py` komutunu çalıştırın

2. **İlk Müşteriyi Ekleyin:**
   - "Danışan Kayıt" sekmesine gidin
   - "Yeni Müşteri" butonuna tıklayın
   - Müşteri bilgilerini doldurun

3. **İlk Siparişi Oluşturun:**
   - "Siparişler" sekmesine gidin
   - "Yeni Sipariş" butonuna tıklayın
   - Sipariş detaylarını doldurun


## 📁 Dosya Yapısı

```
İLK PROJE/
├── main.py                          # Ana program girişi
├── gui.py                           # Kullanıcı arayüzü
├── database.py                      # Veritabanı işlemleri
├── setup.py                         # Kurulum scripti
├── uninstall.py                     # Kaldırma scripti
├── bildirim_kontrol.py              # Otomatik bildirim scripti
├── test_bildirim_kontrol.py         # Test scripti
├── KURULUM.bat                      # Kurulum batch dosyası
├── KALDIR.bat                       # Kaldırma batch dosyası
├── customers.db                     # SQLite veritabanı
├── nircmd.exe                       # Windows ses kontrol aracı
├── requirements.txt                 # Python bağımlılıkları
├── README.md                        # Bu dosya
├── KURULUM_KILAVUZU.md             # Detaylı kurulum kılavuzu
├── OTOMATIK_BILDIRIM_KILAVUZU.md   # Otomatik bildirim kılavuzu
├── MANUEL_KURULUM_KILAVUZU.md      # Manuel kurulum kılavuzu
└── PROJE_OZETI_GUNCELLEME.md       # Proje özeti
```

## 🛠️ Sistem Gereksinimleri

### ✅ Minimum Gereksinimler
- **İşletim Sistemi:** Windows 10/11 (64-bit)
- **Python:** 3.8 veya üzeri
- **RAM:** 4 GB
- **Disk Alanı:** 100 MB boş alan

### 🔧 Önerilen Gereksinimler
- **İşletim Sistemi:** Windows 11 (64-bit)
- **Python:** 3.11 veya üzeri
- **RAM:** 8 GB
- **Disk Alanı:** 500 MB boş alan

## 🔧 Kurulum Seçenekleri

### 📁 Kurulum Yolu
- **Varsayılan:** `C:\DiyetisyenTurkmenKurt`
- **Özel:** İstediğiniz klasörü seçebilirsiniz

### 🔗 Kısayollar
- **Masaüstü Kısayolu:** Programı masaüstünden başlatma
- **Başlat Menüsü:** Windows başlat menüsünden erişim
- **Otomatik Başlatma:** Windows açılışında otomatik başlatma

### 🔔 Bildirim Sistemi
- **Otomatik Bildirimler:** Program kapalıyken çalışan sistem
- **Windows Görev Zamanlayıcısı:** Manuel kurulum gerekli
- **Ses Bildirimleri:** Modern bildirim sesleri

## 📊 Kullanım Kılavuzu

### 🎯 Müşteri Yönetimi
1. **Yeni Müşteri Ekleme:**
   - "Danışan Kayıt" sekmesine gidin
   - "Yeni Müşteri" butonuna tıklayın
   - Tüm alanları doldurun ve kaydedin

2. **Müşteri Düzenleme:**
   - Müşteri listesinden birini seçin
   - "Düzenle" butonuna tıklayın
   - Bilgileri güncelleyin

3. **Müşteri Arama:**
   - Arama kutusuna ad, e-posta veya telefon yazın
   - Sonuçlar otomatik olarak filtrelenecek

### 📦 Sipariş Yönetimi
1. **Yeni Sipariş Oluşturma:**
   - "Siparişler" sekmesine gidin
   - "Yeni Sipariş" butonuna tıklayın
   - Müşteri seçin ve sipariş detaylarını doldurun

2. **Sipariş Düzenleme:**
   - Sipariş listesinden birini seçin
   - "Siparişi Düzenle" butonuna tıklayın
   - Detayları güncelleyin

3. **Tarih Seçimi:**
   - Takvim widget'ını kullanın
   - Tarihler DD.MM.YYYY formatında kaydedilir

### 💰 Gelir Takibi
- **Toplam Gelir:** Tüm siparişlerin toplam geliri
- **Toplam Sipariş:** Toplam sipariş sayısı
- **Toplam Müşteri:** Toplam müşteri sayısı
- **Gerçek Zamanlı Güncelleme:** Otomatik istatistik güncelleme

### 🔔 Ödeme Kontrolü
1. **Manuel Kontrol:**
   - "Ödeme Kontrol" sekmesine gidin
   - "Ödemeleri Kontrol Et" butonuna tıklayın
   - Bildirim penceresi açılacak


## 🔧 Sorun Giderme

### ❌ Yaygın Sorunlar

#### Python Bulunamadı
```bash
# Python'u yükleyin ve PATH'e ekleyin
# https://www.python.org/downloads/
```

#### tkcalendar Kütüphanesi Eksik
```bash
pip install tkcalendar
```

#### Veritabanı Hatası
```bash
# Veritabanını yeniden oluşturun
python setup.py
```


### 🔍 Test Komutları
```bash
# Program testi
python main.py

# Bildirim sistemi testi
python test_bildirim_kontrol.py

# Veritabanı testi
python -c "import sqlite3; conn=sqlite3.connect('customers.db'); print('DB OK')"
```

## 🗑️ Program Kaldırma

### Otomatik Kaldırma:
```bash
KALDIR.bat
```

### Manuel Kaldırma:
```bash
python uninstall.py
```

## 📞 Destek

### 📚 Dokümantasyon:
- **Kurulum Kılavuzu:** `KURULUM_KILAVUZU.md`
- **Otomatik Bildirim Kılavuzu:** `OTOMATIK_BILDIRIM_KILAVUZU.md`
- **Manuel Kurulum Kılavuzu:** `MANUEL_KURULUM_KILAVUZU.md`
- **Proje Özeti:** `PROJE_OZETI_GUNCELLEME.md`

### 🔧 Sorun Bildirme:
1. Hata mesajını kopyalayın
2. Ekran görüntüsü alın
3. Sistem bilgilerini not edin
4. Destek ekibiyle iletişime geçin

## 🚀 Gelecek Geliştirmeler

### 🔮 Planlanan Özellikler
- **E-posta Bildirimleri:** SMTP entegrasyonu
- **SMS Bildirimleri:** Telefon numarası entegrasyonu
- **Raporlama:** PDF/Excel rapor oluşturma
- **Yedekleme:** Otomatik veritabanı yedekleme
- **Çoklu Kullanıcı:** Kullanıcı yetkilendirme sistemi

### 🔧 Teknik İyileştirmeler
- **Web Arayüzü:** Flask/Django entegrasyonu
- **Mobil Uygulama:** React Native/Flutter
- **Cloud Veritabanı:** PostgreSQL/MySQL
- **API Entegrasyonu:** RESTful API
- **Docker Container:** Kolay dağıtım

## 📄 Lisans

Bu proje Diyetisyen Türkmen KURT için özel olarak geliştirilmiştir.

**© 2025 Diyetisyen Türkmen KURT. Tüm hakları saklıdır.**

---

**🎉 Programınız artık kullanıma hazır!**

Kurulum için `KURULUM.bat` dosyasını çalıştırın ve kılavuzları takip edin.

**İyi çalışmalar!** 🚀 