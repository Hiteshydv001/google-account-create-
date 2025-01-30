import requests
import random

# Base URL for the OTP API
API_BASE_URL = "https://otp-api.shelex.dev/api"

def get_available_phones(country="USA"):
    """Fetch a list of available phone numbers for a given country."""
    url = f"{API_BASE_URL}/list/{country}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            phones = data.get("phones", [])
            if phones:
                print(f"Found {len(phones)} phone numbers for {country}.")
                return phones
            else:
                print(f"No phone numbers available for {country}.")
                return []
        else:
            print(f"Failed to fetch phone numbers. Status code: {response.status_code}")
            print("Response content:", response.text)
            return []
    except Exception as e:
        print(f"An error occurred while fetching phone numbers: {e}")
        return []

def get_otp(country, phone_number, ago="5m", source="receive-sms-free.cc"):
    """Fetch OTP for a given phone number."""
    url = f"{API_BASE_URL}/{country}/{phone_number}"
    params = {"ago": ago, "source": source}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            print("API Response:", data)  # Debugging output
            otp = data.get("result", {}).get("otp")
            if otp:
                print(f"Retrieved OTP: {otp}")
                return otp
            else:
                print("No OTP available in the response.")
                return None
        else:
            print(f"Failed to fetch OTP. Status code: {response.status_code}")
            print("Response content:", response.text)
            return None
    except Exception as e:
        print(f"An error occurred while fetching OTP: {e}")
        return None

def main():
    # Step 1: Fetch available phone numbers
    country = "USA"  # Change the country if needed
    phones = get_available_phones(country)
    if not phones:
        print("No phone numbers available. Exiting.")
        return

    # Step 2: Randomly select a phone number
    selected_phone = random.choice(phones)
    phone_number = selected_phone.get("value")
    url = selected_phone.get("url")
    print(f"Selected phone number: {phone_number}")
    print(f"Phone number source URL: {url}")

    # Step 3: Fetch OTP for the selected phone number
    otp = get_otp(country, phone_number)
    if otp:
        print(f"Successfully retrieved OTP: {otp}")
    else:
        print("Failed to retrieve OTP.")

if __name__ == "__main__":
    main()
