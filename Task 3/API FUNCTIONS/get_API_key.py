import requests

get_key_headers = {
    "email": "abc1234@mail.ru",
    "password": "abc1234"
}

get_key_params = get_key_headers

api_key_link = "https://petfriends1.herokuapp.com/api/key"

def get_api_key(link, params, headers):

    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text

print(get_api_key(api_key_link, get_key_params, get_key_headers))