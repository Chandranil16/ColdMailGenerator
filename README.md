# 🧊 Cold Email Generator using LangChain, ChromaDB, llama 3.3-70b-versatile, and GroqCloud API

## 📌 Introduction

This project is a **Cold Email Generator** powered by cutting-edge large language models and retrieval-based intelligence. It enables the creation of **highly personalized, context-aware cold emails** for B2B outreach, sales campaigns, and lead engagement. Built with a focus on flexibility, speed, and scalability, the application leverages **LangChain** for orchestrating LLM workflows, **ChromaDB** for semantic vector search, **LLaMA 3.3-70b** for high-quality text generation—all wrapped in a clean, interactive **Streamlit** user interface, and **Groq API** for fetching and generating email content.

By embedding and retrieving prospect data from ChromaDB, the app personalizes emails based on extracting recipient attributes such as job title, company, industry, and pain points, producing natural and persuasive email copy tailored to each contact.

---

## 🛠️ Tech Stack & Tools Used

| Tool / Library       | Purpose |
|----------------------|---------|
| **LangChain**        | Framework for building LLM-driven applications. Used for prompt templating, chaining logic, and managing LLM calls. |
| **ChromaDB**         | Lightweight vector database for storing and retrieving embedded prospect data. Enables semantic search for personalization. |
| **LLaMA 3.3-70B**    | State-of-the-art open-weight LLM served via Groq's ultra-fast inference API. Used for generating email content. |
| **Streamlit**        | Web-based UI for interacting with the email generator in real time. Enables simple and intuitive usage. |
| **GroqCloud API**    | Fetching email content based on information extracted my the LLM model from eah context. |
---

## 🚀 Features

- 🔍 **Context-aware cold email generation**
- 💡 **Extraction of specific attributes and storing it in database** using ChromaDB
- ✨ **LLaMA 3.3-70B** for natural and effective email copy
- 🧠 **Semantic similarity search** for past examples or similar profiles
- 🖥️ **Streamlit interface** for quick input and generation
