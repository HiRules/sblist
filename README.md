## Source List：

### Direct-Domain-List(Domains)：
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf \
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf \
https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/google.china.conf

### chnroutes2(IPv4 only)：
https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt

### apnic(IPv4 and IPv6)：
https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest

### maxmind(IPv4 and IPv6)：
https://raw.githubusercontent.com/Dreamacro/maxmind-geoip/release/Country.mmdb

### adguard(Ads Filtering)：：
https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt

### iwik(IPv4 and IPv6)：
https://www.iwik.org/ipcountry/CN.cidr \
https://www.iwik.org/ipcountry/CN.ipv6

### Gfwlist(Domains)：
https://raw.githubusercontent.com/ruijzhan/chnroute/master/gfwlist.txt

## srs files：
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






