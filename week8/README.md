## 🤖 Project Overview

For the final project of the internship, a sophisticated Question-Answering (QA) Chatbot was developed using the Retrieval-Augmented Generation (RAG) architecture. The goal of this project was to build a system capable of answering questions based on the content of a specific PDF document.

This approach allows a Large Language Model (LLM) to provide accurate, context-aware answers by first retrieving relevant information from a custom knowledge base, thus preventing hallucination and grounding its responses in factual data. The project was implemented locally, leveraging open-source models for both embeddings and generation.

## 📚 Key Concepts & Techniques

This project is an advanced application of Natural Language Processing and Large Language Models, covering several key concepts:

* **Retrieval-Augmented Generation (RAG):** An architecture that combines a retrieval system with a generative model. Instead of relying solely on its pre-trained knowledge, the LLM is provided with relevant text snippets from a document to formulate its answer.
* **Document Loading & Chunking:** Loading a source document (in this case, a PDF) and splitting it into smaller, manageable chunks of text for efficient processing.
* **Embeddings:** Using a sentence transformer model to convert text chunks into high-dimensional numerical vectors (embeddings) that capture semantic meaning.
* **Vector Stores:** Storing the text embeddings in a specialized database (like FAISS) that allows for fast and efficient similarity searches.
* **LLM Integration:** Using a local, open-source Large Language Model (like Llama 2) for the generative part of the RAG pipeline.
* **Chain Building with LangChain:** Utilizing the LangChain framework to construct and manage the entire RAG pipeline, from data ingestion to question-answering.

## 🛠️ Tools & Libraries Used

* **Language:** `Python`
* **Core Framework:** `LangChain`
* **LLM & Embeddings:** `Hugging Face Transformers`, `SentenceTransformers`, `LlamaCpp`
* **Vector Store:** `FAISS (Facebook AI Similarity Search)`
* **Document Loading:** `PyPDFLoader`
* **Environment:** `Jupyter Notebook` / `Google Colab`

## ⚙️ RAG Workflow

The chatbot operates based on the following workflow:

1.  **Data Ingestion (Indexing):**
    * A source PDF document is loaded.
    * The document is split into smaller, overlapping text chunks.
    * An open-source embedding model (`sentence-transformers/all-MiniLM-L6-v2`) is used to convert each text chunk into a vector embedding.
    * These embeddings are stored in a FAISS vector store, creating a searchable knowledge base.

2.  **Question Answering (Retrieval & Generation):**
    * A user asks a question.
    * The same embedding model converts the user's query into a vector.
    * The FAISS vector store performs a similarity search to find the text chunks (and their embeddings) that are most relevant to the query vector.
    * These relevant chunks are passed as context to a local LLM (Llama 2).
    * The LLM uses this context, along with the original question, to generate a human-like, factually grounded answer.

## 🚀 How to Run the Project

To run this project on your local machine (or in a Google Colab environment), follow these steps:

1.  **Clone the repository and navigate to the `Week-08` folder.**

2.  **Install the required libraries:**
    Create a `requirements.txt` file with the necessary packages and install them.
    ```bash
    pip install langchain langchain_community sentence_transformers faiss-cpu pypdf
    pip install llama-cpp-python
    ```
    *(Note: `faiss-cpu` is recommended for systems without a dedicated GPU. Use `faiss-gpu` for CUDA-enabled systems.)*

3.  **Download the LLM:**
    This project uses the Llama 2 model in GGUF format. Download the model file (e.g., `llama-2-7b-chat.Q4_K_M.gguf`) from a source like Hugging Face and place it in the project directory.

4.  **Add a Source Document:**
    Place the PDF file you want to use as the knowledge base (e.g., `source_document.pdf`) into the project directory.

5.  **Run the Jupyter Notebook:**
    Execute the cells in the `Week8_CSI_RAG_QA_Chatbot.ipynb` notebook sequentially to build the vector store and ask questions.

## 💡 Conclusion & Learnings

This final project was a comprehensive exercise in building a modern, practical AI application. It demonstrated the power of RAG in making LLMs more accurate and useful for domain-specific tasks. Key takeaways include the importance of data chunking strategies, the efficiency of vector stores for retrieval, and the ability to run powerful language models entirely on local hardware. This project serves as an excellent foundation for building more advanced conversational AI systems.
