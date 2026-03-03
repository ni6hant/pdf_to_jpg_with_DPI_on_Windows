# PDF to JPG Converter (Windows)

A simple Windows tool to convert PDF files to JPG images.
Supports **drag-and-drop PDFs** or manual file selection, lets you set the **image resolution (DPI)**, and converts PDFs **page by page**. Fully standalone — users do **not need Python or any additional software installed**.

> ⚡ This application was created with the assistance of AI (ChatGPT) to help automate PDF-to-JPG conversion.

---

## How to Use

### Option 1: Drag-and-Drop

1. Drag your PDF file onto the `pdf_to_jpg_gui.exe` file.
2. A window will appear asking you to **choose the output folder**.
3. Enter the desired **DPI** (image resolution).

   * Recommended: 150–200 for screen, 300+ for print.
4. The program will convert each PDF page to a JPG image in the selected folder.
5. A popup will confirm when conversion is complete.

### Option 2: Manual Selection

1. Double-click the `pdf_to_jpg_gui.exe`.
2. Select a PDF file via the dialog.
3. Choose an **output folder** for the JPG images.
4. Enter the **DPI**.
5. Conversion will start, and a popup will confirm when finished.

---

## Features

* Converts multi-page PDFs — one JPG per page.
* Real-time **progress bar** shows conversion status.
* Fully **standalone** EXE — no Python or additional software required.
* Users can **cancel conversion** safely by closing the progress window.
* Works offline; no internet connection needed.

---

## Notes

* Higher DPI produces higher-quality images but larger file sizes.
* Canceling a conversion will safely stop the process without errors.

---

## Credits

This tool was made possible thanks to:

* **ChatGPT (AI)** — for guidance and script generation
* **PyMuPDF (fitz)** — Python library for PDF rendering ([https://pypi.org/project/PyMuPDF/](https://pypi.org/project/PyMuPDF/))
* **Pillow** — Python Imaging Library ([https://pypi.org/project/Pillow/](https://pypi.org/project/Pillow/))

Special thanks to all contributors of these libraries for making PDF processing accessible.
