import requests


def get_ip_location(ip):

    try:

        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=5
        )

        data = response.json()

        if data.get("status") != "success":
            return {
                "country": None,
                "city": None,
                "latitude": None,
                "longitude": None,
                "timezone": None
            }
            
        return {
            "country": data.get("country"),
            "city": data.get("city"),
            "latitude": data.get("lat"),
            "longitude": data.get("lon"),
            "timezone": data.get("timezone")
        }

    except Exception:

        return {
            "country": None,
            "city": None,
            "latitude": None,
            "longitude": None,
            "timezone": None
        }