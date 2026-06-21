from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

folders = [
    "app",
    "app/api",
    "app/core",
    "app/database",
    "app/schemas",
    "app/services",
    "app/dashboard",
    "reports",
    "logs",
    "generators"
]

for folder in folders:
    (BASE / folder).mkdir(parents=True, exist_ok=True)

print("Folders created successfully.")