# Google Account Creation Automation

![Google Account](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)


This project automates the process of creating a Google account using Python and Selenium. It includes two main components:
1. Fetching a one-time password (OTP) through an API.
2. Automating the Google account creation process using Selenium.

Project Structure
```
google-account-create-/
    ├── README.md
    ├── fetch_otp.py
    └── google_account_create.py
```

Overview of Components

📜 **fetch_otp.py**
This script fetches a one-time password (OTP) using an external OTP API. The OTP is essential for verifying phone numbers during account creation.

#### Key Functions:
- **`get_available_phones(country="USA")`**: Fetches available phone numbers from the specified country.
- **`get_otp(country, phone_number, ago="5m", source="receive-sms-free.cc")`**: Retrieves the OTP for the given phone number.
- **`main()`**: Orchestrates phone number selection and OTP retrieval.

📜 **google_account_create.py**
This script automates the Google account creation process using Selenium. It opens Google’s account creation page and fills out the required information.

#### Features:
- **Generates Unique Username**: Combines first and last names with a random number.
- **Generates Strong Password**: Ensures security by using a mix of characters, numbers, and symbols.
- **Form Automation**: Fills in dynamic fields like date of birth, gender, and username using Selenium.

Requirements
To get started, ensure you have the following installed:
- Python 3.x
- Selenium: Install with `pip install selenium`
- WebDriver for Chrome: [Download from here](https://sites.google.com/chromium.org/driver/)

How to Use
1. **Clone the Repository**:
```bash
git clone https://github.com/yourusername/google-account-create.git
```
2. **Run the OTP Fetcher**:
Fetch the OTP before running the account creation script.
```bash
python fetch_otp.py
```
3. **Run the Google Account Creation Script**:
After obtaining the OTP, you can run the account creation script:
```bash
python google_account_create.py
```

How It Works

### 1. **Fetching OTP**
The script retrieves available phone numbers for a specified country using an OTP API. It then selects a phone number and fetches the OTP, which is required to verify the account.

### 2. **Creating Google Account**
It uses Selenium to navigate Google’s account creation form, entering details such as:
- Name
- Birthday
- Gender
- Username (generated dynamically)
- Password (generated securely)
It bypasses basic bot protection using the `undetected_chromedriver` option.

Customization Options
- **Change the Country**: In `fetch_otp.py`, modify the `country` parameter to select a different country for phone number fetching.
- **Customize User Details**: Modify `google_account_create.py` to set different user details (name, birthday, etc.).

Contact
Feel free to reach out with any questions or contributions!
Email: [hiteshofficial0001@example.com](mailto:hiteshofficial0001@example.com)
