# Game-rule-pdf-analyzer

- This project is a Retrieval-Augmented Generation (RAG) system that answers questions using information extracted from PDF documents. It uses LangChain to orchestrate document loading, text splitting, and semantic search. The PDFs are embedded into vector space using locally running Ollama models like gemma:2b, and stored in a ChromaDB vector store. When a user asks a question, the system retrieves relevant document chunks based on similarity, passes them along with the query to an LLM for context-aware answers, and displays the result. The project includes scripts for indexing new PDFs (populate_database.py), querying the database (query_data.py), testing accuracy (test_rag.py), and even provides a Flask-based web interface (app.py) for ease of use. It's ideal for building question-answering systems over custom data, especially in resource-constrained environments, since everything runs locally.

- This project is a Retrieval-Augmented Generation (RAG) system built using:
- 📄 PDF documents as the knowledge source
- 🧠 Ollama for local LLM inference and embeddings
- 📦 ChromaDB for vector storage and similarity search
- 🛠️ LangChain for orchestration
- 🌐 Flask (optional) for a web interface
