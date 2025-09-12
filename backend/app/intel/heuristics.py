import re
import tldextract
# import language_tool_python   # disable for now

PHISH_KEYWORDS = ["urgent", "immediately", "account suspended", "verify your account"]

def check_keywords(text: str):
    found = [kw for kw in PHISH_KEYWORDS if kw.lower() in text.lower()]
    return {"keywords_found": found}

def check_urls(text: str):
    urls = re.findall(r"(https?://\S+)", text)
    domains = [tldextract.extract(url).registered_domain for url in urls]
    return {"urls": urls, "domains": domains}

def check_grammar(text: str):
    # temporarily disabled
    return {"grammar_errors": 0}

def check_sender(sender: str):
    suspicious = False
    if sender and any(char.isdigit() for char in sender.split("@")[-1].split(".")[0]):
        suspicious = True
    return {"sender": sender, "sender_suspicious": suspicious}
