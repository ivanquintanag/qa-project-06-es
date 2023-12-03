import sender_stand_request
import pytest
from data import KitBody

def run_test(test_name, kit_body, expected_status, expected_name=None):
    response = sender_stand_request.send_post_request(kit_body)

    assert response.status_code == expected_status

    if expected_status == 201 and expected_name is not None:
        assert response.json()["name"] == expected_name

def test_positive_assert_1(): # caso1: número permitido de caracteres (1)
    kit_body = KitBody.kit_body_1
    run_test("Test 1", kit_body, 201, "a")

def test_postive_assert_2():  # caso2: número permitido de caracteres (511)
    kit_body = KitBody.kit_body_2
    run_test('Test 2', kit_body, 201, 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_postive_assert_3(): # caso3: número de caracteres menor a la cantidad permitida (0)
    kit_body = KitBody.kit_body_3
    run_test('Test 3', kit_body, 400, '')

def test_negative_assert_4(): # caso4: número de caracteres mayor a la cantidad permitida (512)
    kit_body = KitBody.kit_body_4
    run_test('Test 4', kit_body, 400, 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

def test_negative_assert_5(): # caso5: caracteres especiales
    kit_body = KitBody.kit_body_5
    run_test('Test 5', kit_body, 201, '*%@,')

def test_negative_assert_6(): # caso6: Se permiten espacios
    kit_body = KitBody.kit_body_6
    run_test('Test 6', kit_body, 201, 'A Aaa')

def test_negative_assert_7(): # caso7: Se permiten números
    kit_body = KitBody.kit_body_7
    run_test('Test 7', kit_body, 201, '123')

def test_negative_assert_8(): # caso8: parámetro no se pasa en la solicitud
    kit_body = KitBody.kit_body_8(None)
    run_test('Test 8', kit_body, 400, '{}')

def test_negative_assert_9(): # caso9: un parámetro diferente (número)
    kit_body = KitBody.kit_body_9
    run_test('Test 9', kit_body, 400, '123')

    if _name_ == '_main_':
        print('pass')
