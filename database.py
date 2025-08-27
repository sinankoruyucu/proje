import sqlite3
import os
from datetime import datetime

class CustomerDatabase:
    def __init__(self, db_name="customers.db"):
        self.db_name = db_name
        self.create_tables()
        self.upgrade_message = self.upgrade_database()
    
    def create_tables(self):
        """Veritabanı tablolarını oluşturur"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Müşteriler tablosu
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                address TEXT,
                company TEXT,
                created_date TEXT,
                notes TEXT
            )
        ''')
        
        # Siparişler tablosu
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                order_date TEXT,
                start_date TEXT,
                end_date TEXT,
                product_name TEXT,
                quantity INTEGER,
                price REAL,
                total_price REAL,
                status TEXT,
                notification_sent INTEGER DEFAULT 0,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )
        ''')
        
        # Performans için index'ler
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_customers_name ON customers(name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON orders(customer_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_end_date ON orders(end_date)')
        
        conn.commit()
        conn.close()
    
    def upgrade_database(self):
        """Veritabanı şemasını yükseltir ve durum mesajı döndürür"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("PRAGMA table_info(orders)")
            columns = [column[1] for column in cursor.fetchall()]
            changes_made = False
            if 'start_date' not in columns:
                cursor.execute('ALTER TABLE orders ADD COLUMN start_date TEXT')
                changes_made = True
            if 'end_date' not in columns:
                cursor.execute('ALTER TABLE orders ADD COLUMN end_date TEXT')
                changes_made = True
            if 'notification_sent' not in columns:
                cursor.execute('ALTER TABLE orders ADD COLUMN notification_sent INTEGER DEFAULT 0')
                changes_made = True
            if changes_made:
                cursor.execute('''
                    UPDATE orders 
                    SET start_date = order_date, 
                        end_date = date(order_date, '+7 days')
                    WHERE start_date IS NULL OR end_date IS NULL
                ''')
            conn.commit()
            # Mesaj kaldırıldı - sessiz yükseltme
            return None
        except Exception as e:
            try:
                conn.close()
                import os
                if os.path.exists(self.db_name):
                    os.remove(self.db_name)
                    self.create_tables()
                return None
            except Exception as e2:
                return None
        finally:
            try:
                conn.close()
            except:
                pass
    
    def check_customer_exists(self, name):
        """Müşteri adının var olup olmadığını kontrol eder"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name FROM customers WHERE name = ?', (name,))
        customer = cursor.fetchone()
        
        conn.close()
        return customer
    
    def add_customer(self, name, email, phone, address, company, notes):
        """Yeni müşteri ekler"""
        # Önce aynı isimde müşteri var mı kontrol et
        existing_customer = self.check_customer_exists(name)
        if existing_customer:
            raise ValueError(f"'{name}' isimli müşteri zaten mevcut! (ID: {existing_customer[0]})")
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO customers (name, email, phone, address, company, created_date, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, address, company, created_date, notes))
        
        conn.commit()
        conn.close()
        return cursor.lastrowid
    
    def get_all_customers(self):
        """Tüm müşterileri getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM customers ORDER BY created_date DESC')
        customers = cursor.fetchall()
        
        conn.close()
        return customers
    
    def search_customers(self, search_term):
        """Müşteri arama"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM customers 
            WHERE name LIKE ? OR email LIKE ? OR phone LIKE ? OR company LIKE ?
            ORDER BY created_date DESC
        ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
        
        customers = cursor.fetchall()
        conn.close()
        return customers
    
    def update_customer(self, customer_id, name, email, phone, address, company, notes):
        """Müşteri bilgilerini günceller"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE customers 
            SET name=?, email=?, phone=?, address=?, company=?, notes=?
            WHERE id=?
        ''', (name, email, phone, address, company, notes, customer_id))
        
        conn.commit()
        conn.close()
    
    def delete_customer(self, customer_id):
        """Müşteriyi siler"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Önce müşterinin siparişlerini sil
        cursor.execute('DELETE FROM orders WHERE customer_id=?', (customer_id,))
        
        # Sonra müşteriyi sil
        cursor.execute('DELETE FROM customers WHERE id=?', (customer_id,))
        
        conn.commit()
        conn.close()
    
    def add_order(self, customer_id, product_name, quantity, price, start_date, end_date, status="Beklemede"):
        """Yeni sipariş ekler"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_price = quantity * price
        
        cursor.execute('''
            INSERT INTO orders (customer_id, order_date, start_date, end_date, product_name, quantity, price, total_price, status, notification_sent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
        ''', (customer_id, order_date, start_date, end_date, product_name, quantity, price, total_price, status))
        
        conn.commit()
        conn.close()
    
    def mark_notification_sent(self, order_id):
        """Bildirim gönderildi olarak işaretler"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('UPDATE orders SET notification_sent = 1 WHERE id = ?', (order_id,))
        
        conn.commit()
        conn.close()
        return cursor.lastrowid
    
    def update_order(self, order_id, product_name, quantity, price, start_date, end_date, status):
        """Siparişi günceller"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        total_price = quantity * price
        
        cursor.execute('''
            UPDATE orders 
            SET product_name = ?, quantity = ?, price = ?, total_price = ?, 
                start_date = ?, end_date = ?, status = ?
            WHERE id = ?
        ''', (product_name, quantity, price, total_price, start_date, end_date, status, order_id))
        
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
    def get_order_by_id(self, order_id):
        """ID'ye göre sipariş getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT o.*, c.name as customer_name 
            FROM orders o 
            JOIN customers c ON o.customer_id = c.id 
            WHERE o.id = ?
        ''', (order_id,))
        
        order = cursor.fetchone()
        conn.close()
        return order
    
    def get_customer_orders(self, customer_id):
        """Müşterinin siparişlerini getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM orders WHERE customer_id=? ORDER BY order_date DESC', (customer_id,))
        orders = cursor.fetchall()
        
        conn.close()
        return orders
    
    def search_orders(self, search_term):
        """Siparişleri arar"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        search_pattern = f"%{search_term}%"
        
        cursor.execute('''
            SELECT o.*, c.name as customer_name
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.product_name LIKE ? OR c.name LIKE ? OR o.status LIKE ?
            ORDER BY o.order_date DESC
        ''', (search_pattern, search_pattern, search_pattern))
        
        orders = cursor.fetchall()
        conn.close()
        return orders
    
    def get_all_orders(self):
        """Tüm siparişleri getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT o.*, c.name as customer_name
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            ORDER BY o.order_date DESC
        ''')
        
        orders = cursor.fetchall()
        conn.close()
        return orders
    
    def get_order_statistics(self):
        """Sipariş istatistiklerini getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM orders WHERE status != ?', ('İptal',))
        total_orders = cursor.fetchone()[0]
        
        cursor.execute('SELECT SUM(total_price) FROM orders WHERE status != ?', ('İptal',))
        total_revenue = cursor.fetchone()[0] or 0
        
        cursor.execute('SELECT COUNT(*) FROM orders WHERE status = ?', ('İptal',))
        cancelled_orders = cursor.fetchone()[0]
        
        cursor.execute('SELECT SUM(total_price) FROM orders WHERE status = ?', ('İptal',))
        cancelled_revenue = cursor.fetchone()[0] or 0
        
        cursor.execute('SELECT COUNT(*) FROM customers')
        total_customers = cursor.fetchone()[0]
        
        conn.close()
        return {
            'total_orders': total_orders,
            'total_revenue': total_revenue,
            'cancelled_orders': cancelled_orders,
            'cancelled_revenue': cancelled_revenue,
            'total_customers': total_customers
        }
    
    def get_expiring_orders(self):
        """Yaklaşan bitiş tarihi olan siparişleri getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Bugünden itibaren 7 gün içinde biten siparişler
        from datetime import datetime, timedelta
        today = datetime.now().date()
        week_later = today + timedelta(days=7)
        
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.quantity, o.price, o.total_price, 
                   o.start_date, o.end_date, o.status, o.notification_sent,
                   julianday(o.end_date) - julianday('now') as days_left
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.end_date BETWEEN ? AND ?
            AND o.status != 'Tamamlandı'
            AND o.status != 'İptal'
            ORDER BY o.end_date
        ''', (today.strftime("%Y-%m-%d"), week_later.strftime("%Y-%m-%d")))
        
        orders = cursor.fetchall()
        conn.close()
        return orders
    
    
    def get_overdue_orders(self):
        """Gecikmiş siparişleri getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        from datetime import datetime
        today = datetime.now().date()
        
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.quantity, o.price, o.total_price,
                   o.start_date, o.end_date, o.status, o.notification_sent,
                   julianday('now') - julianday(o.end_date) as days_overdue
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.end_date < ?
            AND o.status != 'Tamamlandı'
            AND o.status != 'İptal'
            ORDER BY o.end_date
        ''', (today.strftime("%Y-%m-%d"),))
        
        orders = cursor.fetchall()
        conn.close()
        return orders 
    
    def get_daily_payment_check(self):
        """Günlük ödeme kontrolü - tüm aktif siparişleri getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        from datetime import datetime, timedelta
        today = datetime.now().date()
        
        # Bugün biten siparişler
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.quantity, o.price, o.total_price, 
                   o.start_date, o.end_date, o.status, o.notification_sent,
                   julianday(o.end_date) - julianday('now') as days_left,
                   'Bugün Bitiş' as category
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.end_date = ?
            AND o.status != 'Tamamlandı'
            AND o.status != 'İptal'
            ORDER BY o.end_date
        ''', (today.strftime("%Y-%m-%d"),))
        
        today_orders = cursor.fetchall()
        
        # Yarın biten siparişler
        tomorrow = today + timedelta(days=1)
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.quantity, o.price, o.total_price, 
                   o.start_date, o.end_date, o.status, o.notification_sent,
                   julianday(o.end_date) - julianday('now') as days_left,
                   'Yarın Bitiş' as category
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.end_date = ?
            AND o.status != 'Tamamlandı'
            AND o.status != 'İptal'
            ORDER BY o.end_date
        ''', (tomorrow.strftime("%Y-%m-%d"),))
        
        tomorrow_orders = cursor.fetchall()
        
        # Bu hafta biten siparişler (3-7 gün)
        week_later = today + timedelta(days=7)
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.quantity, o.price, o.total_price, 
                   o.start_date, o.end_date, o.status, o.notification_sent,
                   julianday(o.end_date) - julianday('now') as days_left,
                   'Bu Hafta Bitiş' as category
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.end_date BETWEEN ? AND ?
            AND o.status != 'Tamamlandı'
            AND o.status != 'İptal'
            ORDER BY o.end_date
        ''', ((today + timedelta(days=2)).strftime("%Y-%m-%d"), week_later.strftime("%Y-%m-%d")))
        
        week_orders = cursor.fetchall()
        
        # Gecikmiş siparişler
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.quantity, o.price, o.total_price,
                   o.start_date, o.end_date, o.status, o.notification_sent,
                   julianday('now') - julianday(o.end_date) as days_overdue,
                   'Gecikmiş' as category
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.end_date < ?
            AND o.status != 'Tamamlandı'
            AND o.status != 'İptal'
            ORDER BY o.end_date
        ''', (today.strftime("%Y-%m-%d"),))
        
        overdue_orders = cursor.fetchall()
        
        conn.close()
        
        return {
            'today': today_orders,
            'tomorrow': tomorrow_orders,
            'week': week_orders,
            'overdue': overdue_orders
        }
    
    def complete_overdue_orders(self):
        """Sipariş tarihi geçen siparişlerin durumunu 'Tamamlandı' yapar"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        from datetime import datetime
        today = datetime.now().date()
        
        # Gecikmiş siparişleri bul
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.end_date, o.status
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.end_date < ?
            AND o.status != 'Tamamlandı'
            AND o.status != 'İptal'
            ORDER BY o.end_date
        ''', (today.strftime("%Y-%m-%d"),))
        
        overdue_orders = cursor.fetchall()
        
        # Durumlarını 'Tamamlandı' yap
        updated_count = 0
        for order in overdue_orders:
            order_id = order[0]
            cursor.execute('''
                UPDATE orders 
                SET status = 'Tamamlandı'
                WHERE id = ?
            ''', (order_id,))
            updated_count += 1
        
        conn.commit()
        conn.close()
        
        return {
            'updated_count': updated_count,
            'overdue_orders': overdue_orders
        }
    
    def get_completed_orders(self):
        """Tamamlanmış siparişleri getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT o.id, c.name, o.product_name, o.quantity, o.price, o.total_price,
                   o.start_date, o.end_date, o.status, o.notification_sent,
                   julianday('now') - julianday(o.end_date) as days_completed
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.status = 'Tamamlandı'
            ORDER BY o.end_date DESC
        ''')
        
        orders = cursor.fetchall()
        conn.close()
        return orders
    
    def reset_database(self):
        """Tüm verileri siler ve veritabanını sıfırlar"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            # Tüm tabloları temizle
            cursor.execute('DELETE FROM orders')
            cursor.execute('DELETE FROM customers')
            
            # Auto-increment sayaçlarını sıfırla
            cursor.execute('DELETE FROM sqlite_sequence WHERE name="customers"')
            cursor.execute('DELETE FROM sqlite_sequence WHERE name="orders"')
            
            conn.commit()
            return True
        except Exception as e:
            print(f"Veritabanı sıfırlama hatası: {e}")
            return False
        finally:
            conn.close()
    
    def update_order_status(self, order_id, new_status):
        """Sipariş durumunu günceller"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                UPDATE orders 
                SET status = ?
                WHERE id = ?
            ''', (new_status, order_id))
            
            conn.commit()
            return True
        except Exception as e:
            print(f"Sipariş durumu güncelleme hatası: {e}")
            return False
        finally:
            conn.close()
    
    def complete_selected_overdue_orders(self, order_ids):
        """Seçilen gecikmiş siparişlerin durumunu 'Tamamlandı' yapar"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            updated_count = 0
            completed_orders = []
            
            for order_id in order_ids:
                # Siparişin gecikmiş olup olmadığını kontrol et
                cursor.execute('''
                    SELECT o.id, c.name, o.product_name, o.end_date, o.status
                    FROM orders o
                    JOIN customers c ON o.customer_id = c.id
                    WHERE o.id = ? AND o.end_date < date('now')
                    AND o.status != 'Tamamlandı' AND o.status != 'İptal'
                ''', (order_id,))
                
                order = cursor.fetchone()
                if order:
                    # Siparişi tamamla
                    cursor.execute('''
                        UPDATE orders 
                        SET status = 'Tamamlandı'
                        WHERE id = ?
                    ''', (order_id,))
                    updated_count += 1
                    completed_orders.append(order)
            
            conn.commit()
            return {
                'updated_count': updated_count,
                'completed_orders': completed_orders
            }
            
        except Exception as e:
            print(f"Seçilen siparişleri tamamlama hatası: {e}")
            return {
                'updated_count': 0,
                'completed_orders': []
            }
        finally:
            conn.close()
    
    def get_orders_by_status(self, status):
        """Belirli durumdaki siparişleri getirir"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT o.*, c.name as customer_name
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            WHERE o.status = ?
            ORDER BY o.order_date DESC
        ''', (status,))
        
        orders = cursor.fetchall()
        conn.close()
        return orders
    
    def delete_all_data(self):
        """Tüm müşteri ve sipariş verilerini siler"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            # Önce siparişleri sil (foreign key constraint)
            cursor.execute('DELETE FROM orders')
            # Sonra müşterileri sil
            cursor.execute('DELETE FROM customers')
            # Auto increment counter'ları sıfırla
            cursor.execute('DELETE FROM sqlite_sequence WHERE name IN ("customers", "orders")')
            
            conn.commit()
            print("✅ Tüm veriler başarıyla silindi")
            
        except Exception as e:
            conn.rollback()
            print(f"❌ Veri silme hatası: {e}")
            raise
        finally:
            conn.close()