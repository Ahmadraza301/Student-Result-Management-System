@echo off
echo ========================================
echo   Creating Release Package
echo ========================================
echo.

set VERSION=1.0
set RELEASE_NAME=StudentRMS-v%VERSION%

echo Step 1: Building executables...
call build.bat

echo.
echo Step 2: Creating release folder...
if exist "release" rmdir /s /q "release"
mkdir "release\%RELEASE_NAME%"

echo.
echo Step 3: Copying files...
xcopy "dist\dashboard.exe" "release\%RELEASE_NAME%\" /Y
xcopy "dist\report.exe" "release\%RELEASE_NAME%\" /Y
xcopy "dist\LAUNCHER.bat" "release\%RELEASE_NAME%\" /Y
xcopy "dist\rms.db" "release\%RELEASE_NAME%\" /Y
xcopy "dist\README.md" "release\%RELEASE_NAME%\" /Y
xcopy "dist\USER_GUIDE.md" "release\%RELEASE_NAME%\" /Y
xcopy "dist\images\*" "release\%RELEASE_NAME%\images\" /E /I /Y

echo.
echo Step 4: Creating ZIP archive...
powershell Compress-Archive -Path "release\%RELEASE_NAME%\*" -DestinationPath "release\%RELEASE_NAME%.zip" -Force

echo.
echo ========================================
echo   Release package created!
echo   Location: release\%RELEASE_NAME%.zip
echo ========================================
echo.
echo You can now:
echo 1. Upload to GitHub Releases
echo 2. Share via Google Drive/Dropbox
echo 3. Host on your website
echo.
pause
