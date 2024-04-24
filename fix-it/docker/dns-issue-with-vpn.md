# Dns issue with VPN

## Problem
When using `VPN`/`Zero trust` clients in `MAC OS X` docker is taking ownership of DNS process.

## Cloudflare Zero Trust issue
When using `docker desktop` on  `MAC OS X`, `Cloudflare warp` client fails to register.

```
Status: Unable to Connect
Error reason: DNS Proxy Failure
Error code: CF_DNS_PROXY_FAILURE
Error description: The WARP Agent must be the only process responsible for DNS resolution on the device. One or more processes are already bound to port 53: mDNSResponder.
Learn more: https://cfl.re/CF_DNS_PROXY_FAILURE
```

## Solution
```shell
sudo sed -i '' 's/"kernelForUDP": true/"kernelForUDP": false/' ~/Library/Group\ Containers/group.com.docker/settings.json
```

> [!TIP]
> This could help with other `VPN`/`Zero trust` clients.
