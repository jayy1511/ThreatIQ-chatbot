from fastapi import APIRouter, Depends, HTTPException
from ..deps import get_current_user
from ..intel.heuristics import check_keywords, check_urls, check_grammar, check_sender
from ..intel.whois_check import check_domain_age
from ..intel.virustotal import check_url_virustotal

router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("/")
def analyze_message(
    payload: dict,
    current_user: dict = Depends(get_current_user)
):
    text = payload.get("text")
    sender = payload.get("sender", "")

    if not text:
        raise HTTPException(status_code=400, detail="Missing text field")

    results = {}
    # run heuristics
    results.update(check_keywords(text))
    results.update(check_urls(text))
    results.update(check_grammar(text))
    results.update(check_sender(sender))

    # extra intelligence lookups
    vt_results = []
    whois_results = []
    for domain in results.get("domains", []):
        whois_results.append(check_domain_age(domain))
    for url in results.get("urls", []):
        vt_results.append(check_url_virustotal(url))

    results["virustotal"] = vt_results
    results["whois"] = whois_results

    return {
        "user": current_user,
        "analysis": results
    }
