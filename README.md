# Source List：
### Direct-Domain-List(Domains --> cn_site)：
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf \
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf \
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/google.china.conf
### chnroutes2(IPv4 only --> cn_ipv4)：
https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt
### apnic([IPv4 & IPv6] --> [cn_ipv4 & cn_ipv6])：
https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest
### maxmind([IPv4 & IPv6] --> [cn_ipv4 & cn_ipv6])：
https://raw.githubusercontent.com/Dreamacro/maxmind-geoip/release/Country.mmdb
### adguard(Ads Filtering --> [filter and filter_unblock])：
https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt
### iwik([IPv4 & IPv6] --> [cn_ipv4 & cn_ipv6])：
https://www.iwik.org/ipcountry/CN.cidr \
https://www.iwik.org/ipcountry/CN.ipv6
### Gfwlist(Domains --> gfwlist)：
https://raw.githubusercontent.com/ruijzhan/chnroute/master/gfwlist.txt
# Set Relation：
cn_site = accelerated-domains.china + apple.china + google.china \
cn_ipv4 = chnroutes2 + apnic[cn_ipv4] + maxmind[cn_ipv4] + iwik[cn_ipv4] \
cn_ipv6 = apnic[cn_ipv6] + maxmind[cn_ipv6] + iwik[cn_ipv6]
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




