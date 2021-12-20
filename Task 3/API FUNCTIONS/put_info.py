import requests

put_info_headers = {
    "auth_key": "003c6904c7f44a085a12f9bf146415bb3d72270254cfd4dc8e0bd1e2",
    "pet_id": "2a352474-8d13-4ca0-a0e5-ee82fb3ab474"
}

put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "2a352474-8d13-4ca0-a0e5-ee82fb3ab474"


def put_pet_info(link, p_params, p_headers):
    response = requests.put(link,
                            params=p_params,
                            headers=p_headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(put_pet_info(put_info_link, put_info_params, put_info_headers))
