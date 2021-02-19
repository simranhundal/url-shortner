import requests
# getting user input for link
print("Enter Url to be shortened")
url = input()

# hiding my api key use provided executable file for testing
api_key = "my api key"
# using cuttly api with key and given url to make shortened link
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

# response is given as json 
response = requests.get(api_url).json()["url"]

# various error checking if link is not valid
if response["status"] == 7:
    print("Shortened URL is:  ", response["shortLink"])
elif response["status"] == 2:
    print("Error link is incorrect")
elif response["status"] == 1:
    print("Error link is already shortened")
else:
    print("error")
