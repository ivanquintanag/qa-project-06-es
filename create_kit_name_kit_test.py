import sender_stand_request
import pytest
from data import KitBody

def run_test(test_name, kit_body, expected_status, expected_name=None):
    response = sender_stand_request.send_post_request(kit_body)

    assert response.status_code == expected_status

    if expected_status == 201 and expected_name is not None:
        assert response.json()["name"] == expected_name

def test_allowed_character_count(): # caso1: número permitido de caracteres (1)
    kit_body = KitBody.kit_body_1
    run_test("Test 1", kit_body, 201, "a")

def test_valid_input_maximum_character_limit():  # caso2: número permitido de caracteres (511)
    kit_body = KitBody.kit_body_2
    run_test('Test 2', kit_body, 201, ("Abcd..." * 32))
def test_valid_input_minimun_character_limit(): # caso3: número de caracteres menor a la cantidad permitida (0)
    kit_body = KitBody.kit_body_3
    run_test('Test 3', kit_body, 400, '')

def test_longer_than_allowed_character_count(): # caso4: número de caracteres mayor a la cantidad permitida (512)
    kit_body = KitBody.kit_body_4
    run_test('Test 4', kit_body, 400, ("Abcd..." * 32))

def test_special_characters(): # caso5: caracteres especiales
    kit_body = KitBody.kit_body_5
    run_test('Test 5', kit_body, 201, '*%@,')

def test_allow_spaces(): # caso6: Se permiten espacios
    kit_body = KitBody.kit_body_6
    run_test('Test 6', kit_body, 201, 'A Aaa')

def test_allow_numbers(): # caso7: Se permiten números
    kit_body = KitBody.kit_body_7
    run_test('Test 7', kit_body, 201, '123')

def test_parameters_not_passed_in_request(): # caso8: parámetro no se pasa en la solicitud
    kit_body = KitBody.kit_body_8(None)
    run_test('Test 8', kit_body, 400, '{}')

def test_different_parameter(): # caso9: un parámetro diferente (número)
    kit_body = KitBody.kit_body_9
    run_test('Test 9', kit_body, 400, '123')

if __name__ == '_main_':
   print('pass')
