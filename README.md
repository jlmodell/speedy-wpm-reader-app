# optional: create a virtual environment (i use uv)

uv venv

# install dependencies

uv pip install pyperclip pyfiglet rich pyinstaller
-or-
uv pip install -r requirements.txt

# enter virtual environment

.venv/Scripts/activate

# code to generate single .exe

pyinstaller --onefile --console --add-data=".venv/Lib/site-packages/pyperclip;pyperclip" --add-data=".venv/Lib/site-packages/rich;rich" --add-data=".venv/Lib/site-packages/pyfiglet;pyfiglet" -n jeffs-speedy-wpm-reader-app.exe .\main.py
