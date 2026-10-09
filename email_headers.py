
from email import policy
from email.parser import BytesParser

import re
from email.utils import parseaddr

def get_domain(header):
    address = parseaddr(str(header or ""))[1]

    if "@" in address:
        return address.rsplit("@", 1)[1].lower()

    return ""


def check_email_security(message):
    warnings = []

    from_domain = get_domain(message.get("From"))
    reply_domain = get_domain(message.get("Reply-To"))

    print("\n=== KAVACH SECURITY CHECKS ===")

    # Check sender mismatch
    if from_domain and reply_domain:
        if from_domain != reply_domain:
            warnings.append("From and Reply-To domains differ")

    # Read reported authentication results
    auth_headers = message.get_all(
        "Authentication-Results", []
    )

    auth_text = " ".join(str(h) for h in auth_headers)

    for protocol in ["spf", "dkim", "dmarc"]:
        match = re.search(
            rf"\b{protocol}\s*=\s*([a-z]+)\b",
            auth_text,
            re.IGNORECASE
        )

        status = match.group(1).lower() if match else "not reported"

        print(f"{protocol.upper()} (reported): {status}")

        if status in ["fail", "softfail", "permerror"]:
            warnings.append(f"Reported {protocol.upper()} issue: {status}")

    print("\nWarnings found:", len(warnings))

    for warning in warnings:
        print("WARNING:", warning)

def analyze_email(file_path):
    with open(file_path, "rb") as file:
        email_message = BytesParser(
            policy=policy.default
        ).parse(file)

    print("\n=== KAVACH EMAIL SECURITY ANALYSIS ===")

    print("From:", email_message.get("From"))
    print("Reply-To:", email_message.get("Reply-To"))
    print("Return-Path:", email_message.get("Return-Path"))
    print("Subject:", email_message.get("Subject"))

    print("\n--- Authentication Results ---")
    for result in email_message.get_all(
        "Authentication-Results", []
    ):
        print(result)

    print("\n--- DKIM Signatures ---")
    for signature in email_message.get_all(
        "DKIM-Signature", []
    ):
        print(signature)

    print("\n--- Received Headers ---")
    received = email_message.get_all("Received", [])

    for hop in received:
        print(hop)

    print("Total mail hops:", len(received))
    check_email_security(email_message)


if __name__ == "__main__":
    analyze_email("sample_email.eml")
