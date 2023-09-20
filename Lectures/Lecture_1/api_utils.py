import requests
from requests import Session, Response
from typing import Any

S: Session = requests.Session()


def get_sites(lat, long, limit, radius) -> list:
    url: str = "https://en.wikipedia.org/w/api.php"

    params: dict[str, str] = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }

    r: Response = S.get(url=url, params=params)
    pages: Any = r.json()['query']['geosearch']
    sites: list = [i['title'] for i in pages]

    return sites
