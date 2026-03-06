from config import *
import chromadb
from groq import Groq
import pandas
from dotenv import load_dotenv
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

load_dotenv()

client = chromadb.Client()

groq_client = Groq()
new_collection_name = 'faqs'

sentence_transformer_ef = SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL,
    device="cpu"
)


def ingest_faq_data(path_csv):
    if new_collection_name not in [c.name for c in client.list_collections()]:
        print("creating collection ...")
        collection = client.create_collection(
            name=new_collection_name,
            embedding_function=sentence_transformer_ef
        )
        df = pandas.read_csv(path_csv)
        print(df.head())
        docs = df['question'].to_list()
        metadata = [{'answer': ans} for ans in df['answer'].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]
        print("Ingesting FAQ data into Chromadb...")
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )   
        print(f"FAQ Data successfully ingested into Chroma collection: {new_collection_name}")
    else:
        print(f"Collection: {new_collection_name} already exist")


def get_relevant_qa(query):
    collection = client.get_collection(
        name=new_collection_name,
        embedding_function=sentence_transformer_ef
    )
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result


def generate_answer(query, context):
    prompt = f'''Given the following context and question, generate answer based on this context only.
    If the answer is not found in the context, kindly state "I don't know". Don't try to make up an answer.
    
    CONTEXT: {context}
    
    QUESTION: {query}
    '''
    completion = groq_client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ],
        model=LLM_MODEL
    )

    return completion.choices[0].message.content


def faq_chain(query):
    result = get_relevant_qa(query)
    print(result)
    context = "\n".join([r.get('answer') for r in result['metadatas'][0]])

    print("Context:", context)
    answer = generate_answer(query, context)
    return answer


if __name__ == '__main__':
    ingest_faq_data(path_csv)
    query = "what's your policy on defective products?"
    query = "Do you take cash as a payment option?"
    # result = get_relevant_qa(query)
    answer = faq_chain(query)
    print("Answer:",answer)
