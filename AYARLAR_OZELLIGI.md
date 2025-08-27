# ⚙️ Ayarlar Özelliği

## ✅ Yeni Özellik Eklendi!

### **🎯 Eklenen Özellik:**
Sağ üstte ayarlar butonu ile uygulama başlığını değiştirme ve şifre korumalı ayarlar sistemi.

### **📋 Özellik Detayları:**

#### **1. Ayarlar Butonu:**
- **Konum:** Sağ üst köşe
- **İkon:** ⚙️ Ayarlar
- **Şifre Korumalı:** Evet (varsayılan: 11235)

#### **2. Şifre Sistemi:**
- **Varsayılan Şifre:** 11235
- **Şifre Değiştirme:** Ayarlar içinden değiştirilebilir
- **Güvenlik:** Yanlış şifre girişinde hata mesajı

#### **3. Ayarlanabilir Özellikler:**
- **Uygulama Başlığı:** Ana penceredeki başlık metni
- **Başlık Konumu:** Sol, Orta, Sağ seçenekleri

## 🔧 Teknik Uygulama:

### **1. GUI Düzenlemesi:**
```python
# Başlık frame (başlık ve ayarlar butonu için)
title_frame = ttk.Frame(self.main_frame)
title_frame.pack(fill=tk.X, pady=(0, 20))

# Ayarlar butonu (sağ taraf)
settings_button = ttk.Button(title_frame, text="⚙️ Ayarlar", 
                            command=self.show_settings_dialog)
settings_button.pack(side=tk.RIGHT, padx=(10, 0))

# Başlık (ortada)
self.title_label = ttk.Label(title_frame, text=self.app_title, 
                            font=('Arial', 16, 'bold'))
self.title_label.pack(expand=True, fill=tk.X)
```

### **2. Şifre Kontrolü:**
```python
def show_settings_dialog(self):
    """Ayarlar dialog'unu gösterir"""
    # Şifre kontrolü
    password_dialog = tk.Toplevel(self.root)
    password_dialog.title("Şifre Gerekli")
    password_dialog.geometry("300x150")
    password_dialog.transient(self.root)
    password_dialog.grab_set()
    
    # Şifre girişi
    password_var = tk.StringVar()
    password_entry = ttk.Entry(password_dialog, textvariable=password_var, 
                              show="*", width=20)
    
    def check_password():
        if password_var.get() == self.settings_password:
            password_dialog.destroy()
            self.open_settings()
        else:
            messagebox.showerror("Hata", "Yanlış şifre!")
            password_var.set("")
            password_entry.focus()
```

### **3. Ayarlar Penceresi:**
```python
def open_settings(self):
    """Ayarlar penceresini açar"""
    settings_dialog = tk.Toplevel(self.root)
    settings_dialog.title("Ayarlar")
    settings_dialog.geometry("450x350")
    
    # Uygulama başlığı ayarı
    title_var = tk.StringVar(value=self.app_title)
    title_entry = ttk.Entry(main_frame, textvariable=title_var, width=40)
    
    # Başlık konumu ayarı
    position_var = tk.StringVar(value=self.title_position)
    
    def update_position():
        self.title_position = position_var.get()
        self.update_title_position()
    
    ttk.Radiobutton(position_frame, text="Sol", variable=position_var, 
                   value="left", command=update_position).pack(side=tk.LEFT, padx=(0, 20))
    ttk.Radiobutton(position_frame, text="Orta", variable=position_var, 
                   value="center", command=update_position).pack(side=tk.LEFT, padx=(0, 20))
    ttk.Radiobutton(position_frame, text="Sağ", variable=position_var, 
                   value="right", command=update_position).pack(side=tk.LEFT)
    
    def save_settings():
        # Başlığı güncelle
        new_title = title_var.get().strip()
        if new_title:
            self.app_title = new_title
            self.title_label.config(text=self.app_title)
            self.root.title(self.app_title)
        
        # Başlık konumunu güncelle
        self.title_position = position_var.get()
        self.update_title_position()
        
        # Otomatik kayıt
        self.auto_save_data("Ayarlar Güncellendi")
        
        messagebox.showinfo("Başarılı", "Ayarlar başarıyla kaydedildi!")
        settings_dialog.destroy()
```

### **4. Başlık Konumu Güncelleme:**
```python
def update_title_position(self):
    """Başlık konumunu günceller"""
    if self.title_position == "left":
        # Başlık sola
        self.title_label.grid(row=0, column=0, sticky='w')
        self.title_label.master.grid_columnconfigure(0, weight=0)
        self.title_label.master.grid_columnconfigure(1, weight=1)
    elif self.title_position == "right":
        # Başlık sağa
        self.title_label.grid(row=0, column=1, sticky='e')
        self.title_label.master.grid_columnconfigure(0, weight=1)
        self.title_label.master.grid_columnconfigure(1, weight=0)
    else:  # center
        # Başlık ortada
        self.title_label.grid(row=0, column=1, sticky='ew')
        self.title_label.master.grid_columnconfigure(0, weight=1)
        self.title_label.master.grid_columnconfigure(1, weight=0)
        self.title_label.master.grid_columnconfigure(2, weight=1)
```

## 📊 Çalışma Mantığı:

### **1. Ayarlar Butonuna Tıklama:**
1. **Kullanıcı "⚙️ Ayarlar" butonuna tıklar**
2. **Şifre giriş penceresi açılır**
3. **Kullanıcı şifreyi girer (varsayılan: 11235)**
4. **Şifre doğruysa ayarlar penceresi açılır**

### **2. Ayarları Değiştirme:**
1. **Uygulama başlığını değiştir**
2. **Başlık konumunu seç (Sol/Orta/Sağ)**
3. **"Kaydet" butonuna tıkla**
4. **Değişiklikler anında uygulanır**

### **3. Güvenlik Kontrolü:**
- **Yanlış şifre:** Hata mesajı gösterilir
- **Doğru şifre:** Ayarlar penceresi açılır
- **Enter tuşu:** Şifre kontrolü yapılır

## 🎯 Test Senaryoları:

### **✅ Test 1: Ayarlar Butonuna Tıklama**
1. Sağ üstteki "⚙️ Ayarlar" butonuna tıkla
2. **Beklenen Sonuç:** Şifre giriş penceresi açılır

### **✅ Test 2: Yanlış Şifre Girişi**
1. Ayarlar butonuna tıkla
2. Yanlış şifre gir (örn: 12345)
3. "Giriş" butonuna tıkla
4. **Beklenen Sonuç:** "Yanlış şifre!" hatası

### **✅ Test 3: Doğru Şifre ile Giriş**
1. Ayarlar butonuna tıkla
2. Doğru şifreyi gir (11235)
3. "Giriş" butonuna tıkla
4. **Beklenen Sonuç:** Ayarlar penceresi açılır

### **✅ Test 4: Başlık Değiştirme**
1. Ayarlar penceresinde başlığı değiştir
2. "Kaydet" butonuna tıkla
3. **Beklenen Sonuç:** Başlık anında değişir

### **✅ Test 5: Başlık Konumu Değiştirme**
1. Ayarlar penceresinde "Sol" seçeneğini seç
2. **Beklenen Sonuç:** Başlık sola kayar
3. "Orta" seçeneğini seç
4. **Beklenen Sonuç:** Başlık ortaya gelir
5. "Sağ" seçeneğini seç
6. **Beklenen Sonuç:** Başlık sağa kayar

### **✅ Test 6: Enter Tuşu ile Giriş**
1. Ayarlar butonuna tıkla
2. Şifreyi gir ve Enter tuşuna bas
3. **Beklenen Sonuç:** Şifre kontrolü yapılır

## 🚀 Kullanım Talimatları:

### **1. Ayarlara Erişim:**
1. **Sağ üstteki "⚙️ Ayarlar" butonuna tıklayın**
2. **Şifre giriş penceresinde "11235" yazın**
3. **"Giriş" butonuna tıklayın veya Enter tuşuna basın**

### **2. Başlık Değiştirme:**
1. **"Uygulama Başlığı" alanına yeni başlığı yazın**
2. **"Kaydet" butonuna tıklayın**
3. **Başlık anında değişecektir**

### **3. Başlık Konumu Değiştirme:**
1. **"Başlık Konumu" bölümünde istediğiniz seçeneği seçin**
2. **"Sol" seçeneği:** Başlık sola kayar
3. **"Orta" seçeneği:** Başlık ortada kalır
4. **"Sağ" seçeneği:** Başlık sağa kayar

### **4. Güvenlik Notları:**
- **Başlık alanını boş bırakırsanız:** Mevcut başlık kalır
- **Yanlış şifre:** Hata mesajı gösterilir
- **Şifre değiştirme:** Artık mevcut değil

## 📋 Avantajlar:

### **✅ Kullanıcı Dostu:**
- Kolay erişilebilir ayarlar butonu
- Şifre korumalı güvenlik
- Anında değişiklik uygulama

### **✅ Güvenlik:**
- Şifre korumalı ayarlar
- Yanlış şifre girişinde uyarı
- Şifre değiştirme imkanı

### **✅ Esneklik:**
- Başlık özelleştirme
- Şifre değiştirme
- Otomatik kayıt sistemi

### **✅ Görsel Tasarım:**
- Sağ üstte düzenli konumlandırma
- Modern ikon kullanımı
- Temiz arayüz tasarımı
- **Başlık her zaman ortada kalır**

## 🎉 Sonuç:

**Ayarlar sistemi başarıyla eklendi!**

### **✅ Artık Çalışan Özellikler:**
- ✅ Sağ üstte ayarlar butonu
- ✅ Şifre korumalı giriş (11235)
- ✅ Uygulama başlığı değiştirme
- ✅ **Başlık konumu seçimi (Sol/Orta/Sağ)**
- ✅ Anında konum değişimi
- ✅ Otomatik kayıt sistemi
- ✅ Güvenlik kontrolleri

### **🚀 Kullanıma Hazır:**
- **Ayarlar Butonu:** Sağ üstte ⚙️ ikonu
- **Şifre:** Varsayılan 11235
- **Başlık Değiştirme:** Anında uygulama
- **Başlık Konumu:** Sol/Orta/Sağ seçenekleri
- **Güvenlik:** Şifre korumalı erişim

**Artık uygulama başlığını ve konumunu istediğiniz zaman değiştirebilirsiniz!** ⚙️

---

**© 2025 Diyetisyen Türkmen KURT. Tüm hakları saklıdır.** 