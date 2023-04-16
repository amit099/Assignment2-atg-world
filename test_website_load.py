import requests

def test_atg_website():
    url = 'https://122#%@#%@$@$@%ghgfhfhghffh!$@#@#/'
    print(f"Trying to load {url}")
    response = requests.get(url)
    assert response.status_code == 200, f'Failed to load {url}'
    print(f"{url} loaded successfully!")
