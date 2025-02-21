PLATFORM_STYLES = {
    "인스타그램": {
        "icon": "📸",
        "format": lambda text: (
            f"{text.strip() if text.strip() else '내용을 입력해주세요'}\n\n"
            ".\n.\n.\n"
            "#소통 #일상 #팔로우"
        )
    },
    "트위터": {
        "icon": "🐦",
        "format": lambda text: (
            text[:277] + "..." if len(text) > 280 
            else (text.strip() if text.strip() else "내용을 입력해주세요")
        ).strip()
    },
    "링크드인": {
        "icon": "💼",
        "format": lambda text: (
            "💼 Professional Update\n\n"
            f"{text.strip() if text.strip() else '내용을 입력해주세요'}\n\n"
            "Thoughts? Let me know in the comments! 👇\n"
            "#Professional #Networking #Growth"
        )
    }
} 