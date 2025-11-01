# 🗄️ Database Backup Automation

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-green)
![Telegram](https://img.shields.io/badge/Telegram-Notifications-blue)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![CI](https://github.com/arminf83/database-backup/workflows/CI%20-%20Database%20Backup/badge.svg)

**Professional PostgreSQL database backup system with Telegram notifications and automatic cleanup**

[View Source](https://github.com/arminf83/database-backup) | 
[Report Bug](https://github.com/arminf83/database-backup/issues)

</div>

## ✨ Features

- ✅ **Automated PostgreSQL Backups** - Using pg_dump with custom format
- ✅ **Telegram Notifications** - Instant backup delivery to channels/groups
- ✅ **Automatic Cleanup** - Configurable retention policy
- ✅ **Environment Configuration** - Secure credential management
- ✅ **Comprehensive Logging** - Detailed operation logs
- ✅ **Error Handling** - Robust exception management
- ✅ **CI/CD Ready** - GitHub Actions integration

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL with pg_dump
- Telegram Bot Token

### Installation
```bash
git clone https://github.com/arminf83/database-backup.git
cd database-backup
pip install -r requirements.txt
