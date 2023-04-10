import os
import glob
import PyPDF2
from llama_index import GPTSimpleVectorIndex
import openai

# Set up OpenAI API credentials
openai.api_key = "key"

# Step 1: Save multiple PDF or text documents
# Place all the documents in a directory
documents_directory = "path/to/documents"
pdf_files = glob.glob(os.path.join(documents_directory, "*.pdf"))
text_files = glob.glob(os.path.join(documents_directory, "*.txt"))
documents = pdf_files + text_files

# Step 2: Parse the documents
parsed_documents = []
for doc_file in documents:
    if doc_file.endswith(".pdf"):
        # Parse PDF documents
        with open(doc_file, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            document_text = ""
            for page in pdf_reader.pages:
                document_text += page.extract_text()
            parsed_documents.append(document_text)
    elif doc_file.endswith(".txt"):
        # Parse text documents
        with open(doc_file, "r") as txt_file:
            document_text = txt_file.read()
            parsed_documents.append(document_text)

# Step 3: Index the documents using Llama Index
index = GPTSimpleVectorIndex([])
index.create_index(index_name='my_docs')
for i, document_text in enumerate(parsed_documents):
    doc_id = f"doc_{i}"
    index.add_document(index_name='my_docs', doc_id=doc_id, document=document_text)

# Step 4: Ask questions using OpenAI API and Llama Index
query = input("ask your question?")
results = index.search(index_name='my_docs', query=query)

# Extract relevant document information from search results
for result in results:
    doc_id = result.doc_id
    document_text = parsed_documents[int(doc_id.split('_')[1])]
    # Use OpenAI API to generate answers from the document text
    answer = openai.Completion.create(
        prompt=f"What is the answer to the following question in the document:\n{document_text}",
        max_tokens=100,
        n=1,
        stop=None
    ).choices[0].text
    print(f"Document ID: {doc_id}")
    print(f"Answer: {answer}\n")
