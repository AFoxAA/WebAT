import yaml
from zeep import Client, Settings
from typing import Any


with open('config.yaml', encoding='utf-8') as f:
    data: Any = yaml.safe_load(f)

settings: Settings = Settings(strict=False)
client: Client = Client(wsdl=data['wsdl'], settings=settings)


def check_text(text: str) -> Any:
    return client.service.checkText(text)[0]['s']
