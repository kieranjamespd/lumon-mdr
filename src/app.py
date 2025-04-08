import streamlit as st
from pathlib import Path
import time
import pandas as pd
from lumon_mdr.core.processor import DataProcessor, NumberCategory

# Configure the page
st.set_page_config(
    page_title="Lumon MDR",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Lumon's retro styling
def load_css():
    css = """
    <style>
        /* Main theme colors and fonts */
        :root {
            --lumon-green: #00ff00;
            --lumon-dark: #1a1a1a;
            --lumon-text: #cccccc;
        }
        
        /* Overall app styling */
        .stApp {
            background-color: var(--lumon-dark);
            color: var(--lumon-text);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: var(--lumon-green) !important;
            font-family: "Courier New", monospace !important;
            text-transform: uppercase;
        }
        
        /* Data container styling */
        .stTextInput > div > div {
            background-color: #000000;
            border: 1px solid var(--lumon-green);
            border-radius: 0;
            color: var(--lumon-green);
            font-family: "Courier New", monospace;
        }
        
        /* Button styling */
        .stButton > button {
            background-color: var(--lumon-dark);
            color: var(--lumon-green);
            border: 1px solid var(--lumon-green);
            border-radius: 0;
            font-family: "Courier New", monospace;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: var(--lumon-green);
            color: var(--lumon-dark);
        }
        
        /* Info boxes */
        .stInfo {
            background-color: #000000;
            border: 1px solid var(--lumon-green);
            border-radius: 0;
            color: var(--lumon-green);
        }
        
        /* Data frame styling */
        .dataframe {
            font-family: "Courier New", monospace !important;
            background-color: #000000 !important;
            color: var(--lumon-green) !important;
        }
        
        /* Animations */
        @keyframes glow {
            0% { text-shadow: 0 0 5px var(--lumon-green); }
            50% { text-shadow: 0 0 20px var(--lumon-green); }
            100% { text-shadow: 0 0 5px var(--lumon-green); }
        }
        
        h1 {
            animation: glow 2s ease-in-out infinite;
        }
        
        /* Category colors */
        .category-scary { color: #ff0000; }
        .category-happy { color: #00ff00; }
        .category-sad { color: #0000ff; }
        .category-angry { color: #ff8c00; }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def initialize_session_state():
    if 'processor' not in st.session_state:
        st.session_state.processor = DataProcessor()
    if 'processed_numbers' not in st.session_state:
        st.session_state.processed_numbers = []

def display_processed_numbers(numbers):
    if not numbers:
        return
    
    # Convert to DataFrame for display
    df = pd.DataFrame([
        {
            'Number': n.value,
            'Category': n.category.value.capitalize(),
            'Confidence': f"{n.confidence:.2%}"
        } for n in numbers
    ])
    
    st.dataframe(
        df,
        column_config={
            'Number': st.column_config.NumberColumn(
                'Number',
                format="%.2f"
            ),
            'Category': st.column_config.TextColumn(
                'Category',
                width='medium'
            ),
            'Confidence': st.column_config.TextColumn(
                'Confidence',
                width='small'
            )
        },
        hide_index=True
    )

def main():
    load_css()
    initialize_session_state()
    
    # Header
    st.title("Lumon Industries - Macro Data Refinement")
    st.markdown("---")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Data Processing")
        
        # Number input section
        st.markdown("### Manual Number Entry")
        number_input = st.text_input(
            "Enter numbers (comma-separated)",
            key="number_input",
            help="Example: 1.5, 42, -3.14, 75"
        )
        
        if st.button("Process Data", key="process_btn"):
            try:
                # Parse and process numbers
                numbers = st.session_state.processor.parse_input(number_input)
                
                # Simulate processing with progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i in range(101):
                    progress_bar.progress(i)
                    status_text.text(f"Processing: {i}%")
                    time.sleep(0.02)  # Slow down for effect
                
                # Process numbers
                processed = st.session_state.processor.process_numbers(numbers)
                st.session_state.processed_numbers = processed
                
                status_text.text("Processing complete!")
                st.success("Data successfully processed")
                
            except ValueError as e:
                st.error(str(e))
        
        # Display processed numbers
        if st.session_state.processed_numbers:
            st.markdown("### Processed Numbers")
            display_processed_numbers(st.session_state.processed_numbers)
    
    with col2:
        st.header("Statistics")
        
        # Display metrics
        st.metric(
            label="Numbers Processed",
            value=st.session_state.processor.processed_count
        )
        st.metric(
            label="Completion Rate",
            value=f"{st.session_state.processor.get_progress():.1f}%"
        )
        
        # Category distribution
        if st.session_state.processed_numbers:
            st.markdown("### Category Distribution")
            categories = [n.category.value for n in st.session_state.processed_numbers]
            category_counts = pd.Series(categories).value_counts()
            st.bar_chart(category_counts)

if __name__ == "__main__":
    main() 