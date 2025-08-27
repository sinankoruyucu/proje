import tkinter as tk
from tkinter import messagebox
from gui import CustomerManagementGUI
import sys
import os
import ctypes

def main():
    """Ana uygulama fonksiyonu"""
    try:
        # Windows görev çubuğu için uygulama ID'si ayarla
        try:
            myappid = 'diyetisyen.turkmen.kurt.1.0'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except:
            pass
        
        # Ana pencere oluştur
        root = tk.Tk()
        
        # Pencereyi geçici olarak gizle
        root.withdraw()
        
        # Uygulama başlığı ve ikonu
        root.title("Diyetisyen Türkmen KURT")
        
        # Pencere ikonunu ayarla
        try:
            # Orijinal ikon kullan
            root.iconbitmap('icon.ico')
        except Exception as e:
            # Hata durumunda PNG'yi dene
            try:
                icon = tk.PhotoImage(file='icon.png')
                root.iconphoto(False, icon)
            except:
                # Hiçbiri çalışmazsa varsayılan ikon kullan
                print(f"İkon yükleme hatası: {e}")
        
        # Pencere boyutu ve konumu
        window_width = 1400
        window_height = 800
        
        # Ekran merkezinde konumlandır
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Minimum boyut ayarla
        root.minsize(800, 600)
        
        # GUI'yi başlat
        app = CustomerManagementGUI(root)
        
        # Pencereyi göster
        root.deiconify()
        
        # Pencere kapatma olayı
        def on_closing():
            if messagebox.askokcancel("Çıkış", "Uygulamadan çıkmak istediğinizden emin misiniz?"):
                root.destroy()
                sys.exit()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Uygulamayı başlat
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Kritik Hata", f"Uygulama başlatılırken hata oluştu:\n{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 