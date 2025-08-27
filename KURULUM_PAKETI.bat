@echo off
chcp 65001 >nul
title Diyetisyen Türkmen KURT - Kurulum Paketi

echo.
echo ========================================
echo    Diyetisyen Türkmen KURT
echo    Kurulum Paketi
echo ========================================
echo.

:: Kurulum yolu
set INSTALL_PATH=C:\DiyetisyenTurkmenKurt

echo 📁 Kurulum yolu: %INSTALL_PATH%
echo.

:: Kurulum klasörünü oluştur
if not exist "%INSTALL_PATH%" (
    echo ✅ Kurulum klasörü oluşturuluyor...
    mkdir "%INSTALL_PATH%"
) else (
    echo ℹ️ Kurulum klasörü zaten mevcut
)

:: EXE dosyasını kopyala
if exist "DiyetisyenTurkmenKurt.exe" (
    echo ✅ Program dosyası kopyalanıyor...
    copy "DiyetisyenTurkmenKurt.exe" "%INSTALL_PATH%\" >nul
    echo ✅ Program dosyası kopyalandı
) else (
    echo ❌ DiyetisyenTurkmenKurt.exe bulunamadı!
    echo Lütfen EXE dosyasının bu script ile aynı klasörde olduğundan emin olun.
    pause
    exit /b 1
)

:: Veritabanını kopyala (varsa)
if exist "customers.db" (
    echo ✅ Veritabanı kopyalanıyor...
    copy "customers.db" "%INSTALL_PATH%\" >nul
    echo ✅ Veritabanı kopyalandı
) else (
    echo ℹ️ Veritabanı bulunamadı, yeni oluşturulacak
)

:: Ses dosyalarını kopyala (varsa)
if exist "nircmd.exe" (
    echo ✅ Ses kontrolü dosyası kopyalanıyor...
    copy "nircmd.exe" "%INSTALL_PATH%\" >nul
    echo ✅ Ses kontrolü dosyası kopyalandı
)

if exist "nircmdc.exe" (
    echo ✅ Ses kontrolü dosyası (alternatif) kopyalanıyor...
    copy "nircmdc.exe" "%INSTALL_PATH%\" >nul
    echo ✅ Ses kontrolü dosyası (alternatif) kopyalandı
)

:: Masaüstü kısayolu oluştur
echo ✅ Masaüstü kısayolu oluşturuluyor...
set DESKTOP_PATH=%USERPROFILE%\Desktop
set SHORTCUT_PATH=%DESKTOP_PATH%\Diyetisyen Türkmen KURT.bat

echo @echo off > "%SHORTCUT_PATH%"
echo chcp 65001 ^>nul >> "%SHORTCUT_PATH%"
echo title Diyetisyen Türkmen KURT >> "%SHORTCUT_PATH%"
echo cd /d "%INSTALL_PATH%" >> "%SHORTCUT_PATH%"
echo start DiyetisyenTurkmenKurt.exe >> "%SHORTCUT_PATH%"
echo exit >> "%SHORTCUT_PATH%"

echo ✅ Masaüstü kısayolu oluşturuldu

:: Başlat menüsü kısayolu oluştur
echo ✅ Başlat menüsü kısayolu oluşturuluyor...
set START_MENU_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Diyetisyen Türkmen KURT
if not exist "%START_MENU_PATH%" mkdir "%START_MENU_PATH%"

set START_MENU_SHORTCUT=%START_MENU_PATH%\Diyetisyen Türkmen KURT.bat
echo @echo off > "%START_MENU_SHORTCUT%"
echo chcp 65001 ^>nul >> "%START_MENU_SHORTCUT%"
echo title Diyetisyen Türkmen KURT >> "%START_MENU_SHORTCUT%"
echo cd /d "%INSTALL_PATH%" >> "%START_MENU_SHORTCUT%"
echo start DiyetisyenTurkmenKurt.exe >> "%START_MENU_SHORTCUT%"
echo exit >> "%START_MENU_SHORTCUT%"

echo ✅ Başlat menüsü kısayolu oluşturuldu

echo.
echo ========================================
echo ✅ Kurulum tamamlandı!
echo ========================================
echo.
echo 📋 Kurulum Detayları:
echo    • Program: %INSTALL_PATH%\DiyetisyenTurkmenKurt.exe
echo    • Masaüstü Kısayolu: %SHORTCUT_PATH%
echo    • Başlat Menüsü: %START_MENU_SHORTCUT%
echo.
echo 🚀 Programı başlatmak için:
echo    1. Masaüstündeki "Diyetisyen Türkmen KURT.bat" dosyasına çift tıklayın
echo    2. Veya %INSTALL_PATH%\DiyetisyenTurkmenKurt.exe dosyasını çalıştırın
echo    3. Veya Başlat menüsünden "Diyetisyen Türkmen KURT" seçin
echo.
echo 📞 Destek için: Diyetisyen Türkmen KURT
echo.
pause 