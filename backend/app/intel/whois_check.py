import whois

def check_domain_age(domain: str):
    try:
        w = whois.whois(domain)
        created = w.creation_date
        if isinstance(created, list):
            created = created[0]
        return {"domain": domain, "creation_date": str(created)}
    except Exception as e:
        return {"domain": domain, "error": str(e)}
