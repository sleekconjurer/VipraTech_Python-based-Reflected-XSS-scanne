# scanner.py

import requests
from urllib.parse import urljoin
from gen import Gen 

X = ["attribute_name", "html_attribute_value", "html_text_node"]

def scan(u: str, p: dict, m: str = 'GET', t=False):
    R = []
    g = Gen()
    M = g.get_marker()

    for C in X:
        for y in g.get_payloads(C):
            
            p_test = {}
            for k, v in p.items():
                p_test[k] = y

            try:
                if m.upper() == 'GET':
                    resp = requests.get(u, params=p_test, timeout=10)
                elif m.upper() == 'POST':
                    resp = requests.post(u, data=p_test, timeout=10)
                else:
                    continue

                if M in resp.text:
                    R.append({
                        "url": resp.url,
                        "payload": y,
                        "param": list(p.keys())[0],
                        "context": C,
                        "status": resp.status_code,
                        "reflect": "found",
                    })

            except requests.exceptions.RequestException as e:
                if not t:
                    print(f"Error scanning {u}: {e}")
                continue

    if not t:
        report(u, R)
        
    return R


def report(u, R):
    print(f"\n--- SCAN REPORT for {u} ---")
    if not R:
        print("PASS: No findings.")
        return

    print(f"FAIL: {len(R)} finding(s) detected!")
    for i, res in enumerate(R):
        print(f"\n- Finding {i+1} -")
        print(f"  Context: **{res['context']}**")
        print(f"  Reflected Payload: {res['payload']}")
        print(f"  HTTP Status: {res['status']}")

if __name__ == '__main__':
    target_url = "http://localhost/vulnerable_app/profile"
    target_params = {"username": "test_user"}

    print(f"Starting scan on: {target_url}")
    scan(target_url, target_params, m='GET')
