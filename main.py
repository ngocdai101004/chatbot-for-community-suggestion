from langchain.prompts import PromptTemplate
from src.prompts import GENERAL_PROMPT_TEMPLATE, RAG_PROMPT_TEMPLATE
from src.ingest.ingest import data_retriever
from src.agents.llm_agent import get_llm_agent
from src.agents.query_classifier import get_query_classifier, query_classification
from src.agents.conversation_chain import ChatbotChain
# from langchain_community.embeddings import HuggingFaceEmbeddings
# # from langchain_huggingface import HuggingFaceEmbeddings
# from sentence_transformers import SentenceTransformer
# from langchain_community.cross_encoders import HuggingFaceCrossEncoder


retriever = data_retriever()

general_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=GENERAL_PROMPT_TEMPLATE
)

rag_prompt = PromptTemplate(
    input_variables=["chat_history", "question", "context"],
    template=RAG_PROMPT_TEMPLATE
)
print('Retriever')

query_classifier = get_query_classifier()
print(query_classifier)
print('classifier')

llm = get_llm_agent()
print('LLM')

conversation_chain = ChatbotChain(llm=llm, rag_prompt=rag_prompt, general_prompt=general_prompt,
                                  compression_retriever=retriever, query_classifier=query_classifier)

query = 'Give me 3 communities about Data'
print(query_classification(query=query, classifier=query_classifier))
print('Query:', query)
chat_history = [
    {
        'question': 'Hello',
        'answer': 'Hello, What can I help you'
    }
]
message = {
    'question': query,
    'chat_history': chat_history
}
response = conversation_chain.chat(message)
chat_history.append({
    'question': query,
    'answer': response
})
print("------------------Response-------------------\n", response)
print("------------------History------------------- \n", len(chat_history))
print("---------------------------------------------")
