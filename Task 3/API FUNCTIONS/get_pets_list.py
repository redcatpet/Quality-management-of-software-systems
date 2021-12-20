import requests

# "key": "003c6904c7f44a085a12f9bf146415bb3d72270254cfd4dc8e0bd1e2"

get_headers_my_pets = {
    "auth_key ": "003c6904c7f44a085a12f9bf146415bb3d72270254cfd4dc8e0bd1e2",
    "filter": "my_pets"
}

get_params_my_pets = get_headers_my_pets

my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"


def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(get_pets_list(my_pets_link, get_params_my_pets, get_headers_my_pets))
