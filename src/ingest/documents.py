import requests
import pandas as pd
from langchain.docstore.document import Document
from retriever import Retriever


def format_row(row):
    return (
        f"name: {row['name']}, "
        f"rating: {row['rating']}, "
        f"description: {row['description']} "
        f"number_of_members: {row['number_of_members']}, "
    ).lower()


def get_documents(filepaths, format_row=format_row):
    documents = []
    for filepath in filepaths:
        df = pd.read_csv(filepath)
        df['formatted_text'] = df.apply(format_row, axis=1)
        for text in df['formatted_text']:
            document = Document(page_content=text)
            documents.append(document)
    return documents
