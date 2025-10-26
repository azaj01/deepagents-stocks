## ▶️ How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/sagar-n/deepagents.git
cd deep-research-agents-v3
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up your `.env` file:**

```env
TAVILY_API_KEY=your_tavily_key_here
BRAVE_SEARCH_API_KEY=your_brave_key_here
OLLAMA_MODEL=gpt-oss:20B
LM_STUDIO_MODEL=local-model
LM_STUDIO_BASE_URL=http://localhost:1234/v1
LM_STUDIO_API_KEY=lm-studio
DEFAULT_MODEL_PROVIDER=ollama
RECURSION_LIMIT = 30
```

5. **Run the app:**


Start the LangGraph backend:

```bash
langgraph dev
```

The **LangSmith server** will launch at [http://127.0.0.1:2024/](http://127.0.0.1:2024/)

---

### 6. Set Up the Deep Agents UI

1. Clone the UI repository:
   ```bash
   git clone https://github.com/langchain-ai/deep-agents-ui.git
   cd deep-agents-ui
   ```

2. Create a `.env.local` file in the root of the UI project and add the following:
   ```bash
   NEXT_PUBLIC_DEPLOYMENT_URL="http://127.0.0.1:2024"  # Or your LangGraph server URL
   NEXT_PUBLIC_AGENT_ID=research
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start the UI in development mode:
   ```bash
   npm run dev
   ```

   The frontend will be available at [http://localhost:3000](http://localhost:3000)

---

### ✅ Summary

| Component | Description | Default Port |
|------------|--------------|---------------|
| 🧠 **LangGraph / LangSmith Server** | Backend orchestrator for Deep Agents | `8001` |
| 💻 **Deep Agents UI** | Frontend interface for research agents | `3000` |
| ⚙️ **Environment Files** | `.env` (backend) and `.env.local` (frontend) manage configurations | — |

---
