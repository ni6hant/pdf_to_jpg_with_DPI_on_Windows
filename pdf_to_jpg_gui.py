import sys
import os
from tkinter import Tk, filedialog, simpledialog, messagebox
from pdf2image import convert_from_path

def main():
    # Hide Tkinter main window
    root = Tk()
    root.withdraw()

    try:
        # === 1. Get PDF path ===
        if len(sys.argv) > 1:
            pdf_path = sys.argv[1]
            if not os.path.isfile(pdf_path) or not pdf_path.lower().endswith(".pdf"):
                messagebox.showerror("Error", "The dropped file is not a valid PDF.")
                sys.exit(1)
        else:
            pdf_path = filedialog.askopenfilename(
                title="Select a PDF file",
                filetypes=[("PDF files", "*.pdf")]
            )
            if not pdf_path:
                messagebox.showinfo("Cancelled", "No PDF selected. Exiting.")
                sys.exit(0)

        # === 2. Select output folder ===
        output_folder = filedialog.askdirectory(title="Select output folder")
        if not output_folder:
            messagebox.showinfo("Cancelled", "No output folder selected. Exiting.")
            sys.exit(0)

        # === 3. Ask for DPI ===
        dpi = simpledialog.askinteger("DPI", "Enter desired DPI:", initialvalue=300)
        if not dpi or dpi <= 0:
            dpi = 300

        os.makedirs(output_folder, exist_ok=True)

        # === 4. Determine Poppler path ===
        if getattr(sys, 'frozen', False):
            # Running inside EXE
            base_path = sys._MEIPASS
        else:
            # Running as script
            base_path = os.path.dirname(__file__)

        poppler_path = os.path.join(base_path, "poppler-25.12.0", "bin")

        if not os.path.exists(poppler_path) or not os.path.exists(os.path.join(poppler_path, "pdfinfo.exe")):
            messagebox.showerror("Error", f"Poppler binaries not found.\nExpected location:\n{poppler_path}")
            sys.exit(1)

        # === 5. Convert PDF to JPG ===
        pages = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

        if not pages:
            messagebox.showerror("Error", "No pages found in PDF.")
            sys.exit(1)

        for i, page in enumerate(pages):
            page.save(os.path.join(output_folder, f"page_{i+1}.jpg"), "JPEG")

        messagebox.showinfo(
            "Done",
            f"Conversion complete!\n{len(pages)} page(s) saved to:\n{output_folder}"
        )
        sys.exit(0)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()