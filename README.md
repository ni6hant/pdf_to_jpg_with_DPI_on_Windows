# PDF to JPG Converter (Windows)

Note: I needed to make a video about printing books by ignoring the extra white spaces around the pages and also enlarging the smaller pages. However, the first step in that was the need for converting pdf to jpg files. As much as I wanted to do all this myself, I simply didn't have the time and spent an hour trying to get ChatGPT to make a program(exe) for me that will run on every Windows copmuter without even needing to install any pyhon or packages.

> ⚡ This application was created with the assistance of AI (ChatGPT) to help automate PDF-to-JPG conversion.

A simple Windows tool to convert PDF files to JPG images.  
Supports **drag-and-drop PDFs** or manual file selection, and lets you set the **image resolution (DPI)**. Fully standalone — users do **not need Python or any additional software installed**.

---

## How to Use

### Option 1: Drag-and-Drop
1. Drag your PDF file onto the `pdf_to_jpg_gui.exe` file.  
2. A window will appear asking you to **choose the output folder**.  
3. Enter the desired **DPI** (image resolution).  
   - Recommended: 150–200 for screen, 300+ for print.  
4. The program will convert each PDF page to a JPG image in the selected folder.  
5. A popup will confirm when conversion is complete.

### Option 2: Manual Selection
1. Double-click the `pdf_to_jpg_gui.exe`.  
2. Select a PDF file via the dialog.  
3. Choose an **output folder** for the JPG images.  
4. Enter the **DPI**.  
5. Conversion will start and a popup will confirm when finished.

---

## Notes
- Multi-page PDFs will produce multiple JPG files, one per page.  
- Higher DPI produces higher-quality images but larger file sizes.  
- The program is fully offline — no internet connection or Python installation is required.  
- If you encounter an error about Poppler binaries, make sure the EXE is not moved from its original folder containing the bundled Poppler folder.  

---

## Credits

This tool was made possible thanks to:  

- **ChatGPT (AI)** — for guidance and script generation  
- **pdf2image** — Python library for PDF-to-image conversion ([https://pypi.org/project/pdf2image/](https://pypi.org/project/pdf2image/))  
- **Pillow** — Python Imaging Library ([https://pypi.org/project/Pillow/](https://pypi.org/project/Pillow/))  
- **Poppler** — open-source PDF rendering library ([http://poppler.freedesktop.org/](http://poppler.freedesktop.org/))  

Special thanks to all contributors of these libraries for making PDF processing accessible.

---
