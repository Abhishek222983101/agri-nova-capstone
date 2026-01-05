import requests

url = 'http://localhost:9696/predict'

# Test Case: High Rainfall (Should be Rice)
farmer_data = {
    "N": 90, "P": 42, "K": 43,
    "temperature": 20.8, "humidity": 82.0, 
    "ph": 6.5, "rainfall": 202.9
}

print(f"🚜 Sending data to AgriNova ({url})...")
try:
    response = requests.post(url, json=farmer_data)
    if response.status_code == 200:
        result = response.json()
        print("\n✅ PREDICTION RECEIVED:")
        print(f"   Recommended Crop: {result['recommended_crop'].upper()}")
        print(f"   Status: {result['status']}")
    else:
        print(f"\n❌ Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"\n❌ Connection Failed. Is Docker running? \nError: {e}")
