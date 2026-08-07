from app.services.pdf_loader import extract_text

text = extract_text("uploads/sample.pdf")

print(text[:1000])