# Cold Mail Generator - Professional AI-Powered Email Generation
import sys
import warnings
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

warnings.filterwarnings('ignore')

def add_custom_css():
    """Add custom CSS for minimal black and white styling"""
    st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem 1rem;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        background-color: #ffffff;
    }
    
    /* Override Streamlit's dark theme */
    .stApp {
        background-color: #ffffff;
    }
    
    .block-container {
        background-color: #ffffff;
    }
    
    /* SaaS Header styling */
    .saas-header {
        background: #ffffff;
        border-bottom: 1px solid #e0e0e0;
        padding: 0;
        margin-bottom: 0;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .header-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .brand-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .brand-logo {
        font-size: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .brand-info {
        display: flex;
        flex-direction: column;
    }
    
    .brand-name {
        font-size: 1.5rem;
        font-weight: 600;
        margin: 0;
        color: #1a1a1a;
    }
    
    .brand-tagline {
        font-size: 0.85rem;
        color: #666666;
        margin: 0;
        font-weight: 400;
    }
    
    .nav-section {
        display: flex;
        align-items: center;
        gap: 2rem;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-item {
        color: #666666;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        cursor: pointer;
        transition: color 0.2s ease;
    }
    
    .nav-item.active {
        color: #667eea;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.25rem;
    }
    
    .nav-item:hover {
        color: #667eea;
    }
    
    .user-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .user-info {
        color: #666666;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    .upgrade-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
        cursor: pointer;
        transition: transform 0.2s ease;
    }
    
    .upgrade-btn:hover {
        transform: translateY(-1px);
    }
    
    /* Input section styling */
    .input-section {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 4px;
        border: 1px solid #e0e0e0;
        margin-bottom: 2rem;
    }
    
    /* SaaS Dashboard Container */
    .dashboard-container {
        background: #f8f9fa;
        min-height: 100vh;
        padding: 2rem 0;
    }
    
    .dashboard-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }
    
    .saas-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    /* Enhanced Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-size: 1rem;
        transition: all 0.2s ease;
        width: 100%;
        letter-spacing: 0.3px;
        text-transform: none !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4) !important;
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* Secondary button styling */
    .stButton > button[kind="secondary"] {
        background: transparent !important;
        color: #667eea !important;
        border: 1px solid #667eea !important;
    }
    
    .stButton > button[kind="secondary"]:hover {
        background: #667eea !important;
        color: white !important;
    }
    
    /* Email output styling */
    .email-container {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 4px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Footer styling */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: #ffffff;
        color: #000000;
        text-align: center;
        padding: 1rem;
        border-top: 1px solid #e0e0e0;
        z-index: 1000;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        font-size: 0.9rem;
    }
    
    .footer-brand {
        font-weight: 400;
        color: #666666;
    }
    
    .footer-links {
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
    }
    
    .footer-links a {
        color: #000000;
        text-decoration: none;
        font-weight: 400;
        transition: color 0.2s ease;
        border-bottom: 1px solid transparent;
    }
    
    .footer-links a:hover {
        color: #666666;
        border-bottom: 1px solid #666666;
    }
    
    /* Responsive design improvements */
    @media (max-width: 768px) {
        .footer-content {
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .footer-links {
            gap: 1rem;
        }
        
        .header-title {
            font-size: 1.8rem;
        }
        
        .main {
            padding: 1rem 0.5rem;
        }
        
        .input-section {
            padding: 1rem;
        }
    }
    
    @media (max-width: 480px) {
        .header-title {
            font-size: 1.5rem;
        }
        
        .header-subtitle {
            font-size: 0.9rem;
        }
        
        .main {
            padding: 0.5rem 0.25rem;
        }
    }
    
    /* Tool-like styling improvements */
    .metric-container {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 4px;
        padding: 1rem;
        text-align: center;
    }
    
    /* Better spacing for tool layout */
    .stContainer {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Enhanced button styling */
    .stButton > button {
        transition: all 0.2s ease;
        font-size: 0.95rem;
    }
    
    .stButton > button:active {
        transform: translateY(1px);
    }
    
    /* Improved metrics display */
    [data-testid="metric-container"] {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 4px;
        padding: 1rem;
    }
    
    /* Better expander styling */
    .streamlit-expanderHeader {
        font-weight: 500;
        font-size: 0.95rem;
    }
    
    /* Clean dividers */
    .element-container hr {
        margin: 1.5rem 0;
        border-color: #e0e0e0;
    }
    
    /* Add padding to main content to avoid footer overlap */
    .main .block-container {
        padding-bottom: 5rem;
        background-color: #ffffff;
    }
    
    /* Success message styling */
    .success-message {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 4px;
        padding: 1rem;
        color: #000000;
        margin: 1rem 0;
    }
    
    /* Info box styling */
    .info-box {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 4px;
        padding: 1rem;
        margin: 1rem 0;
        color: #000000;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: #ffffff !important;
        border: 1px solid #e0e0e0;
        color: #000000 !important;
    }
    
    /* Text styling overrides with proper contrast */
    .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6, 
    .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #1a1a1a !important;
    }
    
    /* Widget text corrections */
    .stSelectbox label, .stTextInput label, .stTextArea label,
    .stCheckbox label, .stRadio label, .stSlider label,
    .stNumberInput label, .stDateInput label, .stTimeInput label {
        color: #1a1a1a !important;
        font-weight: 500 !important;
    }
    
    .stSelectbox > div > div > div, 
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        color: #1a1a1a !important;
        background-color: #ffffff !important;
    }
    
    /* Metric styling improvements */
    [data-testid="metric-container"] {
        background: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
        padding: 1.5rem !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
    }
    
    [data-testid="metric-container"] > div {
        color: #1a1a1a !important;
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #667eea !important;
        font-weight: 700 !important;
    }
    
    /* Expander improvements */
    .streamlit-expanderHeader {
        background: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        color: #1a1a1a !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    
    .streamlit-expanderContent {
        border: 1px solid #e0e0e0 !important;
        border-top: none !important;
        background: #ffffff !important;
    }
    
    /* Success/Error/Warning message styling */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 8px !important;
        border: none !important;
    }
    
    .stSuccess > div {
        background: #d1f2eb !important;
        color: #00695c !important;
    }
    
    .stError > div {
        background: #ffebee !important;
        color: #c62828 !important;
    }
    
    .stWarning > div {
        background: #fff8e1 !important;
        color: #ef6c00 !important;
    }
    
    .stInfo > div {
        background: #e3f2fd !important;
        color: #1565c0 !important;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 0.75rem;
        background-color: #ffffff;
        color: #000000;
    }
    
    /* Spinner styling */
    .stSpinner {
        color: #000000;
    }
    
    /* Divider styling */
    hr {
        border: none;
        border-top: 1px solid #e0e0e0;
        margin: 2rem 0;
    }
    
    /* Sidebar and other elements */
    .css-1d391kg, .css-12oz5g7 {
        background-color: #ffffff;
    }
    
    /* Alert styling */
    .stAlert {
        background-color: #f8f9fa;
        color: #000000;
    }
    
    /* Code block styling */
    .stCodeBlock {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
    }
    </style>
    """, unsafe_allow_html=True)

def add_header():
    """Add SaaS-style header with navigation"""
    st.markdown("""
    <div class="saas-header">
        <div class="header-nav">
            <div class="brand-section">
                <div class="brand-logo">📧</div>
                <div class="brand-info">
                    <h1 class="brand-name">EmailCraft AI</h1>
                    <p class="brand-tagline">Professional Cold Email Generator</p>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-links">
                    <span class="nav-item active">Generator</span>
                    <span class="nav-item">Templates</span>
                    <span class="nav-item">Analytics</span>
                    <span class="nav-item">Pricing</span>
                </div>
                <div class="user-section">
                    <span class="user-info">Free Plan</span>
                    <button class="upgrade-btn">Upgrade</button>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def add_footer():
    """Add SaaS-style footer"""
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <div class="footer-brand">
                <div class="footer-logo">📧 EmailCraft AI</div>
                <div class="footer-tagline">© 2025 Powered by AI Technology</div>
            </div>
            <div class="footer-links">
                <div class="footer-section">
                    <span class="footer-title">Product</span>
                    <span class="footer-link">Features</span>
                    <span class="footer-link">Pricing</span>
                    <span class="footer-link">API</span>
                </div>
                <div class="footer-section">
                    <span class="footer-title">Company</span>
                    <a href="https://sanjanb.github.io/" target="_blank" class="footer-link">About</a>
                    <a href="https://github.com/sanjanb" target="_blank" class="footer-link">Creator</a>
                    <span class="footer-link">Contact</span>
                </div>
                <div class="footer-section">
                    <span class="footer-title">Resources</span>
                    <span class="footer-link">Documentation</span>
                    <a href="https://github.com/sanjanb/cold-mail-generator" target="_blank" class="footer-link">Source Code</a>
                    <span class="footer-link">Support</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_streamlit_app(llm, portfolio, clean_text):
    """Create the main Streamlit application interface"""
    
    # Add custom CSS and header
    add_custom_css()
    add_header()
    
    # Main content layout - responsive design
    container = st.container()
    
    with container:
        # Create responsive columns
        left_spacer, main_content, right_spacer = st.columns([1, 10, 1])
        
        with main_content:
            # Tool description section
            st.markdown("""
            <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 4px; margin-bottom: 2rem; border: 1px solid #e9ecef;">
                <p style="margin: 0; color: #666666; font-size: 1rem; line-height: 1.5;">
                    Transform job postings into personalized outreach emails using AI. 
                    Simply paste a careers page URL and get professional cold emails tailored to specific positions.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Two-column layout for better tool structure
            input_col, info_col = st.columns([7, 3])
            
            with input_col:
                # Input section with tool-like interface
                st.markdown("### Input")
                
                url_input = st.text_input(
                    "Job Posting URL",
                    value="https://www.wearedevelopers.com/en/companies/3853/picnic-technologies/47673/machine-learning-engineer",
                    placeholder="https://company.com/careers/position",
                    help="Enter any company's careers page or specific job posting URL"
                )
                
                # Action buttons in a row
                button_col1, button_col2 = st.columns([3, 1])
                
                with button_col1:
                    submit_button = st.button("Generate Emails", type="primary", use_container_width=True)
                
                with button_col2:
                    clear_button = st.button("Clear", use_container_width=True)
                    if clear_button:
                        st.rerun()
            
            with info_col:
                # Tool information sidebar
                st.markdown("### Guide")
                
                with st.expander("How to Use", expanded=True):
                    st.markdown("""
                    **Steps:**
                    1. Paste job posting URL
                    2. Click 'Generate Emails'
                    3. Copy generated emails
                    4. Customize and send
                    """)
                
                with st.expander("Tips", expanded=False):
                    st.markdown("""
                    **Best Results:**
                    - Use specific job posting URLs
                    - Ensure URL is publicly accessible
                    - Works with most careers pages
                    """)
                
                with st.expander("Features", expanded=False):
                    st.markdown("""
                    - AI-powered analysis
                    - Portfolio matching
                    - Multiple email variants
                    - Professional formatting
                    """)
            
            # Divider
            st.markdown("<hr style='margin: 2rem 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)
            
            # Results section
            if submit_button:
                if not url_input.strip():
                    st.error("Please enter a valid URL")
                else:
                    # Create results container
                    results_container = st.container()
                    
                    with results_container:
                        st.markdown("### Results")
                        
                        try:
                            with st.spinner("Processing job posting..."):
                                # Load and process the webpage
                                loader = WebBaseLoader([url_input])
                                data = clean_text(loader.load().pop().page_content)
                                
                                # Load portfolio and extract jobs
                                portfolio.load_portfolio()
                                jobs = llm.extract_jobs(data)
                                
                                if not jobs:
                                    st.warning("No job postings found on this page. Try a more specific URL.")
                                else:
                                    # Success metrics
                                    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
                                    with metrics_col1:
                                        st.metric("Jobs Found", len(jobs))
                                    with metrics_col2:
                                        st.metric("Emails Generated", len(jobs))
                                    with metrics_col3:
                                        st.metric("Status", "Complete")
                                    
                                    st.markdown("---")
                                    
                                    # Generate and display emails
                                    for i, job in enumerate(jobs, 1):
                                        # Email header
                                        email_header_col1, email_header_col2 = st.columns([8, 2])
                                        
                                        with email_header_col1:
                                            job_title = job.get('role', 'Position')
                                            if len(jobs) > 1:
                                                st.markdown(f"#### Email {i}: {job_title}")
                                            else:
                                                st.markdown("#### Generated Email")
                                        
                                        with email_header_col2:
                                            if st.button(f"Copy", key=f"copy_{i}", use_container_width=True):
                                                st.success("Select email text below to copy", icon="📋")
                                        
                                        # Generate and display email
                                        skills = job.get('skills', [])
                                        links = portfolio.query_links(skills)
                                        email = llm.write_mail(job, links)
                                        
                                        # Email display with better formatting
                                        st.markdown("""
                                        <div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 1rem; margin: 1rem 0;">
                                        """, unsafe_allow_html=True)
                                        
                                        st.code(email, language='text')
                                        
                                        st.markdown("</div>", unsafe_allow_html=True)
                                        
                                        if i < len(jobs):
                                            st.markdown("---")
                                    
                                    # Action summary
                                    st.success(f"Successfully generated {len(jobs)} professional email(s). Review and customize before sending.")
                                        
                        except Exception as e:
                            st.error(f"Error processing URL: {str(e)}")
                            st.info("**Troubleshooting:** Check URL accessibility or try a different job posting link.")
            
            # Tool footer info
            st.markdown("<hr style='margin: 3rem 0 2rem 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)
            
            # About section in columns
            about_col1, about_col2 = st.columns(2)
            
            with about_col1:
                with st.expander("About This Tool"):
                    st.markdown("""
                    **Cold Mail Generator** analyzes job postings and creates personalized outreach emails 
                    by matching your portfolio with position requirements.
                    
                    Built with Groq AI, LangChain, and ChromaDB for accurate, relevant email generation.
                    """)
            
            with about_col2:
                with st.expander("Privacy & Data"):
                    st.markdown("""
                    - No data is permanently stored
                    - Processing happens locally
                    - URLs are only used for content analysis
                    - Your portfolio data stays secure
                    """)
    
    # Add footer
    add_footer()

if __name__ == "__main__":
    # Configure page
    st.set_page_config(
        page_title="Cold Mail Generator - Professional AI Email Tool",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    try:
        # Initialize components
        chain = Chain()
        portfolio = Portfolio()
        
        # Run the app
        create_streamlit_app(chain, portfolio, clean_text)
        
    except Exception as e:
        st.error(f"Failed to initialize application: {e}")
        st.info("Please ensure all required files are present and environment variables are set.")
        st.markdown("""
        **Quick Fix:**
        1. Check that your .env file contains your Groq API key
        2. Ensure resources/my_portfolio.csv exists
        3. Run pip install -r requirements.txt to install dependencies
        """)