from app.database.db import Base
from app.database.db import engine

from app.database.models import *
from app.database.account_models import *
from app.database.group_models import *
from app.database.trade_models import *
from app.database.trade_history_models import *
from app.database.webhook_log_models import *


def create_all_tables():

    Base.metadata.create_all(bind=engine)

    print("All tables created.")