import requests
import ipaddress

def is_valid_ip(ip):
    """Return True if `ip` is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def get_ip_location(ip_address):
    """Query ip-api.com for geolocation info and print readable results."""
    # Validate IP first
    if not is_valid_ip(ip_address):
        print(f"Invalid IP address: {ip_address}")
        return

    try:
        url = f"http://ip-api.com/json/{ip_address}"   # Public IP Geolocation API
        resp = requests.get(url, timeout=5)            # Short timeout to avoid hanging
        resp.raise_for_status()                        # Raise for HTTP errors
        data = resp.json()

        # ip-api returns status field; check it
        if data.get("status") != "success":
            print("Lookup failed:", data.get("message", "Unknown error"))
            return

        # Print results safely using .get() to avoid KeyError
        print(f"IP Address: {data.get('query', ip_address)}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Region: {data.get('regionName', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Latitude: {data.get('lat', 'N/A')}")
        print(f"Longitude: {data.get('lon', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Org: {data.get('org', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")

    except requests.Timeout:
        print("Error: Request timed out.")
    except requests.RequestException as e:
        print("Network error:", e)
    except ValueError:
        print("Error: Received invalid JSON from the API.")
    except Exception as e:
        print("Unexpected error:", e)

# ---------------- MAIN ---------------- #

ip = input("Enter an IP address: ").strip()
get_ip_location(ip)

# Example IP for testing: 213.155.225.186
