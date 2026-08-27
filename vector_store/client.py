# Responsible for:
# Creating/configuring the ChromaDB client.

import chromadb
from config.settings import settings

def get_chroma_client() -> chromadb.PersistentClient:
  return chromadb.PersistentClient(
    path=settings.CHROMA_PATH
  )