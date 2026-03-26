from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_margin(0)
pdf.image("shirtificate.png", x=.5, y=10)
pdf.set_font("Helvetica", size=26)
pdf.set_text_color(255, 255, 255)
pdf.cell(w=0, h=160, text=f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")