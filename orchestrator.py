import tkinter as tk
from tkinter import messagebox, scrolledtext

from browser.browser_agent import get_ai_news
from filesystem.pdf_generator import create_sample_chart
from terminal.terminal_agent import run_terminal_command
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_ai_news():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    driver.get("https://news.google.com/search?q=artificial%20intelligence&hl=en-IN&gl=IN&ceid=IN%3Aen")
    
    headlines = []
    try:
        cards = driver.find_elements(By.CSS_SELECTOR, "article h3")
        for card in cards[:10]:
            headlines.append(card.text.strip())
    except Exception as e:
        headlines.append(f"Error fetching headlines: {e}")
    
    driver.quit()
    return headlines


def process_instruction(instruction):
    output = ""

    if "AI headlines" in instruction:
        news = get_ai_news()
        output = "📰 Top AI News Headlines:\n\n" + "\n".join(f"{i+1}. {n}" for i, n in enumerate(news))

    elif "generate PDF" in instruction or "chart" in instruction:
        chart_path = create_sample_chart()
        output = f"📊 Chart created: {chart_path}\n(Preview not shown here. Open the file manually if needed.)"

    elif "run command" in instruction:
        command = instruction.split("run command")[-1].strip()
        output = run_terminal_command(command)

    else:
        output = "❓ Instruction not recognized. Try: \n- 'AI headlines'\n- 'generate chart'\n- 'run command echo Hello'"

    return output

def on_submit():
    instruction = entry.get()
    if not instruction:
        messagebox.showwarning("Input Needed", "Please enter an instruction.")
        return
    result = process_instruction(instruction)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

# UI setup
root = tk.Tk()
root.title("Autonomous AI Agent")
root.geometry("700x450")

label = tk.Label(root, text="🧠 Enter your instruction:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=80)
entry.pack(pady=5)

submit_btn = tk.Button(root, text="▶️ Run Agent", command=on_submit)
submit_btn.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, height=15, width=80, font=("Consolas", 10))
output_box.pack(pady=10)

root.mainloop()




