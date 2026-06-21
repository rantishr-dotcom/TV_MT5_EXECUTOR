from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

folders = [
    "app",
    "app/api",
    "app/core",
    "app/database",
    "app/schemas",
    "dashboard",
    "exports",
    "logs",
    "mt5",
    "reports"
]

for folder in folders:
    (BASE / folder).mkdir(parents=True, exist_ok=True)

files = [
    "main.py",
    "START.bat",
    "app/api/__init__.py",
    "app/core/__init__.py",
    "app/database/__init__.py",
    "app/schemas/__init__.py",
]

for file in files:
    path = BASE / file
    path.touch(exist_ok=True)

print("Project structure created successfully!")