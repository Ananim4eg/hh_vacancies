import json
from unittest.mock import patch, Mock

from src.api_client import HeadHunterAPI


@patch('requests.get')
def test_connect_to_api_hh(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200

    mock_get.return_value = mock_response

    assert HeadHunterAPI()._connect_to_api() == True


@patch('requests.get')
def test_not_connect_to_api_hh(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404

    mock_get.return_value = mock_response

    assert HeadHunterAPI()._connect_to_api() == False


@patch('requests.get')
def test_get_data_to_api_hh(mock_get):

    test_data = {'items': [
        {
            'id': '123',
            'test_info': 'test'
        }
    ]
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = test_data

    mock_get.return_value = mock_response

    assert HeadHunterAPI().get_vacancies('Тестировщик') == list(test_data['items'])

