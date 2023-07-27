import requests

class Spotify:

    def __init__(self, token: str):
        self.token = token

    # Header that uses token
    def get_auth_header(self) -> dict:
        return {"Authorization": "Bearer " + self.token}

    def search_for_artist(self, artist_name: str) -> dict:
        url = "https://api.spotify.com/v1/search"
        header = self.get_auth_header()
        query = f"?q={artist_name}&type=artist&limit=3"

        query_url = url + query
        result = requests.get(query_url, headers=header)
        json_result = result.json()
        
        return json_result