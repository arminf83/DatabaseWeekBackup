# config.py
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for database backup system"""
    
    # PostgreSQL Configuration
    PG_USER = os.getenv("PG_USER")
    PG_PASSWORD = os.getenv("PG_PASSWORD")
    PG_HOST = os.getenv("PG_HOST", "localhost")
    PG_PORT = os.getenv("PG_PORT", "5432")
    PG_DB = os.getenv("PG_DB")
    
    # Backup Configuration
    BACKUP_DIR = os.getenv("BACKUP_DIR", "./backups")
    RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "7"))
    
    # Telegram Configuration
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls):
        """Validate required environment variables"""
        required_vars = {
            "PG_USER": cls.PG_USER,
            "PG_PASSWORD": cls.PG_PASSWORD,
            "PG_DB": cls.PG_DB,
            "BACKUP_DIR": cls.BACKUP_DIR,
            "TELEGRAM_TOKEN": cls.TELEGRAM_TOKEN,
            "TELEGRAM_CHAT_ID": cls.TELEGRAM_CHAT_ID
        }
        
        missing = [var for var, value in required_vars.items() if not value]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=Config.LOG_LEVEL,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

