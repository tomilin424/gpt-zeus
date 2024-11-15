import sqlite3
from datetime import datetime, timedelta
import os

class Database:
    def __init__(self):
        # Удаляем старую базу данных если она существует
        if os.path.exists('bot_database.db'):
            os.remove('bot_database.db')
            
        self.conn = sqlite3.connect('bot_database.db', check_same_thread=False)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Таблица пользователей
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            subscription_type TEXT DEFAULT 'free',
            subscription_end DATE,
            gpt_requests_left INTEGER DEFAULT 5,
            image_requests_left INTEGER DEFAULT 2,
            balance INTEGER DEFAULT 0,
            total_spent INTEGER DEFAULT 0,
            referral_code TEXT UNIQUE,
            referred_by INTEGER,
            registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            auto_renewal BOOLEAN DEFAULT FALSE,
            payment_method TEXT,
            language TEXT DEFAULT 'ru',
            notifications_enabled BOOLEAN DEFAULT TRUE,
            crypto_address TEXT
        )
        ''')
        
        # Таблица транзакций
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount INTEGER,
            type TEXT,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        ''')
        
        # Таблица промокодов
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS promo_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            discount INTEGER,
            type TEXT,
            uses_left INTEGER,
            expires_at DATETIME,
            created_by INTEGER,
            FOREIGN KEY (created_by) REFERENCES users (user_id)
        )
        ''')
        
        # Таблица использованных промокодов
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS used_promo_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            promo_id INTEGER,
            used_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (promo_id) REFERENCES promo_codes (id)
        )
        ''')
        
        # Таблица использования моделей
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usage_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            model_type TEXT,
            prompt TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        ''')
        
        self.conn.commit()

    def get_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        return cursor.fetchone()

    def create_user(self, user_id, referred_by=None):
        cursor = self.conn.cursor()
        # Генерируем уникальный реферальный код
        ref_code = f"REF{user_id}{hash(str(datetime.now()))}"[:10]
        
        cursor.execute('''
        INSERT OR IGNORE INTO users 
        (user_id, referral_code, referred_by) 
        VALUES (?, ?, ?)
        ''', (user_id, ref_code, referred_by))
        
        if referred_by:
            # Начисляем бонус рефереру (например, 5 запросов)
            cursor.execute('''
            UPDATE users 
            SET gpt_requests_left = gpt_requests_left + 5 
            WHERE user_id = ?
            ''', (referred_by,))
            
        self.conn.commit()

    def get_user_by_ref_code(self, ref_code):
        cursor = self.conn.cursor()
        cursor.execute('SELECT user_id FROM users WHERE referral_code = ?', (ref_code,))
        result = cursor.fetchone()
        return result[0] if result else None

    def update_referrer(self, user_id, referrer_id):
        cursor = self.conn.cursor()
        cursor.execute('''
        UPDATE users 
        SET referred_by = ? 
        WHERE user_id = ?
        ''', (referrer_id, user_id))
        self.conn.commit()

db = Database() 