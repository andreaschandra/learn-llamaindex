import os
import sys
import logging

import config
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
