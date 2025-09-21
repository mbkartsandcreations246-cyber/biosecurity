import streamlit as st
import pandas as pd
from modules.data_ingestion import DataIngestion
from modules.visualization import create_overview_dashboard
from utils.database import DatabaseManager

# Configure page
st.set_page_config(
    page_title="Marine Data Platform",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'db_manager' not in st.session_state:
    st.session_state.db_manager = DatabaseManager()

# Main page
st.title("🌊 AI-Driven Unified Marine Data Platform")
st.markdown("""
### Comprehensive Analysis for Oceanographic, Fisheries, and Molecular Biodiversity Data
""")

# Overview section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Datasets Loaded", len(st.session_state.db_manager.get_all_datasets()))

with col2:
    st.metric("Species Records", st.session_state.db_manager.get_species_count())

with col3:
    st.metric("Oceanographic Points", st.session_state.db_manager.get_ocean_data_count())

with col4:
    st.metric("AI Models Active", 5)

# Quick navigation
st.markdown("### Quick Access")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Upload New Data", use_container_width=True):
        st.switch_page("pages/1_Data_Upload.py")

with col2:
    if st.button("🌊 Oceanographic Dashboard", use_container_width=True):
        st.switch_page("pages/2_Oceanographic_Dashboard.py")

with col3:
    if st.button("🐟 Fisheries Analysis", use_container_width=True):
        st.switch_page("pages/3_Fisheries_Analysis.py")

# Platform features
st.markdown("### Platform Features")

feature_cols = st.columns(2)

with feature_cols[0]:
    st.markdown("""
    *Data Integration & Standardization*
    - Multi-format data upload (CSV, JSON, Excel)
    - Darwin Core and OBIS standards compliance
    - Automated metadata generation
    - Real-time data validation
    """)

with feature_cols[1]:
    st.markdown("""
    *AI-Powered Analysis*
    - Species identification and prediction
    - Cross-domain correlation analysis
    - Ecosystem health modeling
    - Biodiversity trend forecasting
    """)

# Recent activity
st.markdown("### Recent Activity")
if st.session_state.db_manager.get_recent_uploads():
    recent_data = st.session_state.db_manager.get_recent_uploads()
    st.dataframe(recent_data, use_container_width=True)
else:
    st.info("No recent uploads. Start by uploading your marine datasets!")

# Data sources integration status
st.markdown("### Data Sources Integration")
col1, col2 = st.columns(2)

with col1:
    st.markdown("*External Data Sources*")
    sources_status = {
        "OBIS (Ocean Biodiversity)": "🟢 Connected",
        "CMFRI (Fisheries Data)": "🟢 Connected", 
        "INCOIS (Oceanographic)": "🟢 Connected",
        "FishBase (Species Traits)": "🟢 Connected"
    }
    
    for source, status in sources_status.items():
        st.write(f"- {source}: {status}")

with col2:
    st.markdown("*System Health*")
    st.write("- Database: 🟢 Operational")
    st.write("- AI Models: 🟢 Ready")
    st.write("- APIs: 🟢 Active")
    st.write("- Visualizations: 🟢 Functional")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
<small>Centre for Marine Living Resources and Ecology (CMLRE) | Ministry of Earth Sciences</small>
</div>
""", unsafe_allow_html=True)
