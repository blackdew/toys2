import streamlit as st

def convert_to_instagram_style(text):
    # 인스타그램 스타일 변환
    lines = text.split('\n')
    formatted_text = '\n\n'.join(lines)  # 문단 간격 추가
    hashtags = '#소통 #일상 #팔로우'  # 기본 해시태그
    return f"{formatted_text}\n\n.\n.\n.\n{hashtags}"

def convert_to_twitter_style(text):
    # 트위터 스타일 변환
    if len(text) > 280:
        text = text[:277] + "..."
    return text

def convert_to_linkedin_style(text):
    # 링크드인 스타일 변환
    professional_intro = "💼 Professional Update:\n\n"
    call_to_action = "\n\nThoughts? Let me know in the comments! 👇\n#Professional #Networking #Growth"
    return f"{professional_intro}{text}{call_to_action}"

def main():
    st.title("소셜 미디어 텍스트 변환기 ✨")
    
    # 입력 텍스트 영역
    user_text = st.text_area("변환할 텍스트를 입력하세요:", height=150)
    
    # 플랫폼 선택
    platform = st.selectbox(
        "변환할 플랫폼을 선택하세요:",
        ["인스타그램", "트위터", "링크드인"]
    )
    
    if user_text:
        st.write("원본 텍스트:", user_text)
        
        # 선택된 플랫폼에 따라 변환
        if platform == "인스타그램":
            converted_text = convert_to_instagram_style(user_text)
            st.write("📸 인스타그램 스타일:")
        elif platform == "트위터":
            converted_text = convert_to_twitter_style(user_text)
            st.write("🐦 트위터 스타일:")
        else:  # 링크드인
            converted_text = convert_to_linkedin_style(user_text)
            st.write("💼 링크드인 스타일:")
            
        # 변환된 텍스트를 박스 안에 표시
        st.text_area("변환된 텍스트:", value=converted_text, height=200)
        
        # 복사 버튼
        st.button("클립보드에 복사", help="클릭하면 변환된 텍스트가 클립보드에 복사됩니다")

if __name__ == "__main__":
    main() 