PLATFORM_STYLES = {
    "인스타그램": {
        "icon": "📸",
        "format": lambda text: (
            f"{text.strip()}\n\n"
            ".\n.\n.\n"
            "#소통 #일상 #팔로우"
        )
    },
    "트위터": {
        "icon": "🐦",
        "format": lambda text: (
            f"{text[:277]}..." if len(text) > 280 else text
        ).strip()
    },
    "링크드인": {
        "icon": "💼",
        "format": lambda text: (
            "💼 Professional Update\n\n"
            f"{text.strip()}\n\n"
            "Thoughts? Let me know in the comments! 👇\n"
            "#Professional #Networking #Growth"
        )
    }
} 