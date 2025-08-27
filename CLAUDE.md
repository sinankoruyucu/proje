# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a customer management system for a dietitian (Diyetisyen Türkmen KURT). It's a desktop application built with Python, Tkinter for the GUI, and SQLite for data storage. The system manages customers, orders, payment tracking, and includes an automated notification system.

## Development Commands

### Running the Application
```bash
# Install dependencies
pip install -r requirements.txt

# Run the main application
python main.py

# Alternative: Use the batch file (Windows)
başlat.bat
```

### Building and Distribution
```bash
# Build EXE file using PyInstaller (automatically installs PyInstaller if missing)
python build_exe.py

# Manual PyInstaller installation if needed
pip install pyinstaller

# Install EXE package (after building)
EXE_KURULUM.bat

# Create installation package
KURULUM_PAKETI.bat

# Prepare distribution package
KURULUM_PAKETI_HAZIRLA.bat
```

### Testing
```bash
# Run database unit tests
python test_database.py

# Run GUI unit tests
python test_gui.py

# Run all tests with discovery
python -m unittest discover -v

# Run specific test class
python -m unittest test_database.TestCustomerDatabase -v
```

### Database Operations
```bash
# The database (customers.db) is automatically created when running main.py
# Database operations are handled through the CustomerDatabase class in database.py

# Reset database for testing
python -c "from database import CustomerDatabase; db = CustomerDatabase(); db.reset_database()"
```

## Architecture

### Core Components

**main.py** - Entry point that initializes the Tkinter window and starts the GUI
- Sets up 1400x800 window with minimum 800x600 size
- Handles Windows taskbar integration and icon setup
- Application lifecycle management with graceful shutdown confirmation

**gui.py** - Main GUI implementation using Tkinter with modern styling
- Tabbed interface with customer registration, orders, revenue tracking, and payment control
- Advanced caching system for performance optimization (customer_cache, order_cache)
- Date formatting utilities (DD.MM.YYYY ↔ YYYY-MM-DD conversion)
- Phone number validation and input sanitization
- Excel export functionality with OpenPyXL integration
- Modern TTK styling with custom button themes (Primary, Success, Warning)

**database.py** - Database layer using SQLite with automatic schema upgrades
- CustomerDatabase class manages all database operations with connection pooling
- Two main tables: customers and orders with proper foreign key relationships
- Automatic database migration system for schema updates
- Performance-optimized with database indexes on key columns
- Comprehensive CRUD operations with transaction safety

### Key Features

**Customer Management**
- Add, edit, delete, and search customers
- Fields: name, email, phone, address, company, notes

**Order Management** 
- Create and manage customer orders
- Track order dates, start/end dates, products, quantities, prices
- Order status tracking with notification system

**Payment Tracking**
- Automated checks for upcoming and overdue payments
- Visual notifications and message boxes

**Notification System**
- Background notification system that runs independently
- Uses Windows task scheduler for automation
- Visual alerts and message boxes (audio removed)

### File Structure
```
İLK PROJE/
├── main.py              # Application entry point
├── gui.py               # Tkinter GUI implementation
├── database.py          # SQLite database layer
├── build_exe.py         # PyInstaller build script
├── customers.db         # SQLite database file
├── requirements.txt     # Python dependencies
├── başlat.bat          # Application launcher
└── *.bat               # Installation and packaging scripts
```

## Database Schema

**customers table:**
- id (PRIMARY KEY), name, email, phone, address, company, created_date, notes

**orders table:**
- id (PRIMARY KEY), customer_id (FOREIGN KEY), order_date, start_date, end_date, product_name, quantity, price, total_price, status, notification_sent

## Dependencies

Core Python packages (from requirements.txt):
- tkcalendar==1.6.1 (calendar widget for date selection)
- pandas>=1.3.0 (Excel file operations)
- openpyxl>=3.0.0 (Excel file handling)
- pyodbc>=4.0.0 (SQL Server connectivity support)

Built-in modules used:
- tkinter (GUI framework)
- sqlite3 (database)
- datetime (date/time operations)
- threading (background operations)

## Development Notes

**Platform and Localization:**
- The application is designed for Windows environments
- Uses Turkish language for the user interface
- Windows taskbar integration with custom app ID

**Build and Deployment:**
- PyInstaller-based EXE generation with automatic dependency detection
- Automated installation and distribution system via batch files
- Icon fallback system (icon.ico → icon.png → default)

**Data Management:**
- Database migrations are handled automatically in database.py
- All dates stored in YYYY-MM-DD format internally, displayed as DD.MM.YYYY
- Comprehensive test coverage with unittest framework

**UI/UX Architecture:**
- Modern TTK styling with custom themes and color schemes
- Cache-based performance optimization for large datasets
- Tabbed interface with responsive design patterns

**Testing Framework:**
- Complete unit test suite for both database and GUI components
- Isolated test environments using temporary databases
- Mock-based GUI testing to avoid UI dependencies