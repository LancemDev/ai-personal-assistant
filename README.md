Sure! Here’s the README formatted in a way that should be easier for you to copy:

```markdown
# Foundation

## Overview

Foundation is a multi-modal AI voice assistant designed to respond to user prompts through voice commands, text inputs, and visual data. It integrates various AI models to provide informative and context-aware responses, making it suitable for a wide range of applications.

## Features

- **Voice Recognition**: Understands and processes user voice commands.
- **Text Processing**: Analyzes and responds to text-based queries.
- **Image Analysis**: Can interpret images provided by the user for context.
- **Clipboard Access**: Retrieves text from the system clipboard.
- **Logging**: Maintains a log of interactions for review and debugging.
- **Text-to-Speech**: Converts text responses into spoken words.

## Requirements

To run this project, you need the following:

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LancemDev/new-foundation.git
   cd new-foundation
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_GEN_AI_API_KEY=your_google_gen_ai_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

To start the assistant, run the main script:

```bash
python src/backend/main.py
```

Make sure your environment is set up correctly and the necessary API keys are provided.

## Logging

Logs are stored in the `logs` directory. You can check `main.log` for the main application logs and `test.log` for testing logs.

## Testing

You can run tests by executing the `test.py` script:

```bash
python test.py
```

This script tests various functionalities of the assistant, including audio transcription, prompt extraction, and response generation.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [OpenAI](https://openai.com) for their API.
- [Google Generative AI](https://cloud.google.com/generative-ai) for their services.
- [Groq](https://groq.com) for their AI model integration.
- [Pillow](https://python-pillow.org) for image processing capabilities.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for voice recognition functionalities.
```
