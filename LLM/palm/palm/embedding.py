from langchain.embeddings import VertexAIEmbeddings
from langchain.document_loaders import DirectoryLoader, TextLoader
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

loader = DirectoryLoader("sample_codes/", show_progress=True, use_multithreading=True, loader_cls=TextLoader)
docs = loader.load()

model = VertexAIEmbeddings()
vector_list = []

for doc in docs:
    vector = np.array(model.embed_query(doc.page_content))
    vector_list.append((doc.metadata["source"], vector.reshape(1, -1)))


(base_filename, base_vec) = vector_list[0]
for (elem_filename, elem_vec) in vector_list[1:]:
    print(f"{base_filename} vs {elem_filename} = {cosine_similarity(elem_vec, base_vec)}")
