import subprocess

def word_to_pdf(word_path, output_path):
    try:
        subprocess.run(["unoconv", "-f", "pdf", "-o", output_path, word_path])
        print(f"Word document converted to PDF: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    word_path = "input.docx"  # Replace with the actual path to your Word document
    output_path = "output.pdf"  # Replace with the desired output path for the PDF
    word_to_pdf(word_path, output_path)
