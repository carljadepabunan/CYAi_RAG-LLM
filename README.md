# ✍🏻📚🤖  **CYAi RAG-LLM** 🤖📚✍🏻
_**(Still In Developments)**_
### 📍 Screenshot

<img width="1600" height="860" alt="image" src="https://github.com/user-attachments/assets/d6c21d49-dc7a-4714-afba-5e9e857dce3c" />

### 📍 Developers
      1. Mr. Carl Jade Pabunan
      2. Mr. Yousif Aboud Elsiddig
      3. Mr. Arth Ruther Berango

### 📍 Web Application Demo Link
      https://cyai-rag-llm.streamlit.app/
### 📍 What Is **CYAi**?
- It is a chatbot uses _RAG-LLM_ technology focuses on developing students knowledge, students can upload PDF files and chat with CYAi about the PDF files they upload.
- CYAi means; C-carl, Y-yousif, A-arth, Ai-Artificial intelligence. Carl, Yousif, and Arth was the three programmers developed CYAi
- **fun fact:** "CYAi is our _AI6100-AI Prompt Engineering Course "By AMA University"_ final project and it was inspired by two of the United Nation SDG which is No Poverty and Quality education."
### 📍 What Is **RAG-LLM**?
- Retrieval Augmented Generation (RAG) is a structural method designed to enhance the performance of large language model (LLM) applications by utilizing specialized data. This process involves fetching documents or information pertinent to a specific question or task and supplying them as context for the LLM. RAG has proven effective in applications such as support chatbots and question-and-answer systems that require current information or access to specialized knowledge in a particular field. (databricks.com)
### 📍 Technology Used
- **Streamlit**: 🌟 A powerful framework for building interactive web applications, allowing users to easily upload PDF files and interact with the AI.
- **Langchain**: 🔗 A library designed for building applications with language models, enabling seamless integration of various components for enhanced functionality.
- **Langchain Communit**y: 🌐 An extension of Langchain that provides additional tools and resources for building language model applications.
- **python-doten**v: 📦 A library for managing environment variables, making it easy to configure settings and keep sensitive information secure.
- **Transformers**: 🤖 Provides access to a wide range of pre-trained language models, enabling the chatbot to understand and generate human-like responses based on uploaded content.
- **Torch**: 🔥 A deep learning framework that supports tensor computations and is essential for running models from the Transformers library.
- **Sentence-Transformers**: 🧠 A library for generating sentence embeddings, enhancing the chatbot's ability to understand and process user queries.
- **faiss-cpu**: ⚙️ A library for efficient similarity search and clustering of dense vectors, improving the chatbot's performance in retrieving relevant information.
- **pyMuPDF**: 📄 A library for reading and extracting text from PDF files, helping the application retrieve relevant information from user uploads.

# 🟢 Settup Requirements
- Python: 3.13.+ https://www.python.org/downloads/release/python-3130
- Visual Studio Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools
- Visual Studio Code: https://code.visualstudio.com/download
- Git: https://git-scm.com/downloads

# 🟢 How To Settup And Use CYAi Offline
### 👉 A. Setting Up Desketop Computer
   1. Install Python 3.13.5+
   2. Install Visual Code
   3. Install Git
   4. Install Visual Studio Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools

            a. Open The Downloaded "vs_BuildTools"
            b. Select Desktop Development with C++ and Select this:
                  - Windows 10 SDK or Windows 11 SDK (it depends on your computer windows version)
                  - MSVC v142 - VS 2019 C++ x64/x86 build tools (or later)
            e. Click Install
### 👉 B. Cloning The Repository
   1. Open Visual Studio Code
   2. Create Or Upload Folder
   3. Open Visual Studio Code Terminal, For Shortcut Type "CTRL + J"
   4. To Clone Repo Type:

            git clone https://github.com/carljadepabunan/CYAi_RAG-LLM.git
### 👉 C. Get The API Key From Huggingchain
   1. Open This Link, Create Account And Create Access Key Or Token: https://huggingface.co
### 👉 D. Creating And Activate Virtual Environment
      cd CYAi_RAG-LLM
      python -m venv .venv
      .\.venv\Scripts\activate
### 👉 E. Installing Require Dependencies
      pip install -r requirements.txt
### 👉 F. Enabling The Costum UI For Streamlit      
      mkdir .streamlit
      move config.toml .\.streamlit
### 👉 G. Running The Main Application
      streamlit run app.py
### 👉 H. Upload choosen file and interact with the RAG-LLM.
