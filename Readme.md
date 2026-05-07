# 📊 AI Data Analyst Agent

An intelligent, command-line-based AI Data Analyst Assistant powered by Hugging Face's Inference API and open-source models (Qwen). This project allows users to chat contextually with an AI and automatically analyze CSV datasets. 

When a dataset is uploaded, the agent acts as an automated data scientist: generating statistical summaries, checking for missing values, plotting correlation heatmaps, training a baseline machine learning model, and summarizing the findings using the LLM.

---

## ✨ Key Features

- **Conversational AI with Memory:** Chat with the AI naturally. The agent remembers the context of the conversation and the datasets you upload.
- **Automated Data Analysis Pipeline:** Simply pass a `.csv` file path, and the agent automatically processes it.
- **Statistical Summaries:** Generates descriptive statistics (`df.describe()`) and missing value reports.
- **Data Visualization:** Automatically calculates correlations and saves a visual `heatmap.png` to your directory.
- **Baseline Machine Learning:** Automatically selects numeric columns, splits the data, trains a `RandomForestRegressor`, and evaluates it using an R² score.
- **AI-Generated Insights:** Feeds the statistical summary to the LLM to generate plain-English explanations and actionable insights about your dataset.
- **Comprehensive Reporting:** Outputs a clean `report.txt` containing all data findings and AI insights.

---

## 📂 Project Structure

```text
ai-data-analyst-agent/
│
├── main.py          # Entry point for the AI Data Analyst Agent
├── agent.py         # Orchestrates the chatbot loop, memory, and dataset analysis
├── tools.py         # Contains the data science toolkit (Pandas, Seaborn, Scikit-Learn)
├── llm.py           # Handles the Hugging Face API connection and LLM prompt formatting
├── chatbot.py       # (Optional) A basic, standalone script for chatting without tools
├── requirements.txt # List of Python dependencies
├── .env             # Environment variables (Hugging Face API token)
└── .gitignore       # Git ignore rules for Python caches and environment files
```

---

## 🛠️ Prerequisites

1. **Python 3.8 or higher**: Make sure Python is installed on your system.
2. **Hugging Face Account**: You need an account at [Hugging Face](https://huggingface.co/).
3. **API Token with Inference Permissions**: 
   - Go to your HF Account Settings -> Access Tokens.
   - Create a **Fine-grained token**.
   - **Crucial:** Ensure you check the box for **"Make calls to the serverless Inference API"**.

---

## 🚀 Setup Instructions

**1. Prepare the Directory**
Ensure all project files (`main.py`, `agent.py`, `tools.py`, etc.) are located in the same folder. Open your terminal or PowerShell and navigate to this folder.

**2. Create a Virtual Environment (Recommended)**
This keeps your project dependencies isolated.

* **Windows:**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

* **macOS/Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables**
Create a `.env` file in your project folder. Add your Hugging Face token exactly like this, with **no spaces** around the equals sign:
```env
qwenAPI_TOKEN=hf_your_actual_token_here
```

---

## 💻 How to Run

To launch the full AI Data Analyst Agent, run the following command in your terminal:

```bash
python main.py
```

### Interacting with the Agent:
* **Chatting:** Type normal questions or greetings (e.g., `"What is a Random Forest model?"`).
* **Analyzing Data:** Type the exact path to a CSV file (e.g., `"products-1000.csv"` or `"C:/data/sales.csv"`). 
  * The agent will process the data and output: `"Analysis complete. Report saved."`
  * Check your project folder for the newly generated `report.txt` and `heatmap.png`.
* **Follow-up Questions:** After analyzing a CSV, you can ask the bot questions about it, as it remembers the upload context.
* **Exiting:** Type `"exit"` to close the agent.
