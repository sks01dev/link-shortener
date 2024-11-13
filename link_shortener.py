from typing import Final
import requests

# Constants
API_KEY: Final[str] = '9dc166a599025f7e10a10ca5d714e5c2e858d'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

def shorten_link(full_link: str):
    # Prepare the payload for the API request
    payload: dict = {'key': API_KEY, 'short': full_link}

    try:
        # Send the GET request to the Cutt.ly API
        response = requests.get(BASE_URL, params=payload)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        
        # Parse the JSON response
        data: dict = response.json()
        
        # Check if the 'url' key is present in the response
        if url_data := data.get('url'):
            
            # Handle the status codes provided
            status_code = url_data.get('status')
            
            if status_code == 7:
                short_link: str = url_data['shortLink']
                print('Success: Your shortened link is:', short_link)
            
            elif status_code == 1:
                print('Error: The link has already been shortened using this service.')
            
            elif status_code == 2:
                print('Error: The entered text is not a valid URL.')
            
            elif status_code == 3:
                print('Error: The preferred link name is already taken.')
            
            elif status_code == 4:
                print('Error: Invalid API key. Please check your API key.')
            
            elif status_code == 5:
                print('Error: The link contains invalid characters or failed validation.')
            
            elif status_code == 6:
                print('Error: The link is from a blocked domain.')
            
            elif status_code == 8:
                print('Error: Monthly link limit reached. Upgrade your plan to shorten more links.')
            
            else:
                print(f'Error: Unknown status code {status_code}.')
        else:
            print('Error: Unexpected API response format.')

    except requests.exceptions.RequestException as e:
        print(f'Error: Failed to connect to the API - {e}')

def main():
    input_link: str = input('Enter a link to shorten: ')
    shorten_link(input_link)

if __name__ == '__main__':
    main()
