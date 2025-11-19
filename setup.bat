@echo off
REM Setup script for Cold Mail Generator (Windows)
echo 🚀 Setting up Cold Mail Generator...

REM Check Python version
python --version
echo.

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist "app\.env" (
    echo ⚙️  Creating environment file...
    copy app\.env.template app\.env
    echo ✏️  Please edit app\.env and add your Groq API key
)

echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Edit app\.env and add your Groq API key
echo 2. Run: streamlit run app\main.py
echo 3. Open your browser to the displayed URL
echo.
echo For more information, see README.md
pause