# English Interview Correction Service

An AI-powered English correction service designed for Koreans preparing for English interviews. By analyzing real interview data from sources like YouTube, the service aims to improve users' English expressions, making them more natural and professional.

## Project Structure

```
english-interview-correction/
├── venv/                           # Virtual environment
├── requirements.txt                # Dependencies
├── model/                          # Model-related code
│   ├── __init__.py
│   ├── qwen_model.py               # Qwen model wrapper class
│   └── prompts.py                  # Prompt templates
├── utils/                          # Utility functions
│   ├── __init__.py
│   └── text_processing.py          # Text processing utilities
├── tests/                          # Test code
│   ├── __init__.py
│   ├── test_model.py               # Model tests
│   └── test_prompts.py             # Prompt tests
├── examples/                       # Example code
│   └── correction_example.py       # Correction examples
└── main.py                         # Main execution file
```

## Installation

1. Clone the project:
```bash
git clone <repository-url>
cd english-interview-correction
```

2. Create and activate virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Interface

```bash
python main.py
```

### Run Examples

```bash
python examples/correction_example.py
```

## System Architecture

This project currently focuses on the Model Layer of the full system. The complete system will consist of the following layers:

1. **Data Collection Layer**
   - Collection of English interview data through YouTube API
   - Will be implemented as a separate service

2. **Data Process Layer**
   - Speech-to-Text conversion
   - Data preprocessing and pattern analysis

3. **Model Layer** (currently being implemented)
   - English expression correction using the Qwen model
   - Few-shot prompt design

4. **Realtime Process Layer**
   - Real-time correction processing for user input
   - Generation of correction feedback

5. **Presentation Layer**
   - User interface (web/app)
   - Visualization of correction results

## Model Information

This project currently uses the Qwen2.5-1.5B-Instruct model from Hugging Face. This multilingual model specializes in English and Chinese, making it suitable for correcting English expressions used by Korean speakers.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.