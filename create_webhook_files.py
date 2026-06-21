from pathlib import Path

BASE = Path(r"C:\Users\i_nan\OneDrive\Desktop\TV_MT5_EXECUTOR")

schema_file = BASE / "app" / "schemas" / "webhook.py"

schema_file.write_text(
'''
from pydantic import BaseModel

class WebhookSignal(BaseModel):
    token: str

    strategy: str
    symbol: str
    timeframe: str

    side: str

    entry: float
    sl: float

    tp1: float
    tp2: float
    tp3: float

    score: int
    session: str

    event_time: str
    mode: str
''',
encoding="utf-8"
)

print("Webhook schema created.")