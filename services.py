import requests

def fetch_product(barcode):
    """
    Fetch product data from OpenFoodFacts API
    """
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("product", None)

    return None