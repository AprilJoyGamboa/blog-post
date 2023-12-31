@echo off

:: Flush the database
python manage.py flush --noinput

:: Delete the SQLite database file
del /q /s /f db.sqlite3

:: Delete existing migrations
rmdir /q /s blogs\migrations

:: Delete media files
rmdir /q /s media\blog_images

:: Execute additional commands or run another batch file
:: For example, you can run script.bat here
call script.bat

:: Pause to keep the console window open (optional)
@REM pause
