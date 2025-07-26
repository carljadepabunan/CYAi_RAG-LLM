import os
import fitz  # ✅ Better PDF layout/text parser (PyMuPDF)
import hashlib
import streamlit as st
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# ✅ Improved PDF text extractor using PyMuPDF (fitz)
def extract_text_from_pdfs(filepaths):
    raw_text_chunks = []
    for path in filepaths:
        doc = fitz.open(path)
        for page in doc:
            text = page.get_text("text")
            if text:
                raw_text_chunks.append(text)
    return raw_text_chunks

# ✅ Streamlit main UI and app logic
def main():
    load_dotenv()
    HF_API_KEY = os.getenv("HF_API_KEY")

    @st.cache_resource
    def load_llm():
        pipe = pipeline("text2text-generation", model="google/flan-t5-base",
                        tokenizer="google/flan-t5-base", device=-1, max_new_tokens=512)
        return HuggingFacePipeline(pipeline=pipe)

    llm = load_llm()

    QA_PROMPT = PromptTemplate(
        input_variables=["chat_history", "question", "context"],
        template="""
You are **YouParth AI**, a helpful tutor and educational assistant focused on solving poverty (SDG 1) and improving education (SDG 4) in the Philippines.

You read uploaded PDF documents and explain them in simple, clear, and helpful Filipino or English (depending on the user’s question).

---
🧠 **Your Task:**
- First, use only the provided context and past chat history.
- If the user asks something unclear like "What does that mean?", try to refer to the last thing they asked.
- If the answer is found in the document, give a short and clear explanation.
- If you **can’t find it in the document**, say:

  > "I couldn’t find that in the document, but here’s a helpful idea based on what I know:"

  Then give a creative answer using general knowledge about the SDGs in the Philippines.

---
📚 **Tone:** Friendly, local, and helpful — like a teacher or community tutor.

💡 **If the user asks:**
- "How to solve poverty?" → Give practical examples in the Philippines (e.g. livelihood programs, free education, skills training).
- "What are the causes?" → Mention common causes like unemployment, lack of access to education, etc.
- "How can I help?" → Suggest actions like volunteering, joining youth-led programs, or spreading awareness.

---
🗨️ **Chat History:**
{chat_history}

📄 **Relevant Document Context:**
{context}

❓ **User Question:**
{question}

✅ **Answer:**
"""
)

    st.set_page_config(page_title="CYAi", page_icon="Logo.png", layout="wide")
    st.title("✨ CYAi ✨ (Still On Developments)")
    st.write("Just upload PDF and start chatting ❕ 😀")
    st.divider()

    with st.sidebar:
        st.title("✨ CYAi ✨")
        st.write("Study Faster ❕ 😀")
        st.image("Carl.png", "Carl bot")
        st.divider()
        uploaded_files = st.file_uploader(" 📤 UPLOAD PDF:", type=["pdf"], accept_multiple_files=True)

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("vectorstore", exist_ok=True)

    @st.cache_resource
    def get_vectorstore(filepaths):
        raw_text_chunks = extract_text_from_pdfs(filepaths)
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text("\n".join(raw_text_chunks))
        embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = FAISS.from_texts(chunks, embedding=embedder)
        hash_id = hashlib.sha256("".join(filepaths).encode()).hexdigest()
        save_path = os.path.join("vectorstore", hash_id)
        vectordb.save_local(save_path)
        return vectordb

    if not uploaded_files:
        uploaded_files = []
        for filename in os.listdir("uploads"):
            if filename.endswith(".pdf"):
                uploaded_files.append(open(os.path.join("uploads", filename), "rb"))

    chatbox_Status = True
    chatbox_Text = " 🔴👎 upload PDF file before chatting..."

    if uploaded_files:
        saved_paths = []
        for file in uploaded_files:
            fname = os.path.basename(file.name)
            save_path = os.path.join("uploads", fname)
            if not os.path.exists(save_path):
                with open(save_path, "wb") as f:
                    f.write(file.read())
            saved_paths.append(save_path)

        with st.spinner(" 🔍 Loading PDF(s)..."):
            vectordb = get_vectorstore(saved_paths)
            retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 4, "lambda_mult": 0.7})
            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

            qa_chain = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=retriever,
                memory=memory,
                combine_docs_chain_kwargs={"prompt": QA_PROMPT}
            )
            st.session_state.qa_chain = qa_chain
            st.success("PDF loaded and ready to chat! 👇")

        chatbox_Status = False
        chatbox_Text = " 🟢👍 you can now chat with the AI..."

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "last_user_question" not in st.session_state:
        st.session_state.last_user_question = ""

    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(chat["question"])
        with st.chat_message("assistant"):
            st.markdown(chat["answer"])

    user_input = st.chat_input(placeholder=chatbox_Text, disabled=chatbox_Status)

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        lower_input = user_input.lower().strip()
        vague_phrases = ["what does that mean", "explain that", "what do you mean", "clarify", "explain"]

        friendly_responses = {
            "hello": "Hi there! 😊 How can I assist you today?",
            "hi": "Hello! 👋 I'm here to help.",
            "hey": "Hey! Need help with something?",
            "how are you": "I'm an AI — always ready to help! 💡",
            "thank you": "You're welcome! 👍",
            "thanks": "Glad to help! 🤗",
            "who are you": "I'm YouParth AI — your smart learning assistant.",
            "what can you do": "I can help you understand the contents of your uploaded PDFs and answer questions related to education, poverty, and more!",
            "can you help me": "Of course! 😊 Just upload a PDF and ask me questions about its content.",
            "help me": "Sure! I'm here to assist you. Upload a PDF and ask anything about it.",
            "help": "I'd be happy to help! What would you like to know?"
        }

        if lower_input in friendly_responses:
            bot_reply = friendly_responses[lower_input]
        elif "qa_chain" in st.session_state:
            with st.spinner("Generating answer..."):
                try:
                    if any(phrase in lower_input for phrase in vague_phrases):
                        actual_question = st.session_state.last_user_question
                    else:
                        actual_question = user_input

                    bot_reply = st.session_state.qa_chain.run({"question": actual_question})
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    bot_reply = "Sorry, I had trouble answering that. Please try again."
        else:
            bot_reply = "Please upload a PDF first so I can assist you better."

        with st.chat_message("assistant"):
            st.markdown(bot_reply)

        st.session_state.chat_history.append({
            "question": user_input,
            "answer": bot_reply
        })
        if lower_input not in vague_phrases:
            st.session_state.last_user_question = user_input

if __name__ == "__main__":
    main()
