from app.database.base import Base
from app.database.connection import engine
from app.models.test import TestTable

Base.metadata.create_all(bind=engine)

print("Tables created successfully")