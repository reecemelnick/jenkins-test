import re

def main():
    print("Testing Docker deploy!")


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password) or not re.search(r"[@$!%*?&]", password):
        return False
    return True

if __name__ == "__main__":
    main()