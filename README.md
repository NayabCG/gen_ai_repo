# Gen AI Repo

A lightweight Python project demonstrating how to use LangChain with OpenAI to build a simple AI-powered app.

This repository is a fork of the original project maintained by [Python-AI008](https://github.com/Python-AI008), and it is intended for learning, experimentation, and contribution.

## Features

- Simple LangChain + OpenAI integration
- Uses Python environment variables for secure API management
- Quick setup for local experimentation
- Easy to extend for prompts, workflows, and AI use cases

## Project Structure

```text
gen_ai_repo/
├── LangChain-OpenAI-Demo/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── .gitignore
├── README.md
└── ...
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- `pip` installed
- An OpenAI API key

## Installation

1. Clone your fork:

```bash
git clone https://github.com/NayabCG/gen_ai_repo.git
cd gen_ai_repo
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.\.venv\Scripts\activate    # Windows
```

3. Install dependencies:

```bash
pip install -r LangChain-OpenAI-Demo/requirements.txt
```

## Configuration

Create a `.env` file in the project root or inside the demo folder and add your OpenAI key:

```env
OPENAI_API_KEY=your_api_key_here
```

Example:

```bash
cp .env.example .env
```

If `.env.example` does not exist yet, just create a new `.env` file manually.

## Running the Demo

```bash
python LangChain-OpenAI-Demo/main.py
```

This script sends a prompt to the OpenAI model and prints the response.

## Example Output

```text
The Prime Minister of India is Narendra Modi.
```

## Technologies Used

- Python
- LangChain
- LangChain OpenAI
- OpenAI API
- Python-dotenv

## Contributing

Contributions are welcome.

To contribute:

1. Fork this repository
2. Create a feature branch:

```bash
git checkout -b feature/my-improvement
```

3. Make your changes
4. Commit them:

```bash
git add .
git commit -m "Add my improvement"
```

5. Push to your fork:

```bash
git push origin feature/my-improvement
```

6. Open a Pull Request on GitHub

## License

This project does not currently include a license file. If you are planning to distribute or collaborate publicly, consider adding an open-source license such as MIT.

## Acknowledgements

- Original repository: [Python-AI008/gen_ai_repo](https://github.com/Python-AI008/gen_ai_repo)
- LangChain: https://www.langchain.com/
- OpenAI: https://openai.com/

## Notes

This project is intended for learning and experimentation. If you’re using this repository as a base for production work, it is recommended to add:

- Better error handling
- Input validation
- Unit tests
- Logging and monitoring
- A proper configuration management strategy

---

Made with ❤️ for learning and building with AI.
