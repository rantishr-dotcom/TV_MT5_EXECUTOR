from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

main_code = '''
from fastapi import FastAPI

app = FastAPI(
    title="TV MT5 Executor",
    version="1.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "project": "TV MT5 Executor"
    }

@app.get("/health")
def health():
    return {
        "api": "running"
    }
'''

(BASE / "main.py").write_text(main_code)

start_bat = r'''
@echo off
call venv\Scripts\activate
uvicorn main:app --host 0.0.0.0 --port 8000
pause
'''

(BASE / "START.bat").write_text(start_bat)

print("main.py and START.bat created!")