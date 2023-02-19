from sqlalchemy import MetaData, Engine, create_engine
import json


def get_database_engine(engine_str: str) -> Engine:
    engine = create_engine(engine_str)
    return engine

def create_metadata_obj(schema: str = None) -> MetaData:
    return MetaData(schema=schema)

def reflect_tables(metadata_obj: MetaData, engine: Engine):
    metadata_obj.reflect(bind=engine)
    tables = metadata_obj.sorted_tables

    database_struct= {"database_schema":metadata_obj.schema}
    for table in tables:
        database_struct[table.name]={}
        for column in table.columns:
            #print(table.name, column.name, repr(column.type.python_type).removeprefix("<class '").removesuffix("'>"))
            database_struct[table.name][column.name]=repr(column.type.python_type).removeprefix("<class '").removesuffix("'>")
            
    
    json_object = json.dumps(database_struct, indent = 4) 
    print(json_object)
    
    return 0
    #for table in reversed(metadata_obj.sorted_tables):
    #    engine.execute(table.delete())


if __name__ == "__main__":
    reflect_tables(create_metadata_obj(), get_database_engine("sqlite:///chinook.db"))