import pytest
from styles import PLATFORM_STYLES
from utils import convert_text

def test_instagram_conversion():
    """Test Instagram style text conversion"""
    test_text = "안녕하세요\n테스트입니다"
    converted = convert_text(test_text, "인스타그램")
    
    assert "안녕하세요\n테스트입니다" in converted
    assert "#소통 #일상 #팔로우" in converted
    assert ".\n.\n." in converted

def test_twitter_conversion():
    """Test Twitter style text conversion with character limit"""
    # 정상 길이 텍스트 테스트
    short_text = "안녕하세요"
    assert convert_text(short_text, "트위터") == "안녕하세요"
    
    # 280자 초과 텍스트 테스트
    long_text = "a" * 300
    converted = convert_text(long_text, "트위터")
    assert len(converted) <= 280
    assert converted.endswith("...")

def test_linkedin_conversion():
    """Test LinkedIn style text conversion"""
    test_text = "전문적인 내용입니다"
    converted = convert_text(test_text, "링크드인")
    
    assert "Professional Update" in converted
    assert "전문적인 내용입니다" in converted
    assert "#Professional" in converted
    assert "comments" in converted

def test_empty_text():
    """Test conversion with empty text"""
    for platform in PLATFORM_STYLES.keys():
        converted = convert_text("", platform)
        assert isinstance(converted, str)
        assert len(converted.strip()) > 0  # 최소한의 포맷팅은 있어야 함

def test_whitespace_handling():
    """Test handling of whitespace in text"""
    test_text = "  테스트  \n  공백  "
    for platform in PLATFORM_STYLES.keys():
        converted = convert_text(test_text, platform)
        assert isinstance(converted, str)
        assert "테스트" in converted
        assert "공백" in converted

def test_invalid_platform():
    """Test handling of invalid platform"""
    with pytest.raises(KeyError):
        convert_text("테스트", "존재하지_않는_플랫폼") 