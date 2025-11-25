# 🏥 Medical Dashboard

> Django admin panel for managing medical data from FastAPI backend

[![CI](https://github.com/aleks2008-dev/medical-dashboard-django/workflows/Django%20CI/badge.svg)](https://github.com/aleks2008-dev/medical-dashboard-django/actions)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://postgresql.org)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)

## 🎯 Project Overview

Medical Dashboard is a Django-based admin panel that provides a web interface for managing medical data stored in PostgreSQL. It integrates seamlessly with the FastAPI medical backend, offering read-only access to doctors, patients, appointments, and rooms data.

## 🏗️ Architecture

```
FastAPI Backend ←→ PostgreSQL ←→ Django Dashboard
     ↕                              ↕
Telegram Bot                   Web Admin Panel
```

## ✨ Features

- 👨⚕️ **Doctor Management** - View and search doctors by specialization
- 👥 **Patient Management** - Browse patient records and contact info
- 📅 **Appointment Tracking** - Monitor appointments with calendar view
- 🏠 **Room Management** - Track room availability and assignments
- 📊 **Statistics Dashboard** - Real-time metrics and analytics
- 🔍 **Advanced Filtering** - Search and filter across all data
- 📱 **Responsive Design** - Works on desktop and mobile

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- PostgreSQL (running FastAPI medical backend)
- Django 5.2+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aleks2008-dev/medical-dashboard.git
   cd medical-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database**
   - Ensure PostgreSQL is running with medical_db
   - Update settings.py if needed

4. **Create admin user**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**
   ```bash
   python manage.py runserver 8001
   ```

6. **Access the dashboard**
   - Admin Panel: http://localhost:8001/admin/
   - Statistics: http://localhost:8001/dashboard/stats/

## 📊 Dashboard Features

### Admin Panel
- **Doctors**: View specializations, experience, categories
- **Patients**: Browse user accounts and contact details
- **Appointments**: Track bookings with date filtering
- **Rooms**: Monitor room assignments

### Statistics Page
- Total counts for all entities
- Today's appointments
- Weekly appointment trends
- Popular medical specializations

## 🔧 Technical Details

### Models
- **Read-only access** to FastAPI database tables
- **UUID primary keys** matching FastAPI schema
- **Foreign key relationships** for data integrity

### Security
- **Staff-only access** to admin panel
- **Read-only permissions** prevent data corruption
- **Django authentication** system

## 🔗 Integration

This dashboard integrates with:
- **FastAPI Medical Backend** - Primary data source
- **Medical Telegram Bot** - Shared database
- **PostgreSQL Database** - Common data store

## 📁 Project Structure

```
medical-dashboard/
├── manage.py
├── requirements.txt
├── medical_dashboard/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── dashboard/
    ├── models.py          # Database models
    ├── admin.py           # Admin configuration
    ├── views.py           # Dashboard views
    └── templates/         # HTML templates
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 👨💻 Author

**Aleks** - [GitHub Profile](https://github.com/aleks2008-dev)

---

⭐ **Part of the Medical App Ecosystem:**
- [FastAPI Backend](https://github.com/aleks2008-dev/medical-app-fastapi)
- [Telegram Bot](https://github.com/aleks2008-dev/medical-telegram-bot)
- **Django Dashboard** (this project)