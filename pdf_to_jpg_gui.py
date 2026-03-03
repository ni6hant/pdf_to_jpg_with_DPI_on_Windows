import sys
import os
from tkinter import Tk, filedialog, simpledialog, messagebox, Toplevel, StringVar
from tkinter import ttk
import fitz  # PyMuPDF
from PIL import Image

def main():
    root = Tk()
    root.withdraw()

    stop_conversion = {"flag": False}  # shared flag to stop gracefully

    try:
        # === 1. PDF file ===
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

        # === 2. Output folder ===
        output_folder = filedialog.askdirectory(title="Select output folder")
        if not output_folder:
            messagebox.showinfo("Cancelled", "No output folder selected. Exiting.")
            sys.exit(0)

        # === 3. DPI ===
        dpi = simpledialog.askinteger("DPI", "Enter desired DPI:", initialvalue=300)
        if not dpi or dpi <= 0:
            dpi = 300

        os.makedirs(output_folder, exist_ok=True)

        # === 4. Open PDF with PyMuPDF ===
        doc = fitz.open(pdf_path)
        total_pages = doc.page_count
        if total_pages == 0:
            messagebox.showerror("Error", "No pages found in PDF.")
            sys.exit(1)

        # === 5. Setup Tkinter progress window ===
        progress_win = Toplevel()
        progress_win.title("Converting PDF")
        progress_win.geometry("400x100")
        progress_win.resizable(False, False)

        label_var = StringVar()
        label_var.set("Starting conversion...")
        label = ttk.Label(progress_win, textvariable=label_var)
        label.pack(pady=10)

        progress_bar = ttk.Progressbar(progress_win, maximum=total_pages, length=350)
        progress_bar.pack(pady=10)
        progress_win.update()

        # === Handle user closing the window ===
        def on_close():
            if messagebox.askyesno("Cancel Conversion", "I dare you to Cancel - Bellatrix Lestrange"):
                stop_conversion["flag"] = True
                progress_win.destroy()

        progress_win.protocol("WM_DELETE_WINDOW", on_close)

        # === 6. Convert each page to JPG ===
        for i, page in enumerate(doc, start=1):
            if stop_conversion["flag"]:
                messagebox.showinfo("Cancelled", "HE DARES! HE DARES!")
                sys.exit(0)

            pix = page.get_pixmap(dpi=dpi)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img.save(os.path.join(output_folder, f"page_{i}.jpg"), "JPEG")

            # Update progress
            progress_bar['value'] = i
            label_var.set(f"Converting page {i} of {total_pages}...")
            progress_win.update()

        progress_win.destroy()
        messagebox.showinfo(
            "Done",
            f"My Lord! \n{total_pages} page(s) saved to:\n{output_folder}"
        )
        sys.exit(0)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()