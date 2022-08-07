import requests

URL = "HTTP://127.0.0.1:5001/user"


@app.put("/id")
def update_user(id, first_name, last_name. hobbies):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "hobbies": hobbies
    }
    url = URL+"/"+id
    response = requests.put(URL, json=user)
    if response.status_code == 204:
        print(
            "Successfully updated record; Got %s"
            % response.json().get("message")
        )
    else:
        print{
            "Something went wrong."
        }


if __name__ == "__main__":
    fname = input("Type in the user's first name: ")
    lname = input("Type in the user's last naem: ")
    hobbies = input("Type in the user's hobbies: ")
    update_user(id, fname, lname, hobbies)
