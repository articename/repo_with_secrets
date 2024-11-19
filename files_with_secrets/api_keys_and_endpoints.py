import requests
import json
import time

# API endpoints
API_BASE_URL = "https://api.example.com"
USER_API_ENDPOINT = "/users"
ORDER_API_ENDPOINT = "/orders"

# Authentication credentials (API Keys and Tokens)
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
ACCESS_TOKEN = "ya29.A0ARrdaM9B-VQuUMUwXG6h9hWdt5hFp92SfkA6H0YyD1q2xIEdtlEjcHym3IYbK6cnDtvYP8h4YfOWiZleW-0a-v3lf5VFYD9oSmmXzOmHrR_qFbdfpy"
SECRET_KEY = "6d47d0ff9c7a9ad62f9a6c9a289eb8fcb5ad34c5"

# Sample headers for API requests
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,
}

# Function to fetch user data
def get_user_data(user_id):
    url = f"{API_BASE_URL}{USER_API_ENDPOINT}/{user_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch user data"}

# Function to create an order
def create_order(order_data):
    url = f"{API_BASE_URL}{ORDER_API_ENDPOINT}"
    response = requests.post(url, headers=headers, data=json.dumps(order_data))
    if response.status_code == 201:
        return response.json()
    else:
        return {"error": "Failed to create order"}

# Example usage
if __name__ == "__main__":
    user_data = get_user_data(123)
    print(f"User Data: {user_data}")
    
    order_data = {
        "product_id": 456,
        "quantity": 2,
        "price": 99.99
    }
    order_response = create_order(order_data)
    print(f"Order Response: {order_response}")
