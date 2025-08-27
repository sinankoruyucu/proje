@echo off
chcp 65001 >nul
title Diyetisyen Türkmen KURT - Kurulum

echo ========================================
echo Diyetisyen Türkmen KURT
echo EXE Kurulum Scripti
echo ========================================
echo.

set INSTALL_PATH=C:\DiyetisyenTurkmenKurt

echo Kurulum yolu: %INSTALL_PATH%
echo.

REM Kurulum klasörünü oluştur
if not exist "%INSTALL_PATH%" (
    mkdir "%INSTALL_PATH%"
    echo ✅ Kurulum klasörü oluşturuldu
)

REM EXE dosyasını kopyala
copy "dist\DiyetisyenTurkmenKurt.exe" "%INSTALL_PATH%\" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Program dosyası kopyalandı
) else (
    echo ❌ Program dosyası kopyalanamadı!
    pause
    exit /b 1
)

REM Masaüstü kısayolu oluştur
set DESKTOP=%USERPROFILE%\Desktop
if exist "%DESKTOP%" (
    echo @echo off > "%DESKTOP%\Diyetisyen Türkmen KURT.bat"
    echo cd /d "%INSTALL_PATH%" >> "%DESKTOP%\Diyetisyen Türkmen KURT.bat"
    echo DiyetisyenTurkmenKurt.exe >> "%DESKTOP%\Diyetisyen Türkmen KURT.bat"
    echo pause >> "%DESKTOP%\Diyetisyen Türkmen KURT.bat"
    echo ✅ Masaüstü kısayolu oluşturuldu
)

echo.
echo ========================================
echo ✅ Kurulum tamamlandı!
echo ========================================
echo.
echo Programı başlatmak için:
echo 1. Masaüstündeki "Diyetisyen Türkmen KURT.bat" dosyasına çift tıklayın
echo 2. Veya %INSTALL_PATH%\DiyetisyenTurkmenKurt.exe dosyasını çalıştırın
echo.
pause
