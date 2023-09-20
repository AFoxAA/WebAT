from zeep import Client
import pytest

wsdl: str = 'http://dss.cryptopro.ru/verify/service.svc?wsdl'
sign: str = ''

client: Client = Client(wsdl=wsdl)


def test_step1() -> None:
    assert client.service.VerifySignature('CMS', sign)['Result'], 'test_step1 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
