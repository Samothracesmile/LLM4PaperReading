# LLM4PaperReading

This repository contains utilities for summarizing academic papers and images using large language models accessed through [Ollama](https://ollama.ai/). The scripts automate extraction of text from PDFs or analysis of images and then call models such as `deepseek-r1:70b` or `gemma3:27b` to generate formatted summaries.

## Requirements

- Python 3.8+
- [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`)
- [FPDF](https://pyfpdf.github.io/)
- A working installation of `ollama` with models `deepseek-r1:70b` and `gemma3:27b`
- Optional: `md2pdf` for converting Markdown summaries to PDF

Install Python dependencies with `pip`:

```bash
pip install pymupdf fpdf
```

## Overview of Scripts

| File | Description |
|------|-------------|
| `paper_reader_kernel.py` | Core library. Defines `paper_reader()` which extracts text from a PDF, queries the DeepSeek model multiple times, merges the answers, and exports a Markdown and PDF summary. |
| `paper_reader.py` | Example script that iterates over PDF files in a folder and calls `paper_reader()` for each one. |
| `image_reader.py` | Demonstrates analyzing cortical surface images with the Gemma model and producing a summary PDF. |
| `prompt_text.py` | Stores the prompts used for the LLM queries. |
| `output_control.py` | Helper functions for text post-processing (e.g., removing Markdown formatting). |

## Usage

1. Place the papers you want to summarize in the `paper2read` folder (adjust the path in `paper_reader.py` if needed).
2. Ensure `ollama` is installed and the required models are available.
3. Run the batch processing script:

```bash
python paper_reader.py
```

Each PDF will be summarized using the DeepSeek model. The resulting Markdown is converted to a PDF with the suffix `_summary.pdf`. The intermediate Markdown file is removed after conversion.

You can also call `paper_reader()` directly in your own code:

```python
from paper_reader_kernel import paper_reader
paper_reader('example.pdf', 'example_summary.pdf', iteration_num=5)
```

For image analysis, run:

```bash
python image_reader.py
```

which processes `.png` images in a specified directory and produces summary PDFs describing the pattern of tau pathology.

## Notes

- These scripts rely on external commands (`ollama`, `md2pdf`) that must be available in your environment.
- The repository currently lacks automated tests. Use the scripts as examples and adapt paths or parameters to your setup.

