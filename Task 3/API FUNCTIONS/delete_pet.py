import requests

delete_pet_headers = {
    "auth_key": "f4ef93427ed53b1c6cdcfe1baacd851c117a2eb339c70c041d38d86c",
    "pet_id": "47df3852-8b69-4949-85b1-f5ea97a7c0af"
}

delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "47df3852-8b69-4949-85b1-f5ea97a7c0af"


def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(delete_pet(DELETE_pet_link, delete_pet_params, delete_pet_headers))
