from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import datetime

def create_sample_chart():
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.title("Sample AI Trend Chart")
    plt.xlabel("Time")
    plt.ylabel("Mentions")
    chart_path = "chart.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def create_pdf_with_chart(title, content):
    filename = f"{title.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
    chart_path = create_sample_chart()
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = [Paragraph(title, styles['Title']), Paragraph(content, styles['Normal'])]
    from reportlab.platypus import Image
    story.append(Image(chart_path, width=400, height=300))
    doc.build(story)
    return filename