import requests
import json
import os
from aggregate6 import aggregate

dnsmasq_china_list = [
    "https://raw.githubusercontent.com/hilist/sblist/hidden/site-green.txt",
    "https://raw.githubusercontent.com/hilist/sblist/hidden/site-red.txt"
]

output_dir = "./rule-set"


def convert_dnsmasq(url: str) -> str:
    r = requests.get(url)
    domain_suffix_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            domain_suffix_list.append(line)
    result = {
        "version": 1,
        "rules": [
            {
                "domain_suffix": []
            }
        ]
    }
    filename = url.split("/")[-1]
    result["rules"][0]["domain_suffix"] = domain_suffix_list
    filepath = os.path.join(output_dir, filename.split(".")[-2] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath



def main():
    files = []
    os.mkdir(output_dir)
    for url in dnsmasq_china_list:
        filepath = convert_dnsmasq(url)
        files.append(filepath)
    print("rule-set source generated:")
    for filepath in files:
        print(filepath)
    for filepath in files:
        srs_path = filepath.replace(".json", ".srs")
        os.system("sing-box rule-set compile --output " +
                  srs_path + " " + filepath)


if __name__ == "__main__":
    main()
