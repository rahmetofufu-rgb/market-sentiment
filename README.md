# Market Sentiment Analyzer

A Python application that scrapes financial and technology news headlines, performs sentiment analysis, stores results in CSV format, and visualizes market sentiment.

## Features
- Multi-source headline collection (Hacker News, Reuters, BBC)
- Text cleaning and polarity-based sentiment classification
- Persistent CSV storage with timestamping
- Basic visualization dashboard

## Installation
1. Clone the repository: `git clone https://github.com/rahmetofufu-rgb/market-sentiment.git`
2. Create and activate a virtual environment: `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. Install dependencies: `pip install -r requirements.txt`

## Usage
```bash
python sentiment.py          # Run scraping + analysis + plot
streamlit run dashboard.py   # Launch interactive dashboard (after Step 7)
Project StatusCurrently in active development. Future enhancements include API integration and advanced ML models.
