pyinstaller.exe --onefile --noconsol --name "Lembrete Sonoro" --icon=res/reminder.ico reminder.py

copy res dist
cd dist
mkdir res
move reminder.ico res
mkdir "Lembrete Sonoro"
move res "Lembrete Sonoro"
move "Lembrete Sonoro.exe" "Lembrete Sonoro"
cd ..
rd /s /q  __pycache__
rd /s /q build
rd dist
del "Lembrete Sonoro.spec"