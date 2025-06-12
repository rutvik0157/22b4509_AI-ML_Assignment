# Intern Test Task Template: Question to Concept Mapping

Roll No: 22b4509  


This template is designed to make it easy to run and evaluate submissions for a question-to-concept mapping task using CSV data and the Anthropic LLM API.

## Folder Structure

```
.
├── main.py                 # Entry point, handles CLI and user code
├── llm_api.py              # Handles Anthropic API calls, loads API key from .env
├── csv_reader.py           # Reads CSV from resources/ and returns data
├── resources/              # Folder containing subject CSVs (ancient_history.csv, math.csv, etc.)
├── .env                    # Stores Anthropic API key
├── requirements.txt        # Python dependencies
├── Makefile                # Run commands
└── README.md               # Instructions
```

## Setup Instructions

1. **Clone the repository and navigate to the project folder.**
2. **Install dependencies:**
   ```
   make install
   ```
3. **Add your Anthropic API key:** --> need not do
   - Copy your API key into the `.env` file:
     ```
     ANTHROPIC_API_KEY=your_anthropic_api_key_here
     ```

## Usage

Run the program with your desired subject:

```
make run SUBJECT=math
```
Or directly:
```
python main.py --subject=math
```

## Where to Write Your Code

- Open `main.py`.
- Find the section marked:
  ```python
  # --- PLACEHOLDER FOR USER CODE ---
  # TODO: Implement your question-to-concept mapping logic here.

  ```
- Write your solution in this section.

## Notes
- The template uses `python-dotenv` to load environment variables.
- The Anthropic API is accessed via the `anthropic` Python package.
---

Feel free to reach out if you have any questions!


