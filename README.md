# PDF Processing Automation Workflow

This is a Python-based PDF document processing automation workflow system that can convert PDF files to PNG images and extract text content from documents using Google Gemini AI.

## Project Structure

```
gjp_workplace/
├── main.py                 # Main program entry point
├── static/                 # Static files directory
│   ├── pdf/               # Store original PDF files
│   ├── img/               # Store converted PNG images
│   └── md/                # Store extracted text content (Markdown format)
└── tools/                 # Tool modules directory
    ├── getPdfList.py      # PDF file list retrieval tool
    ├── pdfToPng.py        # PDF to PNG conversion tool
    ├── getPngList.py      # PNG file list retrieval tool
    └── geminiAPI.py       # Gemini AI text extraction tool
```

## Configuration

### Gemini API Configuration

Before use, please ensure:

1. You have obtained a Google Gemini API key
2. Configure the correct API key in `tools/geminiAPI.py`

### Directory Structure

Ensure the following directories exist:

- `static/pdf/` - Store PDF files to be processed
- `static/img/` - Store converted images (automatically created)
- `static/md/` - Store extracted text (automatically created)

## Important Notes

1. **File Size**: High-resolution conversion may produce large PNG files
2. **Processing Time**: Conversion and text extraction of large PDF files may take a long time
3. **API Limitations**: Google Gemini API may have rate limiting
4. **File Formats**: Currently only supports PDF input and PNG output

## License

All code in this project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

For detailed information, please refer to the [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html) license text.
