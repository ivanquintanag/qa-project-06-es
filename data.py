user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
headers = {
    "Content-Type": "application/json"
}

class KitBody:
    kit_body_1 = {"name": "a"}
    kit_body_2 = {"name": ("Abcd..." * 32)}
    kit_body_3 = {"name": ""}
    kit_body_4 = {"name": ("Abcd..." * 32)}
    kit_body_5 = {"name": '*%@,'}
    kit_body_6 = {"name": 'A Aaa'}
    kit_body_7 = {"name": "123"}
    kit_body_8 = {}
    kit_body_9 = {"name": '123'}
