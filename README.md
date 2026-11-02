# train-booking-chatbot
# 🚆 RailMitra: AI Train Booking & Assistance Chatbot

RailMitra is an intelligent conversational AI assistant built specifically for Indian Railways commuters. Powered by a locally hosted **Ollama LLM** and **LangChain**, and featuring a clean **Streamlit** user interface, this application assists users with train schedules, PNR status inquiries, seat availability guidance, and class explanations while redirecting users safely to official portals for booking.

---

## 📸 Overview & Features

* **Local LLM Execution:** Runs completely offline on your local machine via Ollama (e.g., Llama 3 or Mistral), ensuring privacy and zero API costs.
* **Indian Railways Expertise:** Configured to understand Indian train nomenclature, ticket classes (1A, 2A, 3A, SL, CC, 2S), and IRCTC booking workflows.
* **Interactive UI:** A lightweight and responsive chat interface constructed with Streamlit.
* **Context-Aware Conversations:** Tracks ongoing session history to provide natural, context-aware responses.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frontend UI:** [Streamlit](https://streamlit.io/)
* **LLM Engine:** [Ollama](https://ollama.com/) (Running `llama3` / `mistral`)
* **Orchestration:** [LangChain](https://www.langchain.com/) (`langchain-ollama`)

---

## 📁 Directory Structure

```text
train-booking-chatbot/
│
├── app.py                # Main Streamlit UI frontend
├── chatbot_logic.py      # Ollama & LangChain inference pipeline
├── train_api.py          # Data/API integration for train schedules
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

1. **Python 3.10 or higher** installed on your system.
2. **Ollama** installed and running locally.
   * Download from [ollama.com](https://ollama.com/)
   * Pull the target LLM model in your terminal:
     ```bash
     ollama pull llama3
     ```

---

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/railmitra-ai-chatbot.git
   cd railmitra-ai-chatbot
   ```

2. **Create and Activate a Virtual Environment:**
   * **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   * **macOS / Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

---

## 🏃 Running the Application

1. Ensure the Ollama background service is running on your machine:
   ```bash
   ollama ps
   ```
2. Launch the Streamlit application:
   ```bash
   python -m streamlit run app.py
   ```
3. Open your browser and navigate to `http://localhost:8501`.

---

## 📄 Example `requirements.txt`

```text
streamlit
langchain
langchain-core
langchain-ollama
requests
pandas
```

---

## 🗺️ Roadmap & Future Enhancements

- [ ] Connect live IRCTC RapidAPI endpoints for real-time seat matrix lookup.
- [ ] Implement LangChain Function-Calling Agents for direct structured queries.
- [ ] Add support for multilingual responses (Hindi, Tamil, Telugu, etc.).

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
