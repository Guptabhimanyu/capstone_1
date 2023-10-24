# Replace the old import statement
from pydantic import BaseSettings

# With the new import statement
from pydantic_settings import BaseSettings
import os 
import chromadb
from chromadb.config import Settings 
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory='db',
        anonymized_telemetry=False
)
