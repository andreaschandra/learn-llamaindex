import sys
import logging

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info("Load data...")
documents = SimpleDirectoryReader("data").load_data()
logger.info("Load data finished")

# bge embedding model
logger.info("Embedding model...")
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
logger.info("Embedding model finished")

# ollama
logger.info("Load Ollama...")
Settings.llm = Ollama(model="llama2", request_timeout=120.0)
# Settings.llm = None
logger.info("Ollama finished")

logger.info("VectorStoreIndex loading...")
index = VectorStoreIndex.from_documents(
    documents,
)
logger.info("VectorStoreIndex finished")

# query
logger.info("querying...")
query_engine = index.as_query_engine()

# Paul Graham
logger.info("query_engine.query()")
logger.info("Paul Graham")
response = query_engine.query("What did the author do growing up?")
print(response)

# SpaceX
logger.info("SpaceX")
response = query_engine.query("What is Space X?")
print(response)
logger.info("Query finished")
