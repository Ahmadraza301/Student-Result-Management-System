# Student Result Management System

A comprehensive desktop application for managing student courses, results, and generating reports.

## Features

- **Course Management**: Add, edit, delete, and search courses
- **Student Management**: Manage student information and enrollment
- **Result Management**: Record and manage student results
- **Report Generation**: View results and export to PDF
- **Real-time Dashboard**: Live clock and statistics display

## Installation

### Prerequisites
- Python 3.7 or higher
- Windows 10/11 (tested)

### Setup
1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python dashboard.py
   ```

## Building Executable

### Quick Build (Windows)
1. Double-click `build.bat` to automatically build both executables
2. Find the executables in the `dist` folder

### Manual Build
1. Build dashboard:
   ```bash
   pyinstaller dashboard.spec
   ```
2. Build report:
   ```bash
   pyinstaller report.spec
   ```

## Usage

### Running from Source
- **Main Application**: `python dashboard.py`
- **Individual Modules**:
  - `python course.py` - Course management
  - `python student.py` - Student management
  - `python result.py` - Result management
  - `python report.py` - Report generation

### Running Executable
- Navigate to the `dist` folder
- Run `dashboard.exe` for the main application
- Run `report.exe` for report generation

## Database

The application uses SQLite database (`rms.db`) with the following tables:
- **course**: Course information (ID, name, duration, charges, description)
- **student**: Student details (roll, name, email, gender, DOB, contact, etc.)
- **result**: Student results (roll, name, course, marks, percentage)

## File Structure

```
SRM/
├── dashboard.py          # Main application
├── course.py            # Course management module
├── student.py           # Student management module
├── result.py            # Result management module
├── report.py            # Report generation module
├── create_db.py         # Database creation script
├── dashboard.spec       # PyInstaller spec for dashboard
├── report.spec          # PyInstaller spec for report
├── requirements.txt     # Python dependencies
├── build.bat           # Windows build script
├── images/             # Application images
├── rms.db              # SQLite database
└── dist/               # Built executables
```

## Troubleshooting

### Images Not Showing
- Ensure the `images` folder is in the same directory as the executable
- Check that image files exist and are not corrupted

### Database Errors
- Verify `rms.db` is in the same directory as the executable
- Run `python create_db.py` to recreate the database if needed

### Missing Dependencies
- Install required packages: `pip install -r requirements.txt`
- Ensure PyInstaller is installed: `pip install pyinstaller`

## Development

### Adding New Features
1. Modify the appropriate Python module
2. Update the spec file if new resources are added
3. Rebuild the executable using the build script

### Code Structure
- Each module is a separate class inheriting from tkinter
- Database connections use the `resource_path()` function for compatibility
- Error handling includes fallback options for missing resources

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure the database and images are properly included
