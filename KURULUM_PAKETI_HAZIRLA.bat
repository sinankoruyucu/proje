@echo off
chcp 65001 >nul
title Kurulum Paketi Hazırlama

echo.
echo ========================================
echo    Kurulum Paketi Hazırlanıyor
echo ========================================
echo.

:: Kurulum paketi klasörü oluştur
set PACKAGE_DIR=KURULUM_PAKETI
if exist "%PACKAGE_DIR%" (
    echo ✅ Kurulum paketi klasörü zaten mevcut
) else (
    echo ✅ Kurulum paketi klasörü oluşturuluyor...
    mkdir "%PACKAGE_DIR%"
)

:: EXE dosyasını kopyala
if exist "dist\DiyetisyenTurkmenKurt.exe" (
    echo ✅ EXE dosyası kopyalanıyor...
    copy "dist\DiyetisyenTurkmenKurt.exe" "%PACKAGE_DIR%\" >nul
    echo ✅ EXE dosyası kopyalandı
) else (
    echo ❌ EXE dosyası bulunamadı!
    pause
    exit /b 1
)

:: Veritabanını kopyala
if exist "dist\customers.db" (
    echo ✅ Veritabanı kopyalanıyor...
    copy "dist\customers.db" "%PACKAGE_DIR%\" >nul
    echo ✅ Veritabanı kopyalandı
) else (
    echo ℹ️ Veritabanı bulunamadı
)

:: Ses dosyalarını kopyala
if exist "nircmd.exe" (
    echo ✅ Ses kontrolü dosyası kopyalanıyor...
    copy "nircmd.exe" "%PACKAGE_DIR%\" >nul
    echo ✅ Ses kontrolü dosyası kopyalandı
) else (
    echo ℹ️ nircmd.exe bulunamadı
)

if exist "nircmdc.exe" (
    echo ✅ Ses kontrolü dosyası alternatif kopyalanıyor...
    copy "nircmdc.exe" "%PACKAGE_DIR%\" >nul
    echo ✅ Ses kontrolü dosyası alternatif kopyalandı
) else (
    echo ℹ️ nircmdc.exe bulunamadı
)

:: Kurulum scriptini kopyala
if exist "KURULUM_PAKETI.bat" (
    echo ✅ Kurulum scripti kopyalanıyor...
    copy "KURULUM_PAKETI.bat" "%PACKAGE_DIR%\" >nul
    echo ✅ Kurulum scripti kopyalandı
) else (
    echo ❌ Kurulum scripti bulunamadı!
    pause
    exit /b 1
)

:: Kılavuzu kopyala
if exist "PYTHON_OLMAYAN_KURULUM_KILAVUZU.md" (
    echo ✅ Kurulum kılavuzu kopyalanıyor...
    copy "PYTHON_OLMAYAN_KURULUM_KILAVUZU.md" "%PACKAGE_DIR%\" >nul
    echo ✅ Kurulum kılavuzu kopyalandı
) else (
    echo ℹ️ Kurulum kılavuzu bulunamadı
)

:: README dosyası oluştur
echo ✅ README dosyası oluşturuluyor...
(
echo # Diyetisyen Türkmen KURT - Kurulum Paketi
echo.
echo ## 🚀 Hızlı Kurulum
echo.
echo ### 1. Kurulum:
echo    KURULUM_PAKETI.bat dosyasına çift tıklayın
echo.
echo ### 2. Programı Başlatma:
echo    Masaüstündeki "Diyetisyen Türkmen KURT.bat" dosyasına çift tıklayın
echo.
echo ## 📋 İçerik:
echo    • DiyetisyenTurkmenKurt.exe - Ana program
echo    • customers.db - Veritabanı
echo    • nircmd.exe - Ses kontrolü
echo    • nircmdc.exe - Ses kontrolü (alternatif)
echo    • KURULUM_PAKETI.bat - Kurulum scripti
echo    • PYTHON_OLMAYAN_KURULUM_KILAVUZU.md - Detaylı kılavuz
echo.
echo ## 📞 Destek:
echo    Diyetisyen Türkmen KURT
echo.
echo ---
echo © 2025 Diyetisyen Türkmen KURT. Tüm hakları saklıdır.
) > "%PACKAGE_DIR%\README.md"

echo ✅ README dosyası oluşturuldu

:: Paket içeriğini listele
echo.
echo ========================================
echo ✅ Kurulum Paketi Hazırlandı!
echo ========================================
echo.
echo 📁 Paket Klasörü: %PACKAGE_DIR%
echo.
echo 📋 Paket İçeriği:
dir "%PACKAGE_DIR%" /b
echo.
echo 📊 Dosya Boyutları:
for %%f in ("%PACKAGE_DIR%\*") do (
    echo    %%~nxf - %%~zf byte
)
echo.
echo 🚀 Kurulum için:
echo    1. %PACKAGE_DIR% klasörünü USB'ye kopyalayın
echo    2. Hedef bilgisayarda KURULUM_PAKETI.bat çalıştırın
echo.
echo 💡 Not: Bu paket Python gerektirmez!
echo.
pause 