from app import (
    scam_check,
    calculate_risk_score,
    get_risk_level,
    load_scam_guide,
)
# Test 1: Detect an OTP scam phrase
def test_otp_phrase_is_detected():
    matches = scam_check("Please share your OTP")

    assert any(
        "share your otp" in match.lower()
        for match in matches
    )


# Test 2: Urgent OTP message should be HIGH risk
def test_urgent_otp_message_gets_high_risk():
    matches = scam_check("Urgent! Share your OTP immediately.")
    score = calculate_risk_score(matches)

    assert score >= 70
    assert get_risk_level(score) == "HIGH"


# Test 3: Normal message should have LOW risk
def test_normal_message_gets_low_risk():
    matches = scam_check(
        "Hello, are we still meeting tomorrow?"
    )
    score = calculate_risk_score(matches)

    assert score == 0
    assert get_risk_level(score) == "LOW"


# Test 4: Detect shortened URLs
def test_shortened_url_is_detected():
    matches = scam_check(
        "Check this link https://bit.ly/abc123"
    )

    assert any(
        "shortened URL" in match
        for match in matches
    )


# Test 5: Detect URLs containing an IP address
def test_ip_address_url_is_detected():
    matches = scam_check(
        "Sign in here: http://192.168.1.10/login"
    )

    assert any(
        "IP address" in match
        for match in matches
    )


# Test 6: Detect the @ symbol trick in URLs
def test_at_symbol_url_is_detected():
    matches = scam_check(
        "Sign in here: https://trusted.example@evil.example/login"
    )

    assert any(
        "@ symbol" in match
        for match in matches
    )

# Test 7: Detect a Punycode/lookalike domain
def test_punycode_url_is_detected():
    matches = scam_check(
        "Check this link: https://раypal.example/login"
    )

    assert any(
        "Punycode domain" in match
        for match in matches
    )

def test_scam_guide_loads_otp_advice():
    guide = load_scam_guide()

    assert "OTP" in guide
    assert len(guide) > 0
