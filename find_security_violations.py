import re

def find_security_violations(text):
    violations = []

    # Şifrelerin bulunması için desen
    password_pattern = re.compile(r'\b[A-Za-z0-9@#$%^&+=]{8,}\b')
    passwords = password_pattern.findall(text)
    if passwords:
        violations.append("Potansiyel şifreler bulundu: " + ", ".join(passwords))

    # Kredi kartı numaralarının bulunması için desen
    credit_card_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
    credit_cards = credit_card_pattern.findall(text)
    if credit_cards:
        violations.append("Potansiyel kredi kartı numaraları bulundu: " + ", ".join(credit_cards))

    return violations

if __name__ == "__main__":
    text = input("Taramak istediğiniz metni girin: ")
    security_violations = find_security_violations(text)

    if security_violations:
        print("Güvenlik ihlalleri tespit edildi:")
        for violation in security_violations:
            print(violation)
    else:
        print("Güvenlik ihlali bulunamadı.")
