# Text Summarizer with Hugging Face

A powerful text summarization application built using Hugging Face Transformers that automatically generates concise summaries from long text documents using state-of-the-art transformer models.

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Models Supported](#models-supported)
* [Examples](#examples)
* [API Reference](#api-reference)
* [Contributing](#contributing)
* [License](#license)

## Overview

This project implements an automated text summarization system using state-of-the-art transformer models from Hugging Face. The application processes large text documents and generates coherent, meaningful summaries while preserving key information and context. Perfect for researchers, students, and professionals who need to quickly digest large amounts of text.

## Features

* **Multiple Summarization Techniques**: Supports both extractive and abstractive summarization
* **Pre-trained Models**: Uses powerful models like BART, T5, Pegasus from Hugging Face
* **Flexible Input**: Accepts various input formats (text files, direct text input, URLs)
* **Customizable Length**: Control summary length with min/max parameters
* **Batch Processing**: Summarize multiple documents at once
* **Web Interface**: User-friendly Streamlit interface
* **CLI Support**: Command-line interface for automation
* **GPU Acceleration**: Automatic GPU detection and utilization
* **Multi-language Support**: Works with various languages depending on the model

## Technologies Used

* **Python 3.8+**
* **Hugging Face Transformers** - Pre-trained transformer models
* **PyTorch** - Deep learning framework
* **Streamlit** - Web application framework
* **NLTK** - Natural language processing toolkit
* **NumPy** - Numerical computing
* **Pandas** - Data manipulation and analysis

## Installation

### Prerequisites

* Python 3.8 or higher
* pip package manager
* Git

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/kraj2003/Text_summarizer-Hugging-face-.git
cd Text_summarizer-Hugging-face-
```

2. **Create virtual environment (recommended):**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n text-summarizer python=3.8
conda activate text-summarizer
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Download NLTK data (if required):**
```python
import nltk
nltk.download('punkt')
```

## Usage

### Web Interface (Streamlit)

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

### Command Line Interface

```bash
# Basic usage
python summarizer.py --text "Your long text here..." --max_length 150

# From file
python summarizer.py --file input.txt --output summary.txt

# With custom model
python summarizer.py --file document.txt --model facebook/bart-large-cnn --max_length 200
```

### Python Script Usage

```python
from summarizer import TextSummarizer

# Initialize summarizer
summarizer = TextSummarizer(model_name="facebook/bart-large-cnn")

# Summarize text
text = "Your long text here..."
summary = summarizer.summarize(text, max_length=150, min_length=50)
print(summary)
```

## Project Structure

```
Text_summarizer-Hugging-face-/
│
├── README.md
├── requirements.txt
├── app.py                 # Streamlit web interface
├── summarizer.py          # Main summarizer class
├── cli.py                 # Command line interface
├── config.py              # Configuration settings
├── utils.py               # Utility functions
├── models/                # Model configurations
│   └── model_config.json
├── data/                  # Sample data and test files
│   ├── sample_text.txt
│   └── test_documents/
├── notebooks/             # Jupyter notebooks for experimentation
│   └── text_summarization_demo.ipynb
└── tests/                 # Unit tests
    └── test_summarizer.py
```

## Models Supported

This project supports various pre-trained models from Hugging Face:

* **BART Models:**
  * `facebook/bart-large-cnn` (default)
  * `facebook/bart-base`

* **T5 Models:**
  * `t5-small`
  * `t5-base`
  * `t5-large`

* **Pegasus Models:**
  * `google/pegasus-xsum`
  * `google/pegasus-cnn_dailymail`

* **DistilBART:**
  * `sshleifer/distilbart-cnn-12-6`

## Examples

### Example 1: Basic Text Summarization

```python
from summarizer import TextSummarizer

summarizer = TextSummarizer()
text = """
Your long text here that needs to be summarized...
"""
summary = summarizer.summarize(text)
print(summary)
```

### Example 2: Custom Parameters

```python
summary = summarizer.summarize(
    text,
    max_length=200,
    min_length=50,
    do_sample=False,
    num_beams=4
)
```

### Example 3: Batch Processing

```python
texts = [text1, text2, text3]
summaries = summarizer.batch_summarize(texts)
```

## API Reference

### TextSummarizer Class

#### Methods

* `__init__(model_name="facebook/bart-large-cnn")`: Initialize with model
* `summarize(text, max_length=150, min_length=50, **kwargs)`: Summarize single text
* `batch_summarize(texts, **kwargs)`: Summarize multiple texts
* `load_model(model_name)`: Load different model
* `preprocess_text(text)`: Clean and preprocess text

#### Parameters

* `max_length`: Maximum length of summary
* `min_length`: Minimum length of summary
* `do_sample`: Whether to use sampling
* `num_beams`: Number of beams for beam search
* `temperature`: Sampling temperature
* `top_k`: Top-k sampling parameter
* `top_p`: Top-p sampling parameter

## Requirements

Create a `requirements.txt` file with:

```
torch>=1.9.0
transformers>=4.12.0
streamlit>=1.2.0
nltk>=3.6
numpy>=1.21.0
pandas>=1.3.0
requests>=2.25.0
sentencepiece>=0.1.96
protobuf>=3.17.0
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/Text_summarizer-Hugging-face-.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
flake8 .
black .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Hugging Face for providing pre-trained transformer models
* Facebook AI Research for BART model
* Google Research for T5 and Pegasus models
* The open-source community for continuous support

## Contact

* **Author**: [Khushi Rajpurohit]
* **Email**: [khushirajpurohit2021@gmail.com]
* **GitHub**: [@kraj2003](https://github.com/kraj2003)
* **Project Link**: [https://github.com/kraj2003/Text_summarizer-Hugging-face-](https://github.com/kraj2003/Text_summarizer-Hugging-face-)

---

⭐ If you found this project helpful, please give it a star!

📝 For questions or suggestions, feel free to open an issue or contact me directly.
