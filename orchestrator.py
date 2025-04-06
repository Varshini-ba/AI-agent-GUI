import tkinter as tk
from tkinter import scrolledtext
import requests
import json
from bs4 import BeautifulSoup
from fpdf import FPDF
import datetime

# Helper function: Fetch AI news headlines
def fetch_ai_headlines():
    url = "https://www.bbc.com/news/technology"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        articles = soup.find_all("h3")
        headlines = [a.text.strip() for a in articles if a.text.strip()][:5]

        with open("ai_headlines.txt", "w", encoding="utf-8") as f:
            for h in headlines:
                f.write(f"- {h}\\n")

        return "Top 5 technology headlines saved to ai_headlines.txt"
    except Exception as e:
        return f"Error fetching headlines: {e}"



# Helper function: Search smartphone reviews (mock implementation)
def search_smartphone_reviews():
    pros = ["Great display", "Fast processor", "Good camera"]
    cons = ["Average battery", "No headphone jack"]
    summary = "Smartphone X offers a great display and performance but lacks in battery life."
    with open("smartphone_review_summary.txt", "w", encoding="utf-8") as f:
        f.write("Pros:\n" + "\n".join(pros) + "\n\nCons:\n" + "\n".join(cons) + f"\n\nSummary:\n{summary}")
    return "Smartphone review summary saved to smartphone_review_summary.txt"

# Helper function: Create PDF with renewable energy trends
def create_renewable_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Renewable Energy Trend Report", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, "This report analyzes trends in solar, wind, and hydro energy sources.")
    pdf.cell(0, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}", ln=True)
    pdf.output("renewable_trend_report.pdf")
    return "PDF report saved as renewable_trend_report.pdf"

# Command handler
def process_command(command):
    command = command.lower()
    if command.startswith("ai headlines"):
        return fetch_ai_headlines()
    elif command.startswith("ai search smartphone reviews"):
        return search_smartphone_reviews()
    elif command.startswith("ai renewable energy analysis"):
        return create_renewable_pdf()
    else:
        return "Command not recognized. Try: ai headlines, ai search smartphone reviews, ai renewable energy analysis."

# GUI setup
def run_gui():
    root = tk.Tk()
    root.title("AI Agent GUI")
    root.geometry("600x400")

    tk.Label(root, text="Enter your command below:").pack()
    entry = tk.Entry(root, width=80)
    entry.pack(pady=5)

    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
    output_box.pack(pady=10)

    def handle_run():
        cmd = entry.get()
        result = process_command(cmd)
        output_box.insert(tk.END, f"> {cmd}\n{result}\n\n")
        output_box.see(tk.END)

    tk.Button(root, text="Run", command=handle_run).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()





