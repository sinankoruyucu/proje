#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diyetisyen Türkmen KURT - EXE Oluşturma Scripti
PyInstaller kullanarak tek dosya EXE oluşturur
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pyinstaller():
    """PyInstaller'ın kurulu olup olmadığını kontrol eder"""
    try:
        import PyInstaller
        print("✅ PyInstaller bulundu")
        return True
    except ImportError:
        print("❌ PyInstaller bulunamadı")
        return False

def install_pyinstaller():
    """PyInstaller'ı kurar"""
    print("📦 PyInstaller kuruluyor...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller kuruldu")
        return True
    except subprocess.CalledProcessError:
        print("❌ PyInstaller kurulamadı!")
        return False

def create_spec_file():
    """PyInstaller spec dosyası oluşturur"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
    ],
    datas=[
        ('customers.db', '.'),
        ('*.md', '.'),
        ('*.txt', '.'),
    ],
    hiddenimports=[
        'tkcalendar',
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'sqlite3',
        'datetime',
        'threading',
        'subprocess',
        'os',
        'sys',
        'shutil',
        'pathlib',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DiyetisyenTurkmenKurt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    with open('DiyetisyenTurkmenKurt.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ Spec dosyası oluşturuldu")

def build_exe():
    """EXE dosyasını oluşturur"""
    print("🔨 EXE dosyası oluşturuluyor...")
    print("Bu işlem birkaç dakika sürebilir...")
    
    try:
        # PyInstaller'ı çalıştır
        subprocess.check_call([
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--name=DiyetisyenTurkmenKurt",
            "--add-data=customers.db;.",
            "--add-data=*.md;.",
            "--add-data=*.txt;.",
            "--hidden-import=tkcalendar",
            "--hidden-import=tkinter",
            "--hidden-import=tkinter.ttk",
            "--hidden-import=tkinter.messagebox",
            "--hidden-import=tkinter.filedialog",
            "--hidden-import=sqlite3",
            "--hidden-import=datetime",
            "--hidden-import=threading",
            "--hidden-import=subprocess",
            "--hidden-import=os",
            "--hidden-import=sys",
            "--hidden-import=shutil",
            "--hidden-import=pathlib",
            "main.py"
        ])
        
        print("✅ EXE dosyası oluşturuldu!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ EXE oluşturulurken hata: {e}")
        return False

def create_installer():
    """Basit kurulum scripti oluşturur"""
    installer_content = '''@echo off
chcp 65001 >nul
title Diyetisyen Türkmen KURT - Kurulum

echo ========================================
echo Diyetisyen Türkmen KURT
echo EXE Kurulum Scripti
echo ========================================
echo.

set INSTALL_PATH=C:\\DiyetisyenTurkmenKurt

echo Kurulum yolu: %INSTALL_PATH%
echo.

REM Kurulum klasörünü oluştur
if not exist "%INSTALL_PATH%" (
    mkdir "%INSTALL_PATH%"
    echo ✅ Kurulum klasörü oluşturuldu
)

REM EXE dosyasını kopyala
copy "dist\\DiyetisyenTurkmenKurt.exe" "%INSTALL_PATH%\\" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Program dosyası kopyalandı
) else (
    echo ❌ Program dosyası kopyalanamadı!
    pause
    exit /b 1
)

REM Masaüstü kısayolu oluştur
set DESKTOP=%USERPROFILE%\\Desktop
if exist "%DESKTOP%" (
    echo @echo off > "%DESKTOP%\\Diyetisyen Türkmen KURT.bat"
    echo cd /d "%INSTALL_PATH%" >> "%DESKTOP%\\Diyetisyen Türkmen KURT.bat"
    echo DiyetisyenTurkmenKurt.exe >> "%DESKTOP%\\Diyetisyen Türkmen KURT.bat"
    echo pause >> "%DESKTOP%\\Diyetisyen Türkmen KURT.bat"
    echo ✅ Masaüstü kısayolu oluşturuldu
)

echo.
echo ========================================
echo ✅ Kurulum tamamlandı!
echo ========================================
echo.
echo Programı başlatmak için:
echo 1. Masaüstündeki "Diyetisyen Türkmen KURT.bat" dosyasına çift tıklayın
echo 2. Veya %INSTALL_PATH%\\DiyetisyenTurkmenKurt.exe dosyasını çalıştırın
echo.
pause
'''
    
    with open('EXE_KURULUM.bat', 'w', encoding='utf-8') as f:
        f.write(installer_content)
    
    print("✅ Kurulum scripti oluşturuldu")

def main():
    """Ana fonksiyon"""
    print("🚀 Diyetisyen Türkmen KURT - EXE Oluşturma")
    print("=" * 50)
    
    # 1. PyInstaller kontrolü
    if not check_pyinstaller():
        if not install_pyinstaller():
            print("❌ PyInstaller kurulamadı! Manuel kurulum gerekli.")
            print("Komut: pip install pyinstaller")
            return False
    
    # 2. Gerekli dosyaları kontrol et
    required_files = ['main.py', 'gui.py', 'database.py']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Eksik dosyalar: {', '.join(missing_files)}")
        return False
    
    print("✅ Gerekli dosyalar mevcut")
    
    # 3. Veritabanını oluştur (eğer yoksa)
    if not os.path.exists('customers.db'):
        print("📊 Veritabanı oluşturuluyor...")
        try:
            subprocess.check_call([sys.executable, "setup.py"])
            print("✅ Veritabanı oluşturuldu")
        except subprocess.CalledProcessError:
            print("❌ Veritabanı oluşturulamadı!")
            return False
    
    # 4. EXE oluştur
    if build_exe():
        # 5. Kurulum scripti oluştur
        create_installer()
        
        print("\n" + "=" * 50)
        print("🎉 EXE oluşturma tamamlandı!")
        print("=" * 50)
        print("\nOluşturulan dosyalar:")
        print("📁 dist/DiyetisyenTurkmenKurt.exe - Ana program")
        print("📁 EXE_KURULUM.bat - Kurulum scripti")
        print("\nKurulum için:")
        print("1. dist/ klasöründeki EXE dosyasını kopyalayın")
        print("2. EXE_KURULUM.bat dosyasını çalıştırın")
        print("\nNot: EXE dosyası Python gerektirmez!")
        
        return True
    else:
        print("❌ EXE oluşturulamadı!")
        return False

if __name__ == "__main__":
    main() 