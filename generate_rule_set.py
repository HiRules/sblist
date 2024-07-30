import requests
import json
import os
from aggregate6 import aggregate

simple_site_list = [
    "https://raw.githubusercontent.com/ruijzhan/chnroute/master/gfwlist.txt",
    "https://raw.githubusercontent.com/HiRules/sblist/hidden/custom-site-direct.txt",
    "https://raw.githubusercontent.com/HiRules/sblist/hidden/custom-site-proxy.txt"
]

telegram_ip_list = [
    "https://raw.githubusercontent.com/HiRules/sblist/hidden/telegram.txt"
]

output_dir = "./rule-set"


def convert_site(url: str) -> str:
    r = requests.get(url)
    domain_suffix_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
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


def convert_telegram(url: str) -> str:
    r = requests.get(url)
    ip_cidr_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                ip_cidr_list.append(line)
    result = {
        "version": 1,
        "rules": [
            {
                "ip_cidr": []
            }
        ]
    }
    result["rules"][0]["ip_cidr"] = ip_cidr_list
    filepath = os.path.join(output_dir, url.split("/")[-1] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath
    

def main():
    files = []
    os.mkdir(output_dir)
    for url in simple_site_list:
        filepath = convert_site(url)
        files.append(filepath)
    for url in telegram_ip_list:
        filepath = convert_telegram(url)
        files.append(filepath)
    print("rule-set source generated:")
    for filepath in files:
        print(filepath)
    for filepath in files:
        srs_path = filepath.replace(".json", ".srs")
        os.system("sing-box rule-set compile --output " +
                  srs_path + " " + filepath)
        os.remove(filepath) 


if __name__ == "__main__":
    main()
