import os
os.environ['OPENAI_API_KEY'] = ""

from llama_index import download_loader

WikipediaReader = download_loader("WikipediaReader")

loader = WikipediaReader()
abc = input("which topic do you want to know about")
documents = loader.load_data(pages=[abc])
from llama_index import GPTSimpleVectorIndex
index = GPTSimpleVectorIndex.from_documents(documents)
# save index to file
index.save_to_disk("simple_vector_index.json")
import time
from llama_index import GPTSimpleVectorIndex
from llama_index.optimization.optimizer import SentenceEmbeddingOptimizer
# load from disk
index = GPTSimpleVectorIndex.load_from_disk('simple_vector_index.json')
features="html.parser"
print("Without optimization")
start_time = time.time()
print("Enter a question related to",x)
i = input()
res = index.query(i)
end_time = time.time()
print("Total time elapsed: {}".format(end_time - start_time))
print("Answer: {}".format(res))
