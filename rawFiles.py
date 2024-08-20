import math
import re
import maxminddb
import requests
import os
from aggregate6 import aggregate

dnsmasq_china_list = [
    "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf",
    "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf",
    "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/google.china.conf"
]

chnroutes2 = [
    "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
]

iwik = [
    "https://www.iwik.org/ipcountry/CN.cidr",
    "https://www.iwik.org/ipcountry/CN.ipv6"
]

apnic = [
    "https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest"
]

maxmind = [
    "https://raw.githubusercontent.com/Dreamacro/maxmind-geoip/release/Country.mmdb"
]

output_dir = "./all"
cnsite_filepath = ipv4_filepath = ipv6_filepath = "test"

def convert_dnsmasq(url: str) -> str:
    r = requests.get(url)
    domain_suffix_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                domain = re.match(r"server=\/(.*)\/(.*)", line)
                if domain:
                    domain_suffix_list.append(domain.group(1))
    result = domain_suffix_list
    filename = url.split("/")[-1]
    filepath = os.path.join(output_dir, filename.rsplit(".",1)[0] + ".txt")
    with open(filepath, "w") as f:
        f.write("\n".join(result))
    return filepath


def convert_chnroutes2(url: str) -> str:
    r = requests.get(url)
    ip_cidr_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                ip_cidr_list.append(line)
    result = ip_cidr_list
    filename = url.split("/")[-1]
    filepath = os.path.join(output_dir, filename.split(".")[-2] + ".txt")
    with open(filepath, "w") as f:
        f.write("\n".join(result))
    return filepath


def convert_iwik(url: str) -> str:
    filename = os.path.basename(url)
    suffix = os.path.splitext(filename)[1]
    ip_version = ""
    if suffix == ".cidr":
        ip_version = "ipv4"
    else:
        ip_version = "ipv6"
    r = requests.get(url)
    ip_cidr_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                ip_cidr_list.append(line)
    result = ip_cidr_list
    filepath = os.path.join(output_dir, "iwik-" + ip_version + ".txt")
    with open(filepath, "w") as f:
        f.write("\n".join(result))
    return filepath


def convert_apnic(url: str, country_code: str, ip_version: str) -> str:
    r = requests.get(url)
    ip_cidr_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#"):
                if line.split("|")[1] == country_code and line.split("|")[2] == ip_version:
                    if ip_version == "ipv4":
                        ip_cidr_list.append(line.split(
                            "|")[3] + "/" + str(32 - int(math.log2(int(line.split("|")[4])))))
                    else:
                        ip_cidr_list.append(line.split(
                            "|")[3] + "/" + line.split("|")[4])
    result = aggregate(ip_cidr_list)
    filepath = os.path.join(output_dir, "apnic-" +
                            country_code.lower() + "-" + ip_version + ".txt")
    with open(filepath, "w") as f:
        f.write("\n".join(result))
    return filepath


def convert_maxmind(url: str, country_code: str, ip_version: str) -> str:
    r = requests.get(url)
    with open("Country.mmdb", "wb") as f:
        f.write(r.content)
    f.close()
    reader = maxminddb.open_database("Country.mmdb")
    ip_cidr_list = []
    for cidr, info in reader.__iter__():
        if info.get("country") is not None:
            if info["country"]["iso_code"] == country_code:
                if ip_version == "ipv4" and cidr.version == 4:
                    ip_cidr_list.append(str(cidr))
                elif ip_version == "ipv6" and cidr.version == 6:
                    ip_cidr_list.append(str(cidr))
        elif info.get("registered_country") is not None:
            if info["registered_country"]["iso_code"] == country_code:
                if ip_version == "ipv4" and cidr.version == 4:
                    ip_cidr_list.append(str(cidr))
                elif ip_version == "ipv6" and cidr.version == 6:
                    ip_cidr_list.append(str(cidr))
    reader.close()
    result = aggregate(ip_cidr_list)
    filepath = os.path.join(output_dir, "maxmind-" +
                            country_code.lower() + "-" + ip_version + ".txt")
    with open(filepath, "w") as f:
        f.write("\n".join(result))
    return filepath


def merge_lists(filename, kv, *lists):
    result = set()
    for i in range(len(lists)):
        with open(lists[i],"r",encoding="utf-8") as R:
            for line in R:
                result.add(line.strip())
    result = list(result)
    result.sort(key = kv)
    filepath = os.path.join(output_dir, filename + ".txt")
    with open(filepath,"w",encoding="utf-8") as W:
        for line in result:
            W.write(line + "\n")
    return filepath




#def main():
    files = []
    site_kv = lambda x: (x.split('.')[0])
    ipv4_kv = lambda x: (x.split('.')[0], x.split('.')[1], x.split('.')[2])
    ipv6_kv = lambda x: (x.split(':')[0], x.split(':')[1])
    os.mkdir(output_dir)
    for url in dnsmasq_china_list:
        filepath = convert_dnsmasq(url)
        files.append(filepath)
    for url in chnroutes2:
        filepath = convert_chnroutes2(url)
        files.append(filepath)
    for url in iwik:
        filepath = convert_iwik(url)
        files.append(filepath)
    for url in apnic:
        filepath = convert_apnic(url, "CN", "ipv4")
        files.append(filepath)
        filepath = convert_apnic(url, "CN", "ipv6")
        files.append(filepath)
    for url in maxmind:
        filepath = convert_maxmind(url, "CN", "ipv4")
        files.append(filepath)
        filepath = convert_maxmind(url, "CN", "ipv6")
        files.append(filepath)

    # files[0] = os.path.join(output_dir, accelerated-domains.china.txt)
    # files[1] = os.path.join(output_dir, apple.china.txt)
    # files[2] = os.path.join(output_dir, google.china.txt)
    # files[3] = os.path.join(output_dir, chnroutes.txt)
    # files[4] = os.path.join(output_dir, iwik-ipv4.txt)
    # files[5] = os.path.join(output_dir, iwik-ipv6.txt)
    # files[6] = os.path.join(output_dir, apnic-cn-ipv4.txt)
    # files[7] = os.path.join(output_dir, apnic-cn-ipv6.txt)
    # files[8] = os.path.join(output_dir, maxmind-cn-ipv4.txt)
    # files[9] = os.path.join(output_dir, maxmind-cn-ipv6.txt)
    
    merge_site_lists = [files[0], files[1], files[2]]
    cnsite_filepath = merge_lists("cnsite", site_kv, *merge_site_lists)
    files.append(cnsite_filepath)

    merge_ipv4_lists = [files[3], files[4], files[6], files[8]]
    ipv4_filepath = merge_lists("cnipv4", ipv4_kv, *merge_ipv4_lists)
    files.append(ipv4_filepath)

    merge_ipv6_lists = [files[5], files[7], files[9]]
    ipv6_filepath = merge_lists("cnipv6", ipv6_kv, *merge_ipv6_lists)
    files.append(ipv6_filepath)
    print(requests.get(cnsite_filepath).status_code)


    print("raw files generated:")
    for filepath in files:
        print(filepath)


#if __name__ == "__main__":
#    main()
