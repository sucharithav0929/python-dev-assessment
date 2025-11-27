import requests


def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
            response = requests.get(url)

            if response.status_code != 200:
                print("User not found")
                return None

            users = response.json()
            for i in range(num_users):
                try:
                    user = users[i]
                    name = user["name"]
                    email = user["email"]
                    city = user["address"]["city"]

                    print("Name:",name)
                    print("Email:",email)
                    print("City:",city)
                except IndexError:
                    print("Number of users exceeded")
                    break
    except requests.exceptions.RequestException as e:
            print("Network Error: ", e)
            return None

if __name__ == "__main__":
    print("Fetching 3 users:\n")
    fetch_and_display_users(3)

    print("\nFetching 15 users (out of bounds test):\n")
    fetch_and_display_users(15)


