import httpx
from ..config import settings

VT_BASE = "https://www.virustotal.com/api/v3/urls"

def check_url_virustotal(url: str):
    if not settings.VIRUSTOTAL_API_KEY:
        return {"url": url, "note": "No API key configured"}
    try:
        headers = {"x-apikey": settings.VIRUSTOTAL_API_KEY}
        # VT expects url id (encoded), but for prototype we just send raw url
        resp = httpx.get(f"{VT_BASE}/{url}", headers=headers)
        return {"url": url, "result": resp.json()}
    except Exception as e:
        return {"url": url, "error": str(e)}
