# opnsense-py

A synchronous Python client library and CLI for the [OPNsense](https://opnsense.org) REST API.

## Installation

```bash
# Library only
pip install opnsense-py

# Library + CLI (opn / opnsense commands)
pip install opnsense-py[cli]
```

Requires Python 3.12+.

## CLI quick start

```bash
# HTTPS with self-signed certificate (most common)
opn --host 192.168.1.1 --no-verify-ssl --api-key KEY --api-secret SECRET system status

# Plain HTTP
opn --host 192.168.1.1 --no-tls --api-key KEY --api-secret SECRET system status
```

### Configuration file

Store connection settings in `~/.config/opnsense-py/config.toml` to avoid repeating flags:

```toml
[default]
host = "192.168.1.1"
api_key = "your-key"
api_secret = "your-secret"
verify_ssl = "false"

[prod]
host = "firewall.example.com"
api_key = "prod-key"
api_secret = "prod-secret"
```

Switch profiles with `--profile prod` or `OPNSENSE_PROFILE=prod`.

### Environment variables

| Variable | Description |
|---|---|
| `OPNSENSE_HOST` | Hostname or IP |
| `OPNSENSE_API_KEY` | API key |
| `OPNSENSE_API_SECRET` | API secret |
| `OPNSENSE_VERIFY_SSL` | Set to `false` to skip TLS verification |
| `OPNSENSE_NO_TLS` | Set to `1` to use plain HTTP |
| `OPNSENSE_PROFILE` | Config file profile (default: `default`) |

### Output formats

```bash
opn -o table firewall alias list   # default: human-readable table
opn -o json  firewall alias list   # JSON (pipe-friendly)
opn -o plain firewall alias list   # one value/UUID per line
```

### Available commands

| Command | Description |
|---|---|
| `auth` | Users, groups, API keys |
| `captiveportal` | Captive portal zones, sessions, vouchers |
| `cron` | Cron jobs |
| `dhcrelay` | DHCP relay |
| `diagnostics` | ARP, routes, interfaces, firewall states, traffic |
| `dnsmasq` | Dnsmasq DNS/DHCP host entries and domain overrides |
| `firewall` | Aliases, rules, NAT (DNAT/SNAT) |
| `firmware` | Firmware updates and package management |
| `haproxy` | HAProxy frontends, backends, servers |
| `hostdiscovery` | Network host scanning |
| `ids` | Suricata IDS/IPS policies, rules, alerts |
| `ipsec` | IPsec VPN connections, child SAs, sessions |
| `kea` | Kea DHCP subnets and reservations |
| `monit` | Monit service checks, tests, alerts |
| `ntpd` | NTP daemon status |
| `openvpn` | OpenVPN instances, overwrites, sessions |
| `radvd` | Router Advertisement daemon |
| `routes` | Static routes |
| `routing` | Gateway definitions |
| `syslog` | Remote syslog destinations |
| `system` | System status, services, tunables, backups, reboot |
| `trafficshaper` | Traffic shaper pipes, queues, rules |
| `trust` | Certificate authorities, certificates, CRLs |
| `unbound` | Unbound DNS resolver hosts, forwards, ACLs |
| `wireguard` | WireGuard VPN servers and peers |

Run any command with `--help` for full usage.

## Library usage

```python
from opnsense_py import OPNsenseClient

with OPNsenseClient(
    host="192.168.1.1",
    api_key="your-key",
    api_secret="your-secret",
    verify_ssl=False,
) as client:
    # List firewall aliases
    aliases = client.firewall.search_aliases()
    for alias in aliases.rows:
        print(alias.name, alias.type)

    # Add a cron job
    from opnsense_py.models.cron import CronJob
    result = client.cron.add_job(CronJob(
        command="firmware",
        description="Nightly firmware check",
        minutes="0", hours="2",
        days="*", months="*", weekdays="*",
    ))
    print(result.uuid)
```

### Architecture

The client is structured in layers:

1. **`OPNsenseClient`** — top-level entry point; manages an `httpx.Client` with Basic Auth. All API modules are lazy-loaded as `@cached_property` attributes.
2. **`BaseModule`** — base class providing generic CRUD helpers (`_search`, `_get_item`, `_add_item`, etc.) and service control helpers.
3. **Module classes** (`modules/core/`, `modules/plugins/`) — one per OPNsense subsystem, returning typed Pydantic models.
4. **Pydantic models** (`models/`) — typed representations of OPNsense entities; all extend `OPNsenseModel` with `extra="allow"` so unrecognised fields are preserved.
5. **Exceptions** — `OPNsenseError` → `OPNsenseHTTPError` → `OPNsenseAuthError` / `OPNsenseNotFoundError`; plus `OPNsenseValidationError` for HTTP 200 responses with validation errors.

## Development

```bash
# Install with dev dependencies
poetry install --extras cli

# Run tests
poetry run pytest

# Lint
poetry run ruff check .

# Type check
poetry run mypy opnsense_py/

# Run a single test
poetry run pytest tests/unit/modules/core/test_cron.py::test_search_jobs
```

Integration tests require a live OPNsense instance and are skipped by default:

```bash
OPNSENSE_HOST=192.168.1.1 OPNSENSE_API_KEY=... OPNSENSE_API_SECRET=... \
  poetry run pytest -m integration
```
