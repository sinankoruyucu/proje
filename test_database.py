"""
Diyetisyen Müşteri Yönetim Sistemi - Veritabanı Unit Testleri

Bu dosya CustomerDatabase sınıfının tüm fonksiyonlarını test eder.
"""

import unittest
import sqlite3
import os
import tempfile
from datetime import datetime, timedelta
from database import CustomerDatabase


class TestCustomerDatabase(unittest.TestCase):
    """CustomerDatabase sınıfı için unit testler"""
    
    def setUp(self):
        """Her test öncesi çalışır - geçici test veritabanı oluşturur"""
        # Geçici dosya oluştur
        self.test_db_fd, self.test_db_path = tempfile.mkstemp(suffix='.db')
        os.close(self.test_db_fd)
        
        # Test veritabanı oluştur
        self.db = CustomerDatabase(self.test_db_path)
    
    def tearDown(self):
        """Her test sonrası çalışır - geçici veritabanını siler"""
        if os.path.exists(self.test_db_path):
            os.unlink(self.test_db_path)
    
    def test_database_creation(self):
        """Veritabanı ve tabloların düzgün oluşturulduğunu test eder"""
        # Veritabanı dosyasının var olduğunu kontrol et
        self.assertTrue(os.path.exists(self.test_db_path))
        
        # Tabloların var olduğunu kontrol et
        conn = sqlite3.connect(self.test_db_path)
        cursor = conn.cursor()
        
        # customers tablosu
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='customers'")
        self.assertIsNotNone(cursor.fetchone())
        
        # orders tablosu
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        self.assertIsNotNone(cursor.fetchone())
        
        conn.close()
    
    def test_add_customer(self):
        """Müşteri ekleme fonksiyonunu test eder"""
        # Müşteri ekle
        customer_id = self.db.add_customer(
            name="Test Müşteri",
            email="test@example.com",
            phone="0555-123-4567",
            address="Test Adres",
            company="Test Şirket",
            notes="Test not"
        )
        
        # ID'nin döndürüldüğünü kontrol et
        self.assertIsNotNone(customer_id)
        self.assertIsInstance(customer_id, int)
        
        # Müşterinin veritabanına eklendiğini kontrol et
        customers = self.db.get_all_customers()
        self.assertEqual(len(customers), 1)
        
        customer = customers[0]
        self.assertEqual(customer[1], "Test Müşteri")  # name
        self.assertEqual(customer[2], "test@example.com")  # email
        self.assertEqual(customer[3], "0555-123-4567")  # phone
    
    def test_duplicate_customer_name(self):
        """Aynı isimde müşteri eklemeye çalışınca hata fırlatması gerekir"""
        # İlk müşteri
        self.db.add_customer("Test Müşteri", "test1@example.com", "123", "Adres1", "Şirket1", "Not1")
        
        # Aynı isimde ikinci müşteri - hata fırlatmalı
        with self.assertRaises(ValueError):
            self.db.add_customer("Test Müşteri", "test2@example.com", "456", "Adres2", "Şirket2", "Not2")
    
    def test_search_customers(self):
        """Müşteri arama fonksiyonunu test eder"""
        # Test müşterileri ekle
        self.db.add_customer("Ali Yılmaz", "ali@example.com", "0555-111-1111", "İstanbul", "ABC Şirket", "Not1")
        self.db.add_customer("Ayşe Demir", "ayse@example.com", "0555-222-2222", "Ankara", "XYZ Şirket", "Not2")
        self.db.add_customer("Mehmet Kaya", "mehmet@test.com", "0555-333-3333", "İzmir", "ABC Şirket", "Not3")
        
        # İsimle arama
        results = self.db.search_customers("Ali")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "Ali Yılmaz")
        
        # Email ile arama
        results = self.db.search_customers("test.com")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "Mehmet Kaya")
        
        # Şirket ile arama
        results = self.db.search_customers("ABC")
        self.assertEqual(len(results), 2)
        
        # Bulunamayan arama
        results = self.db.search_customers("Bulunamaz")
        self.assertEqual(len(results), 0)
    
    def test_update_customer(self):
        """Müşteri güncelleme fonksiyonunu test eder"""
        # Müşteri ekle
        customer_id = self.db.add_customer("Eski Ad", "eski@example.com", "111", "Eski Adres", "Eski Şirket", "Eski Not")
        
        # Müşteriyi güncelle
        self.db.update_customer(
            customer_id, 
            "Yeni Ad", 
            "yeni@example.com", 
            "222", 
            "Yeni Adres", 
            "Yeni Şirket", 
            "Yeni Not"
        )
        
        # Güncellemenin başarılı olduğunu kontrol et
        customers = self.db.get_all_customers()
        customer = customers[0]
        self.assertEqual(customer[1], "Yeni Ad")
        self.assertEqual(customer[2], "yeni@example.com")
        self.assertEqual(customer[3], "222")
    
    def test_delete_customer(self):
        """Müşteri silme fonksiyonunu test eder"""
        # Müşteri ve sipariş ekle
        customer_id = self.db.add_customer("Silinecek Müşteri", "sil@example.com", "111", "Adres", "Şirket", "Not")
        order_id = self.db.add_order(customer_id, "Test Ürün", 2, 100.0, "2024-01-01", "2024-01-08")
        
        # Müşteriyi sil
        self.db.delete_customer(customer_id)
        
        # Müşterinin silindiğini kontrol et
        customers = self.db.get_all_customers()
        self.assertEqual(len(customers), 0)
        
        # Siparişlerin de silindiğini kontrol et
        orders = self.db.get_all_orders()
        self.assertEqual(len(orders), 0)
    
    def test_add_order(self):
        """Sipariş ekleme fonksiyonunu test eder"""
        # Önce müşteri ekle
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        
        # Sipariş ekle
        order_id = self.db.add_order(
            customer_id=customer_id,
            product_name="Test Ürün",
            quantity=3,
            price=150.0,
            start_date="2024-01-01",
            end_date="2024-01-15",
            status="Beklemede"
        )
        
        # Siparişin eklendiğini kontrol et
        self.assertIsNotNone(order_id)
        
        orders = self.db.get_all_orders()
        self.assertEqual(len(orders), 1)
        
        order = orders[0]
        self.assertEqual(order[5], "Test Ürün")  # product_name
        self.assertEqual(order[6], 3)  # quantity
        self.assertEqual(order[7], 150.0)  # price
        self.assertEqual(order[8], 450.0)  # total_price (3 * 150)
    
    def test_update_order(self):
        """Sipariş güncelleme fonksiyonunu test eder"""
        # Müşteri ve sipariş ekle
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        order_id = self.db.add_order(customer_id, "Eski Ürün", 1, 100.0, "2024-01-01", "2024-01-08")
        
        # Siparişi güncelle
        result = self.db.update_order(
            order_id=order_id,
            product_name="Yeni Ürün",
            quantity=2,
            price=200.0,
            start_date="2024-02-01",
            end_date="2024-02-15",
            status="Devam Ediyor"
        )
        
        # Güncellemenin başarılı olduğunu kontrol et
        self.assertTrue(result)
        
        order = self.db.get_order_by_id(order_id)
        self.assertEqual(order[5], "Yeni Ürün")
        self.assertEqual(order[6], 2)
        self.assertEqual(order[7], 200.0)
        self.assertEqual(order[8], 400.0)  # 2 * 200
    
    def test_search_orders(self):
        """Sipariş arama fonksiyonunu test eder"""
        # Test verisi hazırla
        customer_id1 = self.db.add_customer("Ali Yılmaz", "ali@example.com", "111", "Adres1", "Şirket1", "Not1")
        customer_id2 = self.db.add_customer("Ayşe Demir", "ayse@example.com", "222", "Adres2", "Şirket2", "Not2")
        
        self.db.add_order(customer_id1, "Vitamin D", 1, 50.0, "2024-01-01", "2024-01-08")
        self.db.add_order(customer_id2, "Kalsiyum", 2, 75.0, "2024-01-02", "2024-01-09")
        self.db.add_order(customer_id1, "Magnezyum", 1, 60.0, "2024-01-03", "2024-01-10", "Tamamlandı")
        
        # Ürün adıyla arama
        results = self.db.search_orders("Vitamin")
        self.assertEqual(len(results), 1)
        
        # Müşteri adıyla arama
        results = self.db.search_orders("Ali")
        self.assertEqual(len(results), 2)
        
        # Durumla arama
        results = self.db.search_orders("Tamamlandı")
        self.assertEqual(len(results), 1)
    
    def test_get_order_statistics(self):
        """Sipariş istatistikleri fonksiyonunu test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        
        self.db.add_order(customer_id, "Ürün1", 2, 100.0, "2024-01-01", "2024-01-08")
        self.db.add_order(customer_id, "Ürün2", 1, 150.0, "2024-01-02", "2024-01-09")
        
        # İstatistikleri al
        stats = self.db.get_order_statistics()
        
        self.assertEqual(stats['total_orders'], 2)
        self.assertEqual(stats['total_revenue'], 350.0)  # (2*100) + (1*150)
        self.assertEqual(stats['total_customers'], 1)
    
    def test_get_order_statistics_with_cancelled_orders(self):
        """İptal edilmiş siparişlerin gelire dahil olmadığını test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        
        # Normal siparişler
        order_id1 = self.db.add_order(customer_id, "Ürün1", 2, 100.0, "2024-01-01", "2024-01-08", "Beklemede")
        order_id2 = self.db.add_order(customer_id, "Ürün2", 1, 150.0, "2024-01-02", "2024-01-09", "Tamamlandı")
        
        # İptal edilmiş sipariş
        order_id3 = self.db.add_order(customer_id, "Ürün3", 3, 200.0, "2024-01-03", "2024-01-10", "İptal")
        
        # İstatistikleri al
        stats = self.db.get_order_statistics()
        
        # İptal edilmiş sipariş sayılmamalı (sadece 2 sipariş)
        self.assertEqual(stats['total_orders'], 2)
        # İptal edilmiş sipariş gelire dahil olmamalı (200*3=600 TL hariç)
        self.assertEqual(stats['total_revenue'], 350.0)  # (2*100) + (1*150)
        # İptal edilmiş sipariş tutarı ayrı hesaplanmalı
        self.assertEqual(stats['cancelled_revenue'], 600.0)  # 3*200
        self.assertEqual(stats['cancelled_orders'], 1)
        self.assertEqual(stats['total_customers'], 1)
    
    def test_get_expiring_orders(self):
        """Yaklaşan bitiş tarihi olan siparişleri test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        
        # Bugünden 3 gün sonra bitecek sipariş
        future_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
        self.db.add_order(customer_id, "Yaklaşan Ürün", 1, 100.0, "2024-01-01", future_date)
        
        # Çok gelecekte bitecek sipariş (test kapsamı dışında)
        far_future = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        self.db.add_order(customer_id, "Uzak Ürün", 1, 100.0, "2024-01-01", far_future)
        
        # Yaklaşan siparişleri al
        expiring = self.db.get_expiring_orders()
        
        # En az 1 sipariş olmalı (3 gün sonra biten)
        self.assertGreaterEqual(len(expiring), 1)
        
        # İlk siparişin yaklaşan olduğunu kontrol et
        self.assertEqual(expiring[0][2], "Yaklaşan Ürün")
    
    def test_get_overdue_orders(self):
        """Gecikmiş siparişleri test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        
        # Geçmişte biten sipariş (gecikmiş)
        past_date = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        self.db.add_order(customer_id, "Gecikmiş Ürün", 1, 100.0, "2024-01-01", past_date, "Beklemede")
        
        # Normal sipariş
        future_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
        self.db.add_order(customer_id, "Normal Ürün", 1, 100.0, "2024-01-01", future_date, "Beklemede")
        
        # Gecikmiş siparişleri al
        overdue = self.db.get_overdue_orders()
        
        # 1 gecikmiş sipariş olmalı
        self.assertEqual(len(overdue), 1)
        self.assertEqual(overdue[0][2], "Gecikmiş Ürün")
    
    def test_update_order_status(self):
        """Sipariş durumu güncelleme fonksiyonunu test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        order_id = self.db.add_order(customer_id, "Test Ürün", 1, 100.0, "2024-01-01", "2024-01-08", "Beklemede")
        
        # Durumu güncelle
        result = self.db.update_order_status(order_id, "Tamamlandı")
        self.assertTrue(result)
        
        # Güncellemenin başarılı olduğunu kontrol et
        order = self.db.get_order_by_id(order_id)
        self.assertEqual(order[9], "Tamamlandı")
    
    def test_mark_notification_sent(self):
        """Bildirim gönderildi işaretleme fonksiyonunu test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        order_id = self.db.add_order(customer_id, "Test Ürün", 1, 100.0, "2024-01-01", "2024-01-08")
        
        # Bildirimi işaretle
        self.db.mark_notification_sent(order_id)
        
        # İşaretlemenin başarılı olduğunu kontrol et
        order = self.db.get_order_by_id(order_id)
        self.assertEqual(order[10], 1)  # notification_sent
    
    def test_reset_database(self):
        """Veritabanı sıfırlama fonksiyonunu test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        self.db.add_order(customer_id, "Test Ürün", 1, 100.0, "2024-01-01", "2024-01-08")
        
        # Veri olduğunu kontrol et
        self.assertEqual(len(self.db.get_all_customers()), 1)
        self.assertEqual(len(self.db.get_all_orders()), 1)
        
        # Veritabanını sıfırla
        result = self.db.reset_database()
        self.assertTrue(result)
        
        # Verilerin silindiğini kontrol et
        self.assertEqual(len(self.db.get_all_customers()), 0)
        self.assertEqual(len(self.db.get_all_orders()), 0)
    
    def test_get_orders_by_status(self):
        """Duruma göre sipariş listeleme fonksiyonunu test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        
        self.db.add_order(customer_id, "Ürün1", 1, 100.0, "2024-01-01", "2024-01-08", "Beklemede")
        self.db.add_order(customer_id, "Ürün2", 1, 100.0, "2024-01-02", "2024-01-09", "Tamamlandı")
        self.db.add_order(customer_id, "Ürün3", 1, 100.0, "2024-01-03", "2024-01-10", "Beklemede")
        
        # Beklemede olan siparişleri al
        pending_orders = self.db.get_orders_by_status("Beklemede")
        self.assertEqual(len(pending_orders), 2)
        
        # Tamamlanan siparişleri al  
        completed_orders = self.db.get_orders_by_status("Tamamlandı")
        self.assertEqual(len(completed_orders), 1)
    
    def test_daily_payment_check(self):
        """Günlük ödeme kontrolü fonksiyonunu test eder"""
        # Test verisi hazırla
        customer_id = self.db.add_customer("Test Müşteri", "test@example.com", "111", "Adres", "Şirket", "Not")
        
        # Bugün biten sipariş
        today = datetime.now().strftime("%Y-%m-%d")
        self.db.add_order(customer_id, "Bugün Biten", 1, 100.0, "2024-01-01", today, "Beklemede")
        
        # Yarın biten sipariş
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.db.add_order(customer_id, "Yarın Biten", 1, 100.0, "2024-01-01", tomorrow, "Beklemede")
        
        # Gecikmiş sipariş
        past_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
        self.db.add_order(customer_id, "Gecikmiş", 1, 100.0, "2024-01-01", past_date, "Beklemede")
        
        # Günlük kontrol
        result = self.db.get_daily_payment_check()
        
        # Sonuçları kontrol et
        self.assertIn('today', result)
        self.assertIn('tomorrow', result) 
        self.assertIn('overdue', result)
        
        self.assertEqual(len(result['today']), 1)
        self.assertEqual(len(result['tomorrow']), 1)
        self.assertEqual(len(result['overdue']), 1)


class TestDatabaseIntegration(unittest.TestCase):
    """Veritabanı entegrasyon testleri"""
    
    def setUp(self):
        """Test öncesi hazırlık"""
        self.test_db_fd, self.test_db_path = tempfile.mkstemp(suffix='.db')
        os.close(self.test_db_fd)
        self.db = CustomerDatabase(self.test_db_path)
    
    def tearDown(self):
        """Test sonrası temizlik"""
        if os.path.exists(self.test_db_path):
            os.unlink(self.test_db_path)
    
    def test_complete_workflow(self):
        """Tam iş akışı testi - müşteri ekleme, sipariş oluşturma, güncelleme"""
        # 1. Müşteri ekle
        customer_id = self.db.add_customer(
            "Ahmet Yılmaz", 
            "ahmet@example.com", 
            "0555-123-4567", 
            "İstanbul, Beşiktaş", 
            "ABC Şirket", 
            "VIP müşteri"
        )
        
        # 2. Sipariş ekle
        order_id = self.db.add_order(
            customer_id=customer_id,
            product_name="D3 Vitamini",
            quantity=2,
            price=120.0,
            start_date="2024-01-01",
            end_date="2024-01-30",
            status="Devam Ediyor"
        )
        
        # 3. Müşteri bilgilerini güncelle
        self.db.update_customer(
            customer_id, 
            "Ahmet Yılmaz", 
            "ahmet.yilmaz@newmail.com", 
            "0555-123-4567", 
            "İstanbul, Beşiktaş", 
            "ABC Şirket", 
            "VIP müşteri - güncellendi"
        )
        
        # 4. Sipariş durumunu güncelle
        self.db.update_order_status(order_id, "Tamamlandı")
        
        # 5. Sonuçları kontrol et
        customers = self.db.get_all_customers()
        orders = self.db.get_all_orders()
        
        self.assertEqual(len(customers), 1)
        self.assertEqual(len(orders), 1)
        
        # Güncellenen müşteri bilgileri
        customer = customers[0]
        self.assertEqual(customer[2], "ahmet.yilmaz@newmail.com")
        self.assertIn("güncellendi", customer[7])  # notes
        
        # Güncellenen sipariş durumu
        order = orders[0]
        self.assertEqual(order[9], "Tamamlandı")  # status


if __name__ == '__main__':
    # Test suite oluştur
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Test sınıflarını ekle
    suite.addTests(loader.loadTestsFromTestCase(TestCustomerDatabase))
    suite.addTests(loader.loadTestsFromTestCase(TestDatabaseIntegration))
    
    # Testleri çalıştır
    runner = unittest.TextTestRunner(verbosity=2)
    print("=" * 70)
    print("Diyetisyen Müşteri Yönetim Sistemi - Veritabanı Unit Testleri")
    print("=" * 70)
    result = runner.run(suite)
    
    # Sonuçları özetle
    print("\n" + "=" * 70)
    print("TEST SONUÇLARI:")
    print(f"Toplam test: {result.testsRun}")
    print(f"Başarılı: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Başarısız: {len(result.failures)}")
    print(f"Hata: {len(result.errors)}")
    print("=" * 70)
    
    if result.failures:
        print("\nBAŞARISIZ TESTLER:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nHATA VEREN TESTLER:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")