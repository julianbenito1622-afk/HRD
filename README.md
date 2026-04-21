# HRD - Home Router Daemon

> Open source ISP management system for small providers. Built on Debian.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Debian-red)

## What is HRD?

HRD is a complete management system for small ISPs. It replaces Excel spreadsheets and manual MikroTik configuration with a single API that runs on any Debian server.

## Features

- ✅ Client management (add, list, delete)
- ✅ MikroTik integration (cut/activate internet per client)
- ✅ Network monitoring (ping nodes, detect outages)
- ✅ REST API with auto-documentation
- ✅ PostgreSQL database
- ✅ One-command install

## Install

```bash
curl -s https://raw.githubusercontent.com/julianbenito1622-afk/HRD/master/install.sh | bash
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /clientes | List all clients |
| POST | /clientes | Create client |
| DELETE | /clientes/{id} | Delete client |
| POST | /mikrotik/cortar/{ip} | Cut client internet |
| POST | /mikrotik/activar/{ip} | Activate client internet |
| GET | /mikrotik/conectados | List connected devices |
| POST | /monitor/ping | Monitor network nodes |

## Requirements

- Debian 11+ or Ubuntu 20+
- MikroTik router with API enabled
- 1GB RAM minimum

## Author

Built by [r00t](https://github.com/julianbenito1622-afk) — Lima, Peru 🇵🇪

## License

MIT — free to use, modify and distribute.