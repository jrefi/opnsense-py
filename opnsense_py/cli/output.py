from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel

from opnsense_py.models.base import ApiResponse, OPNsenseModel, SearchResponse


def render(data: Any, fmt: str) -> str:
    """Render API response data as a string in the requested format.

    Args:
        data: A SearchResponse, ApiResponse, OPNsenseModel, list, or dict.
        fmt: One of "table", "json", "plain".
    """
    if fmt == "json":
        return _to_json(data)
    if fmt == "plain":
        return _to_plain(data)
    return _to_table(data)


# ---------------------------------------------------------------------------
# JSON
# ---------------------------------------------------------------------------


def _to_json(data: Any) -> str:
    return json.dumps(_to_dict(data), indent=2)


# ---------------------------------------------------------------------------
# Plain (one value per line — good for shell pipelines)
# ---------------------------------------------------------------------------


def _to_plain(data: Any) -> str:
    if isinstance(data, SearchResponse):
        rows = [_to_dict(r) for r in data.rows]
        return "\n".join(str(r.get("uuid", r)) for r in rows)
    if isinstance(data, ApiResponse):
        parts = []
        if data.result:
            parts.append(data.result)
        if data.uuid:
            parts.append(data.uuid)
        return "\n".join(parts)
    if isinstance(data, OPNsenseModel):
        d = _to_dict(data)
        return "\n".join(f"{k}: {v}" for k, v in d.items() if v is not None)
    if isinstance(data, dict):
        if "rows" in data and isinstance(data["rows"], list):
            return "\n".join(str(r) for r in data["rows"])
        return "\n".join(f"{k}: {v}" for k, v in data.items())
    if isinstance(data, list):
        return "\n".join(str(item) for item in data)
    return str(data)


# ---------------------------------------------------------------------------
# Table
# ---------------------------------------------------------------------------


def _to_table(data: Any) -> str:
    try:
        from tabulate import tabulate
    except ImportError:
        # Fall back to a minimal built-in table if tabulate is not installed
        return _simple_table(data)

    if isinstance(data, SearchResponse):
        rows = [_to_dict(r) for r in data.rows]
        if not rows:
            return "(no results)"
        return tabulate(rows, headers="keys", tablefmt="simple")

    if isinstance(data, ApiResponse):
        rows = [{"result": data.result, "uuid": data.uuid}]
        return tabulate(rows, headers="keys", tablefmt="simple")

    if isinstance(data, OPNsenseModel):
        d = _to_dict(data)
        rows = [{"field": k, "value": v} for k, v in d.items() if v is not None]
        return tabulate(rows, headers="keys", tablefmt="simple")

    if isinstance(data, list):
        if not data:
            return "(no results)"
        if isinstance(data[0], dict):
            return tabulate(data, headers="keys", tablefmt="simple")
        return "\n".join(str(item) for item in data)

    if isinstance(data, dict):
        # Unwrap OPNsense search-style dicts: {"rows": [...], "total": N, ...}
        if "rows" in data and isinstance(data["rows"], list):
            rows = data["rows"]
            if not rows:
                return "(no results)"
            return tabulate(rows, headers="keys", tablefmt="simple")
        rows = [{"field": k, "value": v} for k, v in data.items()]
        return tabulate(rows, headers="keys", tablefmt="simple")

    return str(data)


def _simple_table(data: Any) -> str:
    """Minimal table renderer used when tabulate is not installed."""
    if isinstance(data, SearchResponse):
        rows = [_to_dict(r) for r in data.rows]
    elif isinstance(data, ApiResponse):
        rows = [{"result": data.result, "uuid": data.uuid}]
    elif isinstance(data, OPNsenseModel):
        d = _to_dict(data)
        rows = [{"field": k, "value": v} for k, v in d.items() if v is not None]
    elif isinstance(data, list):
        rows = [item if isinstance(item, dict) else {"value": item} for item in data]
    elif isinstance(data, dict):
        if "rows" in data and isinstance(data["rows"], list):
            rows = data["rows"]
        else:
            rows = [{"field": k, "value": v} for k, v in data.items()]
    else:
        return str(data)

    if not rows:
        return "(no results)"

    headers = list(rows[0].keys())
    col_widths = {h: len(h) for h in headers}
    for row in rows:
        for h in headers:
            col_widths[h] = max(col_widths[h], len(str(row.get(h, "") or "")))

    fmt = "  ".join(f"{{:<{col_widths[h]}}}" for h in headers)
    lines = [fmt.format(*headers)]
    lines.append("  ".join("-" * col_widths[h] for h in headers))
    for row in rows:
        lines.append(fmt.format(*[str(row.get(h, "") or "") for h in headers]))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _to_dict(obj: Any) -> dict[str, Any]:
    if isinstance(obj, BaseModel):
        return obj.model_dump(exclude_none=True)
    if isinstance(obj, dict):
        return obj
    return {"value": str(obj)}
