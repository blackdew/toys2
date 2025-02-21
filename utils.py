import streamlit as st
from styles import PLATFORM_STYLES

def init_page() -> None:
    """Initialize Streamlit page configuration"""
    st.set_page_config(
        page_title="소셜 미디어 텍스트 변환기",
        page_icon="✨",
        layout="wide"
    )

def convert_text(text: str, platform: str) -> str:
    """Convert text according to the selected platform style"""
    return PLATFORM_STYLES[platform]["format"](text)

def create_text_input() -> tuple[str, str]:
    """Create and return text input and platform selection"""
    user_text = st.text_area(
        "변환할 텍스트를 입력하세요:",
        height=150,
        key="input_text"
    ).strip()
    
    platform = st.selectbox(
        "변환할 플랫폼을 선택하세요:",
        options=PLATFORM_STYLES.keys(),
        key="platform_select"
    )
    
    return user_text, platform

def display_result(user_text: str, converted_text: str, platform: str) -> None:
    """Display the original and converted text in columns"""
    col1, col2 = st.columns(2)
    with col1:
        st.text_area(
            "원본 텍스트:",
            value=user_text,
            height=200,
            disabled=True
        )
    with col2:
        st.write(f"{PLATFORM_STYLES[platform]['icon']} {platform} 스타일:")
        st.text_area(
            "변환된 텍스트:",
            value=converted_text,
            height=200
        )
    
    if st.button("클립보드에 복사 📋", use_container_width=True):
        st.write(f'<script>navigator.clipboard.writeText("{converted_text}");</script>', unsafe_allow_html=True)
        st.toast("텍스트가 클립보드에 복사되었습니다! ✨")