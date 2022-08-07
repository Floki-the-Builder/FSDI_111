import requests

URL = "http://127.00.1:5001/users"


def create_user(first_name, last_name, hobbies):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "hobbies": hobbies
    }
    response = requests.post(URL, json=user)
    if response.status_code == 201:
        print(
            "Successfully created new record; Get: %s"
            % response.json().get("message")
        )
    else:
        print(
            "Something went wrong while trying to create a new user."
        )


if __name__ == "__main__":
    fname = input("Type in the user's first name: ")
    lname = input("Type in the user's last naem: ")
    hobbies = input("Type in the user's hobbies: ")
    create_user(fname, lname, hobbies)
