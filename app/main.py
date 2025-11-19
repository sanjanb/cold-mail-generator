# Import and test all required packages
import sys
import warnings
warnings.filterwarnings('ignore')

# Test imports with version checking
try:
    import streamlit as st
    print(f"✓ Streamlit: {st.__version__}")
except ImportError as e:
    print(f"✗ Streamlit import failed: {e}")
    
try:
    import langchain
    print(f"✓ Langchain: {langchain.__version__}")
except ImportError as e:
    print(f"✗ Langchain import failed: {e}")

try:
    from langchain_community.document_loaders import WebBaseLoader
    print("✓ LangChain Community: WebBaseLoader imported")
except ImportError as e:
    print(f"✗ LangChain Community import failed: {e}")

try:
    from langchain_groq import ChatGroq
    print("✓ LangChain Groq: ChatGroq imported")
except ImportError as e:
    print(f"✗ LangChain Groq import failed: {e}")

try:
    import unstructured
    print(f"✓ Unstructured: {unstructured.__version__}")
except ImportError as e:
    print(f"✗ Unstructured import failed: {e}")

try:
    import selenium
    print(f"✓ Selenium: {selenium.__version__}")
except ImportError as e:
    print(f"✗ Selenium import failed: {e}")

try:
    import chromadb
    print(f"✓ ChromaDB: {chromadb.__version__}")
except ImportError as e:
    print(f"✗ ChromaDB import failed: {e}")

try:
    import pandas as pd
    print(f"✓ Pandas: {pd.__version__}")
except ImportError as e:
    print(f"✗ Pandas import failed: {e}")

try:
    import dotenv
    print(f"✓ Python-dotenv imported")
except ImportError as e:
    print(f"✗ Python-dotenv import failed: {e}")

# Import local modules (if they exist)
try:
    from chains import Chain
    print("✓ Local chains module imported")
except ImportError as e:
    print(f"✗ Local chains module import failed: {e}")

try:
    from portfolio import Portfolio
    print("✓ Local portfolio module imported")
except ImportError as e:
    print(f"✗ Local portfolio module import failed: {e}")

try:
    from utils import clean_text
    print("✓ Local utils module imported")
except ImportError as e:
    print(f"✗ Local utils module import failed: {e}")


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://www.wearedevelopers.com/en/companies/3853/picnic-technologies/47673/machine-learning-engineer")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    try:
        chain = Chain()
        portfolio = Portfolio()
        st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
        create_streamlit_app(chain, portfolio, clean_text)
    except Exception as e:
        st.error(f"Failed to initialize application: {e}")
        st.info("Please ensure all required files are present and environment variables are set.")