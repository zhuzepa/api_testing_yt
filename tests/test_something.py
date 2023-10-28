import requests
from configuration import SERVICE_URL, PATH
from src.enums.global_enums import GlobalErrorMessages


def test_getting_posts():
    response = requests.get(url=SERVICE_URL + PATH)
    received_post = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_post) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    print(response.json())
