# Lumon MDR Software Replica

A modern recreation of the Macro Data Refinement software used by Lumon Industries in the TV show Severance.

## Features (Planned)
- Retro-styled user interface with smooth animations
- Data processing pipeline for "number sorting"
- File upload and processing capabilities
- Interactive data visualization

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run src/app.py
```

## Project Structure
```
lumon-mdr/
├── src/            # Source code
├── tests/          # Test files
├── docs/           # Documentation
├── assets/         # Static assets (images, fonts, etc.)
└── requirements.txt
```

## Development
- Python 3.8+
- FastAPI for backend
- Streamlit for frontend
- Modern development practices with type hints and testing

## License
MIT License 