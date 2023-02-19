from src.db_reflection import reflect_db
import sqlalchemy

def test_get_database_engine():
    assert type(reflect_db.get_database_engine("sqlite:///chinook.db")) == sqlalchemy.Engine

def test_create_metadata_obj():
    assert type(reflect_db.create_metadata_obj()) == sqlalchemy.MetaData

def test_reflect_tables():
    assert reflect_db.reflect_tables(reflect_db.create_metadata_obj(),reflect_db.get_database_engine("sqlite:///chinook.db")) == 0