from pathlib import Path

path_csv = Path(__file__).parent / "resources/faq_data.csv"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_MODEL = "llama-3.3-70b-versatile"

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50