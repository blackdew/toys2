import streamlit as st
from utils import init_page, create_text_input, convert_text, display_result

def main():
    init_page()
    st.title("소셜 미디어 텍스트 변환기 ✨")
    
    user_text, platform = create_text_input()
    
    if user_text:
        converted_text = convert_text(user_text, platform)
        display_result(user_text, converted_text, platform)

if __name__ == "__main__":
    main() 