# Source List：
### Direct-Domain-List：
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf \
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf \
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/google.china.conf
### GeoIP2-CN：
https://raw.githubusercontent.com/Hackl0us/GeoIP2-CN/release/CN-ip-cidr.txt
### chnroutes2：
https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt
### apnic：
https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest
### maxmind：
https://raw.githubusercontent.com/Dreamacro/maxmind-geoip/release/Country.mmdb
### adguard：
https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt
### iwik：
https://www.iwik.org/ipcountry/CN.cidr \
https://www.iwik.org/ipcountry/CN.ipv6
### Gfwlist：
https://raw.githubusercontent.com/ruijzhan/chnroute/master/gfwlist.txt


# srs files：
```json
      {
        "tag": "filter_unblock",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/HiRules/sblist/release/filter_unblock.srs",
        "download_detour": "proxy"
      },
      {
        "tag": "filter",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/HiRules/sblist/release/filter.srs",
        "download_detour": "proxy"
      },
      {
        "tag": "cn_ipv4",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/HiRules/sblist/release/cn_ipv4.srs",
        "download_detour": "proxy"
      },
      {
        "tag": "cn_ipv6",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/HiRules/sblist/release/cn_ipv6.srs",
        "download_detour": "proxy"
      },
      {
        "tag": "cn_site",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/HiRules/sblist/release/cn_site.srs",
        "download_detour": "proxy"
      },
      {
        "tag": "gfwlist",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/HiRules/sblist/release/gfwlist.srs",
        "download_detour": "proxy"
      }
```
# Thanks to：
[@Dreista/sing-box-rule-set-cn](https://github.com/Dreista/sing-box-rule-set-cn) \
[@ruijzhan/chnroute](https://github.com/ruijzhan/chnroute) \
[@felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list) \
[@misakaio/chnroutes2](https://github.com/misakaio/chnroutes2) \
[@Dreamacro/maxmind-geoip](https://github.com/Dreamacro/maxmind-geoip) \
[@AdguardTeam/AdguardFilters](https://github.com/AdguardTeam/AdguardFilters)
[@Hackl0us/GeoIP2-CN](https://github.com/Hackl0us/GeoIP2-CN)




