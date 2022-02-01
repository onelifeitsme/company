import requests


def test_permissions():
    get_page_data = requests.get('http://127.0.0.1:8000/employees')
    assert 'Вход в учётную запись' in get_page_data.text
