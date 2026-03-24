Library Usage
=============

.. code-block:: python

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

Architecture
------------

The client is structured in layers:

1. **OPNsenseClient** — top-level entry point; manages an ``httpx.Client`` with Basic Auth.
   All API modules are lazy-loaded as ``@cached_property`` attributes.

2. **BaseModule** — base class providing generic CRUD helpers (``_search``, ``_get_item``,
   ``_add_item``, etc.) and service control helpers.

3. **Module classes** (``modules/core/``, ``modules/plugins/``) — one per OPNsense subsystem,
   returning typed Pydantic models.

4. **Pydantic models** (``models/``) — typed representations of OPNsense entities; all extend
   ``OPNsenseModel`` with ``extra="allow"`` so unrecognised fields are preserved.

5. **Exceptions** — ``OPNsenseError`` → ``OPNsenseHTTPError`` → ``OPNsenseAuthError`` /
   ``OPNsenseNotFoundError``; plus ``OPNsenseValidationError`` for HTTP 200 responses with
   validation errors.
