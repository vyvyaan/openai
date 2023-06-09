import PyPDF2

# Open the PDF file
with open(r"file path", 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)


    # Extract text from each page of the PDF
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Close the PDF file
    file.close()
# Print the extracted t

import openai

# Set up OpenAI API credentials
openai.api_key = 'openai key'

# Use OpenAI to ask questions
question = input("what do you want to know about the pdf?") 
generated_text = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f'Q: {question}\nText: {text}\nA:',
    max_tokens=1024
)
answer = generated_text.choices[0].text.strip()

# Print the generated answer
print('Answer:', answer)
