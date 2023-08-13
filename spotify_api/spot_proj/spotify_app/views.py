from django.shortcuts import render
from django.http import JsonResponse
from spotify_api.spot_proj.spotify import *  # Assuming you have a Spotify class defined in spotify.py

def search_for_artist(request):
    if request.method == 'GET':
        # Get the artist name from the query parameters
        artist_name = request.GET.get('artist_name', None)

        if artist_name:
            # Create an instance of the Spotify class
            spotify = Spotify()

            # Call the relevant method to search for the artist
            artist_data = spotify.search_artist(artist_name)

            # Return the data as a JSON response
            return JsonResponse(artist_data)

        else:
            return JsonResponse({'error': 'Please provide an artist name in the query parameters.'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)




search_for_artist("Drake")