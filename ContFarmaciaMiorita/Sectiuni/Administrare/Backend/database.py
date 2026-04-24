from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# url-ul bazei de date
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/farmacia_miorita"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()