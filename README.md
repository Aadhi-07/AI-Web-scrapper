# AI Web Scraper


![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-%230E1117.svg?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/github/license/Aadhi-07/AI-Web-scrapper)
![Last Commit](https://img.shields.io/github/last-commit/Aadhi-07/AI-Web-scrapper)


# AI Web Scraper

A powerful, AI-enhanced web scraping tool built using **LangChain**, **Selenium**, **BeautifulSoup**, and **Streamlit**. This tool extracts data from websites, summarizes content using an LLM, and presents the output in a user-friendly Streamlit interface. 

---
hg
## Features

- • Scrape and parse website content using **Selenium** & **BeautifulSoup**
- • Use **LangChain** + LLMs to summarize or interpret the scraped data
- • AI-powered prompt-based interaction with website content
- • Simple and clean **Streamlit UI** for interaction

---

## Project Structure

```
AI-Web-scrapper/

.env                       # Stores your API keys securely
requirements.txt           # Python dependencies
app.py                     # Main Streamlit app
scraper.py                 # Web scraping logic (Selenium + BeautifulSoup)
ai_engine.py               # AI interaction logic using LangChain
utils.py                   # Helper functions
README.md                  # Project documentation
```

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Aadhi-07/AI-Web-scrapper.git
cd AI-Web-scrapper
```

2. **Create and activate a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your API key in `.env`**
```
TOGETHER_API_KEY=your_together_api_key
```

---

## Running the App

```bash
streamlit run app.py
```

---

## How It Works

1. **Input a website URL**
2. The app uses `Selenium` to load dynamic content and `BeautifulSoup` to parse it.
3. Content is passed to a `LangChain` pipeline using your preferred LLM (e.g., OpenAI, Mistral).
4. The AI summarizes or analyzes the content based on your input prompt.
5. Output is shown in the Streamlit app.

---


## Deployment Options

### Local Deployment

1. Follow the [Installation](#installation) steps above.
2. Make sure your `.env` file is set correctly with your API key.
3. Run the app:
```bash
streamlit run app.py
```

