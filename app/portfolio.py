import pandas as pd
import chromadb
import uuid
import os


class Portfolio:
    def __init__(self, file_path="resources/my_portfolio.csv"):
        self.file_path = file_path
        # Handle both absolute and relative paths
        if not os.path.exists(file_path):
            # Try alternative paths
            alternative_paths = [
                "app/resources/my_portfolio.csv",
                "resources/my_portfolio.csv",
                os.path.join(os.path.dirname(__file__), "resources/my_portfolio.csv")
            ]
            for alt_path in alternative_paths:
                if os.path.exists(alt_path):
                    self.file_path = alt_path
                    break
            else:
                raise FileNotFoundError(f"Portfolio CSV file not found. Tried: {[file_path] + alternative_paths}")
        
        self.data = pd.read_csv(self.file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])