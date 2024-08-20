import requests
import json
import os
from aggregate6 import aggregate
from rawFiles import cnsite_filepath, ipv4_filepath, ipv6_filepath

adguard = [
    "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
]

output_dir = "./all"


def convert_site(url: str) -> str:
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
    result["rules"][0]["domain_suffix"] = domain_suffix_list
    filename = url.split("/")[-1]
    filepath = os.path.join(output_dir, filename.rsplit(".",1)[0] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_ip(url: str) -> str:
    r = requests.get(url)
    ip_cidr_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
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
    filename = url.split("/")[-1]
    filepath = os.path.join(output_dir, filename.rsplit(".",1)[0] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_adguard(url: str) -> str:
    r = requests.get(url)
    domain_list = []
    domain_suffix_list = []
    domain_keyword_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if line.strip() == "":
                continue

            if line.startswith("!"):
                continue
            if line.startswith("#"):
                continue

            if line.startswith("@@"):
                continue

            if "*" in line:
                continue
            if "?" in line:
                continue

            if line.endswith("$important"):
                line = line[:-10]

            if line.startswith("://"):
                if line.endswith("^"):
                    domain_list.append(line[3:-1])
                else:
                    print("Warning: " + line)
            elif line.startswith("||"):
                if line.endswith("^"):
                    domain_suffix_list.append(line[2:-1])
                else:
                    domain_keyword_list.append(line[2:])
            elif line.startswith("|"):
                if line.endswith("^"):
                    domain_list.append(line[1:-1])
                else:
                    domain_keyword_list.append(line[1:])
            else:
                if line.endswith("^"):
                    domain_suffix_list.append(line)
    result = {
        "version": 1,
        "rules": [
            {
                "domain": [],
                "domain_keyword": [],
                "domain_suffix": []
            }
        ]
    }
    result["rules"][0]["domain"] = domain_list
    result["rules"][0]["domain_keyword"] = domain_keyword_list
    result["rules"][0]["domain_suffix"] = domain_suffix_list
    filename = url.split("/")[-1]
    filepath = os.path.join(output_dir, filename.split(".")[-2] + ".json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def convert_adguard_unblock(url: str) -> str:
    r = requests.get(url)
    domain_suffix_list = []
    domain_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        print("\n")
        for line in lines:
            if line.strip() == "":
                continue

            if line.startswith("!"):
                continue
            if line.startswith("#"):
                continue

            if "*" in line:
                continue
            if "?" in line:
                continue

            if line.endswith("$important"):
                line = line[:-10]

            if line.startswith("@@||"):
                if line.endswith("^|"):
                    domain_suffix_list.append(line[4:-2])
                elif line.endswith("^"):
                    domain_suffix_list.append(line[4:-1])
                else:
                    print("Warning: " + line)
            elif line.startswith("@@|"):
                if line.endswith("^|"):
                    domain_list.append(line[3:-2])
                elif line.endswith("^"):
                    domain_list.append(line[3:-1])
                else:
                    print("Warning: " + line)
            elif line.startswith("@@"):
                if line.endswith("^|"):
                    domain_suffix_list.append(line[2:-2])
                elif line.endswith("^"):
                    domain_suffix_list.append(line[2:-1])
                else:
                    print("Warning: " + line)
    result = {
        "version": 1,
        "rules": [
            {
                "domain": [],
                "domain_suffix": []
            }
        ]
    }
    result["rules"][0]["domain"] = domain_list
    result["rules"][0]["domain_suffix"] = domain_suffix_list
    filename = url.split("/")[-1]
    filepath = os.path.join(output_dir, filename.split(".")[-2] + ".unblock.json")
    with open(filepath, "w") as f:
        f.write(json.dumps(result, indent=4))
    return filepath


def main():
    files = []
    os.mkdir(output_dir)

    filepath = convert_site(cnsite_filepath)
    files.append(filepath)
    
    filepath = convert_ip(ipv4_filepath)
    files.append(filepath)
    
    filepath = convert_ip(ipv6_filepath)
    files.append(filepath)
  
    for url in adguard:
        filepath = convert_adguard(url)
        files.append(filepath)
        filepath = convert_adguard_unblock(url)
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
