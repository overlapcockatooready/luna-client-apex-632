import requests
import json

class LunaAPI:
    def __init__(self, base_url='https://api.dev.luna.io/'):        
        self.base_url = base_url
    
    def get_user(self, user_id):
        response = requests.get(self.base_url + 'users/' + str(user_id))
        return response.json()
    
    def get_users(self):
        response = requests.get(self.base_url + 'users')
        return response.json()


def main():
    api = LunaAPI()
    user_id = 1
    user = api.get_user(user_id)
    print('User:', user)
    users = api.get_users()
    print('Users:', users)

if __name__ == '__main__':
    main()