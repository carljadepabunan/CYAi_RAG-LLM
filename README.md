# ✍🏻📚🤖  **CYAi RAG-LLM** 🤖📚✍🏻 (Still On Developments)
### 📍 Developers
      1. Mr. Carl Jade Pabunan
      2. Mr. Yousif Aboud Elsiddig
      3. Mr. Arth Ruther Berango
### 📍 Screenshot

<img width="1600" height="860" alt="image" src="https://github.com/user-attachments/assets/d6c21d49-dc7a-4714-afba-5e9e857dce3c" />

### 📍 Web Application Link
      https://cyai-rag-llm.streamlit.app/
### 📍 What Is **CYAi**?
- It is a chatbot uses _RAG-LLM_ technology focuses on developing students knowledge, students can upload PDF files and chat with CYAi about the PDF files they upload.
- CYAi means; C-carl, Y-yousif, A-arth, Ai-Artificial intelligence. Carl, Yousif, and Arth was the three programmers developed CYAi
- **fun fact:** "CYAi is our _AI6100-AI Prompt Engineering Course "By AMA University"_ final project and it was inspired on one of the United Nation SDG which is Quality education."

### 📍 What Is **RAG-LLM**?
- Retrieval Augmented Generation (RAG) is a structural method designed to enhance the performance of large language model (LLM) applications by utilizing specialized data. This process involves fetching documents or information pertinent to a specific question or task and supplying them as context for the LLM. RAG has proven effective in applications such as support chatbots and question-and-answer systems that require current information or access to specialized knowledge in a particular field. (databricks.com)

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
      streamlit run app.python
### 👉 H. Upload choosen file and interact with the RAG-LLM.
