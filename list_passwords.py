import json
import sys
from pathlib import Path

PASS_DIR = Path.home() / Path(".password-store")


def passwords_list(filter_str):
    passwords = PASS_DIR.glob("**/*.gpg")

    json_data = {"items": []}
    for p in passwords:
        p = str(p.relative_to(PASS_DIR)).split(".gpg")[0]
        if filter_str and filter_str.lower() not in p.lower():
            continue

        json_data["items"].append({"title": p, "arg": p})
    return json.dumps(json_data)


if __name__ == "__main__":
    filter_str = sys.argv[1] if len(sys.argv) > 1 else None
    print(passwords_list(filter_str))
