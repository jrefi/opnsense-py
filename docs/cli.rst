CLI Reference
=============

The ``opn`` (and ``opnsense``) command provides a full CLI over the OPNsense REST API.

Quick start
-----------

.. code-block:: bash

   # HTTPS with self-signed certificate (most common)
   opn --host 192.168.1.1 --no-verify-ssl --api-key KEY --api-secret SECRET system status

   # Plain HTTP
   opn --host 192.168.1.1 --no-tls --api-key KEY --api-secret SECRET system status

Configuration file
------------------

Store connection settings in ``~/.config/opnsense-py/config.toml``:

.. code-block:: toml

   [default]
   host = "192.168.1.1"
   api_key = "your-key"
   api_secret = "your-secret"
   verify_ssl = "false"

   [prod]
   host = "firewall.example.com"
   api_key = "prod-key"
   api_secret = "prod-secret"

Switch profiles with ``--profile prod`` or ``OPNSENSE_PROFILE=prod``.

Environment variables
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``OPNSENSE_HOST``
     - Hostname or IP
   * - ``OPNSENSE_API_KEY``
     - API key
   * - ``OPNSENSE_API_SECRET``
     - API secret
   * - ``OPNSENSE_VERIFY_SSL``
     - Set to ``false`` to skip TLS verification
   * - ``OPNSENSE_NO_TLS``
     - Set to ``1`` to use plain HTTP
   * - ``OPNSENSE_PROFILE``
     - Config file profile (default: ``default``)

Output formats
--------------

.. code-block:: bash

   opn -o table firewall alias list   # default: human-readable table
   opn -o json  firewall alias list   # JSON (pipe-friendly)
   opn -o plain firewall alias list   # one value/UUID per line
