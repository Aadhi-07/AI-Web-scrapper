from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# Simplified prompt for better results
template = (
    "Instruction: {parse_description}\n\n"
    "Content:\n{dom_content}\n\n"
    "Only return the extracted data. If nothing matches, return an empty string."
)

model = Together(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def parse_with_mistral(dom_chunks, parse_description):
    results = []
    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            print(f"[Parsing chunk {i}/{len(dom_chunks)}...]")
            response = chain.invoke({
                "dom_content": chunk,
                "parse_description": parse_description
            })
            if response.strip():
                results.append(response.strip())
        except Exception as e:
            print(f"[Error in chunk {i}]: {e}")
    return "\n\n---\n\n".join(results)
