
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
