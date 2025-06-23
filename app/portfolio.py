import pandas as pd
import chromadb
from chromadb.config import Settings
import uuid


class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

        # ✅ Use DuckDB instead of SQLite to avoid sqlite3 version errors
        self.chroma_client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="vectorstore"
        ))

        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],     # Note: documents must be a list
                    metadatas=[{"links": row["Links"]}],  # ✅ also wrap in a list
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        results = self.collection.query(query_texts=skills, n_results=2)
        return results.get('metadatas', [])
