pyinstaller.exe --onefile --noconsol --name "Lembrete Sonoro" --icon=res/reminder.ico reminder.py

mkdir "Lembrete Sonoro/res"
move "dist\Lembrete Sonoro.exe" "Lembrete Sonoro"
copy "res" "Lembrete Sonoro/res"
rd /s /q  __pycache__
rd /s /q build
rd /s /q dist
del "Lembrete Sonoro.spec"
