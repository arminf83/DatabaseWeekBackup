# 🗄️ Database Backup Automation | سیستم بکاپ خودکار دیتابیس

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-green)
![Telegram](https://img.shields.io/badge/Telegram-Notifications-blue)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![CI](https://img.shields.io/badge/Automation-CI%2FCD%20Ready-orange)

**Professional PostgreSQL database backup system with Telegram notifications and automatic cleanup**
**سیستم حرفه‌ای بکاپ خودکار PostgreSQL با ارسال اعلان در تلگرام و پاک‌سازی هوشمند نسخه‌های قدیمی**

[📄 View Source](https://github.com/yourusername/database-backup) •
[🐞 Report Bug](https://github.com/yourusername/database-backup/issues) •
[💬 Contact Developer](mailto:your@email.com)

</div>

---

## ✨ Features | ویژگی‌ها

* ✅ **Automated PostgreSQL Backups** — Using `pg_dump` with custom format
  بکاپ‌گیری خودکار از دیتابیس PostgreSQL با فرمت سفارشی
* ✅ **Telegram Notifications** — Instant file delivery to Telegram
  ارسال مستقیم فایل بکاپ به تلگرام
* ✅ **Automatic Cleanup** — Smart retention management
  پاک‌سازی خودکار نسخه‌های قدیمی
* ✅ **Secure Environment Config** — via `.env`
  پیکربندی ایمن اطلاعات دیتابیس و توکن تلگرام
* ✅ **Comprehensive Logging** — Full activity tracking
  ثبت کامل رویدادها و خطاها
* ✅ **CI/CD Ready** — Perfect for automated deployments
  آماده برای استقرار خودکار در سرور
* ✅ **Cross-platform** — Works on Linux / macOS / Windows
  قابل اجرا در سیستم‌عامل‌های مختلف

---

## ⚙️ Project Structure | ساختار پروژه

```
database-backup/
│
├── config.py              # Environment & logging configuration
├── database_backup.py     # Core backup logic and automation
├── .env.example           # Sample environment configuration
├── requirements.txt       # Python dependencies
└── backups/               # Backup storage directory
```

---

## 🚀 Quick Start | شروع سریع

### Prerequisites | پیش‌نیازها

* Python **3.8+**
* PostgreSQL client (`pg_dump`)
* Telegram bot token

### Installation | نصب

```bash
git clone https://github.com/yourusername/database-backup.git
cd database-backup
pip install -r requirements.txt
```

### Configuration | تنظیمات

Create a `.env` file in the root directory:

```bash
# PostgreSQL Configuration
PG_USER=postgres
PG_PASSWORD=yourpassword
PG_HOST=localhost
PG_PORT=5432
PG_DB=your_database_name

# Backup Settings
BACKUP_DIR=./backups
RETENTION_DAYS=7

# Telegram
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Logging
LOG_LEVEL=INFO
```

---

## ▶️ Usage | نحوه اجرا

### Manual Run | اجرای دستی

```bash
python3 database_backup.py
```

### Scheduled Run (CronJob) | اجرای زمان‌بندی‌شده

برای اجرای خودکار روزانه در ساعت ۲ بامداد:

```bash
crontab -e
```

افزودن خط زیر:

```
0 2 * * * /usr/bin/python3 /path/to/project/database_backup.py >> /path/to/project/backup.log 2>&1
```

---

## 📊 Logging | سیستم لاگ

تمامی مراحل (بکاپ، ارسال، پاک‌سازی) با جزئیات ثبت می‌شوند.
سطح لاگ از طریق `.env` قابل تغییر است (`INFO`, `DEBUG`, `ERROR`).

All processes (backup, send, cleanup) are logged in detail.
You can control verbosity using the `LOG_LEVEL` variable.

---

## 🧼 Cleanup | پاک‌سازی خودکار

بکاپ‌هایی که قدیمی‌تر از مقدار تعیین‌شده در `RETENTION_DAYS` باشند به‌صورت خودکار حذف می‌شوند.
Backups older than the retention period are automatically removed to save disk space.

---

## 🤖 Telegram Integration | اتصال به تلگرام

با تنظیم `TELEGRAM_TOKEN` و `TELEGRAM_CHAT_ID` در `.env`، فایل بکاپ به‌صورت خودکار به چت مشخص‌شده ارسال می‌شود.
Using Telegram Bot API, the backup file is automatically sent to the defined chat or channel.

---

## 🧩 Example Output | خروجی نمونه

```
2025-11-06 02:00:01 - INFO - Starting database backup process
2025-11-06 02:00:02 - INFO - Created backup directory: ./backups/backup_2025-11-06_02-00-02
2025-11-06 02:00:10 - INFO - Backup file sent to Telegram successfully
2025-11-06 02:00:12 - INFO - Cleanup completed: 1 old backup removed
```

---

## 👨‍💻 Author | توسعه‌دهنده

Developed by **[Armin Fazely](https://github.com/arminf83)**
Cybersecurity & Python Automation Engineer

Created with ❤️ for automated PostgreSQL server management.
ساخته شده با ❤️ برای اتوماسیون پشتیبان‌گیری دیتابیس در سرورهای PostgreSQL.

---

## 🛡️ License | مجوز

Distributed under the **MIT License** — free for personal and commercial use.
منتشرشده تحت مجوز **MIT** — قابل استفاده آزاد برای مصارف شخصی و تجاری.

---
