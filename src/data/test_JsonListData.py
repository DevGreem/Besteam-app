from . import JsonListData, UserData
import json

def test_len():
    
    users_path: str = "src/data/users.json"
    
    users = JsonListData.from_json_file(UserData, users_path)
    
    with open(users_path) as file:
        data = json.load(file)
    
    assert len(users) == len(data)