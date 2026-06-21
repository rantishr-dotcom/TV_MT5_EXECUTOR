import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus(os.getenv("POSTGRES_PASSWORD"))

db_url = (
    f"postgresql+psycopg2://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{password}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

print("Connecting to:", os.getenv("POSTGRES_DB"))

try:
    engine = create_engine(db_url)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("DATABASE CONNECTED")
        print(result.fetchone()[0])

except Exception as e:
    print("DATABASE ERROR")
    print(str(e))