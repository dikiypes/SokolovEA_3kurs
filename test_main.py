import pytest
import main
from datetime import datetime
def test_card_number():
    assert main.mask_card_number('1234567812345678') == '1234 56** **** 5678'

def test_mask_account_number():
    assert main.mask_account_number('73654108430135874305') == '**4305'

def test_result_string():
    test_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
    test_data['date'] = datetime.fromisoformat(test_data['date'])
    assert (main.result_string(test_data) =='''26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n''')

