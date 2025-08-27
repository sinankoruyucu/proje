# 🚀 Diyetisyen Türkmen KURT - Kurulum Kılavuzu

## 📋 Sistem Gereksinimleri

### ✅ Minimum Gereksinimler
- **İşletim Sistemi:** Windows 10/11 (64-bit)
- **Python:** 3.8 veya üzeri
- **RAM:** 4 GB
- **Disk Alanı:** 100 MB boş alan
- **Ekran:** 1024x768 çözünürlük

### 🔧 Önerilen Gereksinimler
- **İşletim Sistemi:** Windows 11 (64-bit)
- **Python:** 3.11 veya üzeri
- **RAM:** 8 GB
- **Disk Alanı:** 500 MB boş alan
- **Ekran:** 1920x1080 çözünürlük

## 🎯 Kurulum Adımları

### 1. Python Kurulumu

#### Python Yüklü Değilse:
1. **Python İndirme:**
   - https://www.python.org/downloads/ adresine gidin
   - "Download Python" butonuna tıklayın
   - En son sürümü indirin (3.11.x önerilir)

2. **Python Kurulumu:**
   - İndirilen dosyayı çalıştırın
   - **"Add Python to PATH"** seçeneğini **mutlaka işaretleyin**
   - "Install Now" tıklayın
   - Kurulumu tamamlayın

3. **Kurulum Doğrulama:**
   - Windows + R tuşlarına basın
   - `cmd` yazın ve Enter'a basın
   - `python --version` komutunu çalıştırın
   - Python sürümü görünmelidir

#### Python Zaten Yüklüyse:
- Windows + R → `cmd` → `python --version`
- Sürüm 3.8 veya üzeri olmalıdır

### 2. Program Kurulumu

#### Otomatik Kurulum (Önerilen):
1. **Kurulum Dosyasını Çalıştır:**
   - `KURULUM.bat` dosyasına çift tıklayın
   - Veya komut satırında `KURULUM.bat` çalıştırın

2. **Kurulum Sihirbazını Takip Edin:**
   - Kurulum yolunu seçin (varsayılan: C:\DiyetisyenTurkmenKurt)
   - Kurulum seçeneklerini belirleyin
   - "Kurulumu Başlat" tıklayın

3. **Kurulum Tamamlanmasını Bekleyin:**
   - İlerleme çubuğunu takip edin
   - Kurulum tamamlandı mesajını bekleyin

#### Manuel Kurulum:
1. **Dosyaları Kopyalayın:**
   ```bash
   # Yeni klasör oluştur
   mkdir C:\DiyetisyenTurkmenKurt
   
   # Dosyaları kopyala
   copy *.py C:\DiyetisyenTurkmenKurt\
   copy *.txt C:\DiyetisyenTurkmenKurt\
   copy *.exe C:\DiyetisyenTurkmenKurt\
   copy *.md C:\DiyetisyenTurkmenKurt\
   ```

2. **Python Bağımlılıklarını Yükleyin:**
   ```bash
   pip install tkcalendar
   ```

3. **Veritabanını Oluşturun:**
   ```bash
   cd C:\DiyetisyenTurkmenKurt
   python setup.py
   ```

## ⚙️ Kurulum Seçenekleri

### 📁 Kurulum Yolu
- **Varsayılan:** `C:\DiyetisyenTurkmenKurt`
- **Özel:** İstediğiniz klasörü seçebilirsiniz
- **Not:** Türkçe karakter içermeyen yol seçin

### 🔗 Kısayollar
- **Masaüstü Kısayolu:** Programı masaüstünden başlatma
- **Başlat Menüsü:** Windows başlat menüsünden erişim
- **Otomatik Başlatma:** Windows açılışında otomatik başlatma

### 🔔 Bildirim Sistemi
- **Otomatik Bildirimler:** Program kapalıyken çalışan sistem
- **Windows Görev Zamanlayıcısı:** Manuel kurulum gerekli
- **Ses Bildirimleri:** Modern bildirim sesleri

## 🎯 İlk Çalıştırma

### Programı Başlatma:
1. **Masaüstü Kısayolu:** "Diyetisyen Türkmen KURT" kısayoluna çift tıklayın
2. **Başlat Menüsü:** Başlat → Diyetisyen Türkmen KURT
3. **Manuel:** Kurulum klasöründe `main.py` çalıştırın

### İlk Açılış:
- Program otomatik olarak veritabanını oluşturacak
- Ana ekran açılacak
- Tüm sekmeler kullanıma hazır olacak

## 🔧 Sorun Giderme

### ❌ Python Bulunamadı
**Belirtiler:**
- "Python bulunamadı" hatası
- Python komutu çalışmıyor

**Çözüm:**
1. Python'u yeniden yükleyin
2. "Add Python to PATH" seçeneğini işaretleyin
3. Bilgisayarı yeniden başlatın
4. Komut satırında `python --version` test edin

### ❌ tkcalendar Kütüphanesi Eksik
**Belirtiler:**
- "No module named 'tkcalendar'" hatası
- Takvim widget'ı çalışmıyor

**Çözüm:**
```bash
pip install tkcalendar
```

### ❌ Veritabanı Hatası
**Belirtiler:**
- "Database error" mesajları
- Veriler yüklenmiyor

**Çözüm:**
1. Kurulum klasöründe `customers.db` dosyasının varlığını kontrol edin
2. Gerekirse `setup.py` çalıştırarak veritabanını yeniden oluşturun


## 📊 Kurulum Sonrası Kontrol

### ✅ Başarılı Kurulum Kontrolü:
1. **Program Açılıyor:** Ana ekran görünüyor
2. **Veritabanı Çalışıyor:** Müşteri/sipariş ekleme çalışıyor
3. **Kısayollar:** Masaüstü ve başlat menüsü kısayolları var
4. **Otomatik Başlatma:** Windows açılışında program başlıyor

### 🔍 Test Komutları:
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
1. `KALDIR.bat` dosyasını çalıştırın
2. Onay verin
3. Kaldırma işlemini bekleyin

### Manuel Kaldırma:
1. `python uninstall.py` çalıştırın
2. GUI'de seçenekleri belirleyin
3. "Kaldırmayı Başlat" tıklayın

### Kaldırma Seçenekleri:
- **Masaüstü Kısayolu:** Kısayolu sil
- **Başlat Menüsü:** Menüden kaldır
- **Otomatik Başlatma:** Başlangıçtan kaldır
- **Bildirim Sistemi:** Windows görev zamanlayıcısından kaldır
- **Veritabanı:** Tüm verileri sil

## 📞 Destek

### 🔧 Sorun Bildirme:
1. Hata mesajını kopyalayın
2. Ekran görüntüsü alın
3. Sistem bilgilerini not edin
4. Destek ekibiyle iletişime geçin

### 📚 Dokümantasyon:
- **Kurulum Kılavuzu:** Bu dosya
- **Otomatik Bildirim Kılavuzu:** `OTOMATIK_BILDIRIM_KILAVUZU.md`
- **Manuel Kurulum Kılavuzu:** `MANUEL_KURULUM_KILAVUZU.md`
- **Proje Özeti:** `PROJE_OZETI_GUNCELLEME.md`

### 🆘 Acil Durumlar:
- **Veri Kaybı:** Veritabanı yedekleme dosyalarını kontrol edin
- **Program Açılmıyor:** Python kurulumunu kontrol edin
- **Sistem Çökmesi:** Bilgisayarı güvenli modda başlatın

---

**Kurulum Tamamlandı!** 🎉

Programınız artık kullanıma hazır. İyi çalışmalar!

**© 2025 Diyetisyen Türkmen KURT. Tüm hakları saklıdır.** 