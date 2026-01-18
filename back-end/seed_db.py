"""
Database seed script using direct SQL execution
Run this script to populate the database with comprehensive test data in Kenyan Shillings
"""
import asyncio
import psycopg2
import json
import os
from datetime import datetime

# Connection string - adjust as needed
DB_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@turntable.proxy.rlwy.net:5432/railway')

def parse_db_url(url):
    """Parse PostgreSQL URL"""
    # postgresql://user:password@host:port/dbname
    parts = url.replace('postgresql://', '').split('@')
    credentials = parts[0].split(':')
    host_port = parts[1].split('/')
    return {
        'user': credentials[0],
        'password': credentials[1],
        'host': host_port[0].split(':')[0],
        'port': int(host_port[0].split(':')[1]) if ':' in host_port[0] else 5432,
        'database': host_port[1]
    }

def seed_database():
    try:
        config = parse_db_url(DB_URL)
        print(f"Connecting to database at {config['host']}:{config['port']}...")
        
        conn = psycopg2.connect(
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port=config['port'],
            database=config['database'],
            sslmode='require'
        )
        cursor = conn.cursor()
        print("✅ Connected to database")
        
        # Read and execute SQL script
        with open('/home/alex/My_Projects/petbloom-frontend/back-end/seed.sql', 'r') as f:
            sql_script = f.read()
        
        # Execute the script
        cursor.execute(sql_script)
        conn.commit()
        
        # Count records
        cursor.execute('SELECT COUNT(*) FROM "Pet"')
        pet_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM "Product"')
        product_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM "Review"')
        review_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM "Message"')
        message_count = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        print("\n" + "="*60)
        print("✅ DATABASE SEEDED SUCCESSFULLY!")
        print("="*60)
        print(f"   📊 SUMMARY:")
        print(f"   🐕 Pets: {pet_count}")
        print(f"      - Dogs: 5")
        print(f"      - Cats: 5")
        print(f"   📦 Products: {product_count}")
        print(f"      - Food: 5")
        print(f"      - Toys: 5")
        print(f"      - Habitats: 2")
        print(f"      - Accessories: 2")
        print(f"      - Grooming: 2")
        print(f"   ⭐ Reviews: {review_count}")
        print(f"   💬 Messages: {message_count}")
        print("="*60)
        print("💰 Currency: All prices in Kenyan Shillings (KES)")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    seed_database()
