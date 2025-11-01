# database_backup.py
import os
import subprocess
import shutil
import requests
from datetime import datetime, timedelta
from pathlib import Path

from config import Config, setup_logging

class DatabaseBackup:
    """PostgreSQL database backup system with Telegram notifications"""
    
    def __init__(self):
        self.logger = setup_logging()
        self.backup_path = None
        
    def create_backup_directory(self):
        """Create backup directory with timestamp"""
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
        self.backup_path = Path(Config.BACKUP_DIR) / f"backup_{date_str}"
        self.backup_path.mkdir(parents=True, exist_ok=True)
        self.logger.info(f"Created backup directory: {self.backup_path}")
        return self.backup_path
    
    def backup_database(self):
        """Backup PostgreSQL database using pg_dump"""
        if not self.backup_path:
            raise ValueError("Backup directory not created")
            
        db_backup_file = self.backup_path / f"{Config.PG_DB}.dump"
        self.logger.info(f"Starting database backup to: {db_backup_file}")
        
        # Set password for pg_dump
        os.environ['PGPASSWORD'] = Config.PG_PASSWORD
        
        try:
            result = subprocess.run([
                "pg_dump",
                "-h", Config.PG_HOST,
                "-p", Config.PG_PORT,
                "-U", Config.PG_USER,
                "-F", "c",  # custom format
                "-b",       # include large objects
                "-v",       # verbose
                "-f", str(db_backup_file),
                Config.PG_DB
            ], capture_output=True, text=True, check=True)
            
            self.logger.info("Database backup completed successfully")
            return db_backup_file
            
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Database backup failed: {e.stderr}")
            raise
        finally:
            # Clear password from environment
            if 'PGPASSWORD' in os.environ:
                del os.environ['PGPASSWORD']
    
    def send_to_telegram(self, file_path):
        """Send backup file to Telegram channel"""
        self.logger.info("Sending backup to Telegram...")
        
        url = f"https://api.telegram.org/bot{Config.TELEGRAM_TOKEN}/sendDocument"
        
        try:
            with open(file_path, "rb") as file:
                response = requests.post(
                    url,
                    data={"chat_id": Config.TELEGRAM_CHAT_ID},
                    files={"document": file},
                    timeout=60  # 60 second timeout
                )
            
            if response.status_code == 200:
                self.logger.info("Backup file sent to Telegram successfully")
                return True
            else:
                self.logger.error(f"Telegram API error: {response.status_code} - {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to send to Telegram: {e}")
            return False
    
    def cleanup_old_backups(self):
        """Remove backups older than retention period"""
        self.logger.info(f"Cleaning up backups older than {Config.RETENTION_DAYS} days")
        
        cutoff = datetime.now() - timedelta(days=Config.RETENTION_DAYS)
        backup_dir = Path(Config.BACKUP_DIR)
        
        if not backup_dir.exists():
            self.logger.warning("Backup directory does not exist")
            return
        
        removed_count = 0
        for item in backup_dir.iterdir():
            if item.is_dir() and item.name.startswith("backup_"):
                try:
                    # Extract timestamp from folder name
                    time_str = item.name.replace("backup_", "")
                    folder_time = datetime.strptime(time_str, "%Y-%m-%d_%H-%M-%S")
                    
                    if folder_time < cutoff:
                        shutil.rmtree(item)
                        self.logger.info(f"Removed old backup: {item}")
                        removed_count += 1
                        
                except ValueError as e:
                    self.logger.warning(f"Could not parse backup folder time: {item.name} - {e}")
                except Exception as e:
                    self.logger.error(f"Failed to remove backup: {item} - {e}")
        
        self.logger.info(f"Cleanup completed: {removed_count} old backups removed")
    
    def run(self):
        """Main backup execution flow"""
        try:
            self.logger.info("Starting database backup process")
            
            # Validate configuration
            Config.validate()
            
            # Create backup directory
            self.create_backup_directory()
            
            # Perform database backup
            backup_file = self.backup_database()
            
            # Send to Telegram
            telegram_success = self.send_to_telegram(backup_file)
            
            # Cleanup old backups
            self.cleanup_old_backups()
            
            self.logger.info("Database backup process completed successfully")
            return True, telegram_success
            
        except Exception as e:
            self.logger.error(f"Backup process failed: {e}")
            return False, False

def main():
    """Main entry point"""
    backup_system = DatabaseBackup()
    success, telegram_sent = backup_system.run()
    
    exit_code = 0 if success else 1
    exit(exit_code)

if __name__ == "__main__":
    main()

