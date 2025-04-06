# AI-agent-GUI
A simple autonomous agent GUI using Python
>>>>>>> b041a2032e42a319250612ea3a25fd45c8dd2487
💬 AI Agent GUI
🤖 A simple AI-powered assistant with a graphical user interface.
________________________________________
AI Agent GUI is a Python-based desktop application that acts as a mini AI assistant. It takes user commands through a clean GUI and performs actions like fetching news headlines, telling jokes, checking weather, or searching the web.
This was created as part of the UVCE - Upsurge Labs Assignment 2025.
✨ Features
•	🖼️ Graphical User Interface (GUI) built with tkinter
•	✅ Predefined AI command handling:
o	ai headlines – fetches latest news
o	ai tell me a joke – tells a random joke
o	ai weather in <city> – fetches weather info
o	ai search <query> – performs a web search
•	📜 Scrollable results box for better readability
•	⚙️ Easy to use, beginner-friendly structure
Sample Commands
•	🟢 Basic Level
Command	                        What It Does
ai headlines	Fetches top 5 latest AI or tech news headlines and                          saves to ai_headlines.txt

•	🟡 Intermediate Level
Command	                         What It Does
ai search smartphone reviews	Searches for smartphone reviews online, extracts pros/cons, and creates a text summary (smartphone_summary.txt)

•	🔴 Advanced Level
Command	                             What It Does
ai renewable energy analysis	Researches renewable energy trends, creates a bar chart, and exports a professional PDF report (renewable_trend_report.pdf)

•	💬 Optional Extra Commands
Command	What It Could Do
ai summarize article <url>	Fetch and summarize any article from a link
ai translate to french	Translate your last summary to another language
ai visualize <topic>	Generate a word cloud or chart of any topic


🛠️ Installation Instructions
📦 Requirements
Make sure you have:
•	Python 3.7 or higher
•	Internet connection (for API results)
Required libraries:
Library	Use For
tkinter	Creating the graphical user interface (GUI)
requests	Sending HTTP requests to fetch web content
beautifulsoup4	Parsing HTML (used for scraping headlines)
nltk	Natural Language Processing (summarizing reviews)
matplotlib	Creating charts for PDF reports
fpdf	Generating PDF files

▶️ How to Run the Code
1.	Clone the repository or download the ZIP:
git clone https://github.com/Varshini-ba/AI-agent-GUI.git
2.	Run the program:
python orchestrator.py
3.	The GUI will open. Type commands in the textbox click Run
