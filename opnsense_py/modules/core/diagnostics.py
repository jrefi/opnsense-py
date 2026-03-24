from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.modules.base import BaseModule

_M = "diagnostics"


class DiagnosticsModule(BaseModule):
    """Wrapper for the OPNsense Diagnostics API."""

    # -- Activity ----------------------------------------------------------

    def get_activity(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/activity/get_activity")

    # -- CPU Usage ---------------------------------------------------------

    def get_cpu_type(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/cpu_usage/get_c_p_u_type")

    # -- DNS ---------------------------------------------------------------

    def reverse_lookup(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/dns/reverse_lookup")

    # -- DNS Diagnostics ---------------------------------------------------

    def get_dns_diagnostics(self) -> dict[str, Any]:
        return self._get_config(_M, "dns_diagnostics")

    def set_dns_diagnostics(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "dns_diagnostics", data)

    # -- Firewall ----------------------------------------------------------

    def get_firewall_log(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/firewall/log")

    def get_firewall_log_filters(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/firewall/log_filters")

    def get_pf_states(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/firewall/pf_states")

    def get_pf_statistics(self, section: str | None = None) -> dict[str, Any]:
        path = f"{_M}/firewall/pf_statistics"
        if section:
            path = f"{path}/{section}"
        return self._client._get(path)

    def get_firewall_stats(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/firewall/stats")

    def list_rule_ids(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/firewall/list_rule_ids")

    def query_states(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._client._post(f"{_M}/firewall/query_states", json=data or {})

    def query_pf_top(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._client._post(f"{_M}/firewall/query_pf_top", json=data or {})

    def del_state(self, state_id: str, creator_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/firewall/del_state/{state_id}/{creator_id}")
        return ApiResponse.model_validate(raw)

    def flush_states(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/firewall/flush_states"))

    def flush_sources(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/firewall/flush_sources"))

    def kill_states(self, data: dict[str, Any] | None = None) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/firewall/kill_states", json=data or {}))

    # -- Interface ---------------------------------------------------------

    def get_arp(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_arp")

    def search_arp(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/search_arp")

    def flush_arp(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/interface/flush_arp"))

    def get_ndp(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_ndp")

    def search_ndp(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/search_ndp")

    def get_routes(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_routes")

    def del_route(self, data: dict[str, Any] | None = None) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/interface/del_route", json=data or {}))

    def get_interface_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_interface_config")

    def get_interface_names(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_interface_names")

    def get_interface_statistics(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_interface_statistics")

    def get_bpf_statistics(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_bpf_statistics")

    def get_memory_statistics(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_memory_statistics")

    def get_netisr_statistics(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_netisr_statistics")

    def get_pfsync_nodes(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_pfsync_nodes")

    def get_protocol_statistics(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_protocol_statistics")

    def get_socket_statistics(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_socket_statistics")

    def get_vip_status(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/interface/get_vip_status")

    def set_carp_status(self, status: str) -> ApiResponse:
        """Note: maps to /_carp_status in the API path."""
        raw = self._client._post(f"{_M}/interface/_carp_status/{status}")
        return ApiResponse.model_validate(raw)

    # -- LV Template -------------------------------------------------------

    def search_lv_templates(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "lvtemplate", "search_item", request)

    def get_lv_template(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "lvtemplate", "get_item", uuid)

    def add_lv_template(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "lvtemplate", "add_item", data)

    def set_lv_template(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "lvtemplate", "set_item", uuid, data)

    def del_lv_template(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "lvtemplate", "del_item", uuid)

    def get_lv_template_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/lvtemplate/get")

    def set_lv_template_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/lvtemplate/set", json=data)
        return ApiResponse.model_validate(raw)

    # -- Netflow -----------------------------------------------------------

    def get_netflow_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/netflow/getconfig")

    def set_netflow_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/netflow/setconfig")

    def netflow_cache_stats(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/netflow/cache_stats")

    def netflow_is_enabled(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/netflow/is_enabled")

    def netflow_status(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/netflow/status")

    def netflow_reconfigure(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/netflow/reconfigure"))

    # -- Network Insight ---------------------------------------------------

    def networkinsight_export(
        self,
        provider: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        resolution: str | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {}
        if provider:
            params["provider"] = provider
        if from_date:
            params["from_date"] = from_date
        if to_date:
            params["to_date"] = to_date
        if resolution:
            params["resolution"] = resolution
        return self._client._get(f"{_M}/networkinsight/export", params=params)

    def networkinsight_interfaces(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/networkinsight/get_interfaces")

    def networkinsight_metadata(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/networkinsight/get_metadata")

    def networkinsight_protocols(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/networkinsight/get_protocols")

    def networkinsight_services(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/networkinsight/get_services")

    def networkinsight_timeserie(self, **kwargs: Any) -> dict[str, Any]:
        return self._client._get(f"{_M}/networkinsight/timeserie", params=kwargs)

    def networkinsight_top(self, **kwargs: Any) -> dict[str, Any]:
        return self._client._get(f"{_M}/networkinsight/top", params=kwargs)

    # -- Packet Capture ----------------------------------------------------

    def get_packet_capture_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/packet_capture/get")

    def set_packet_capture_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/packet_capture/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_packet_capture_jobs(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/packet_capture/search_jobs")

    def start_packet_capture(self, job_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/packet_capture/start/{job_id}")
        return ApiResponse.model_validate(raw)

    def stop_packet_capture(self, job_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/packet_capture/stop/{job_id}")
        return ApiResponse.model_validate(raw)

    def remove_packet_capture(self, job_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/packet_capture/remove/{job_id}")
        return ApiResponse.model_validate(raw)

    def download_packet_capture(self, job_id: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/packet_capture/download/{job_id}")

    def view_packet_capture(self, job_id: str, detail: str = "normal") -> dict[str, Any]:
        return self._client._get(f"{_M}/packet_capture/view/{job_id}/{detail}")

    def mac_info(self, mac_addr: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/packet_capture/mac_info/{mac_addr}")

    # -- Ping --------------------------------------------------------------

    def get_ping_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/ping/get")

    def set_ping_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/ping/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_ping_jobs(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/ping/search_jobs")

    def start_ping(self, job_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/ping/start/{job_id}")
        return ApiResponse.model_validate(raw)

    def stop_ping(self, job_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/ping/stop/{job_id}")
        return ApiResponse.model_validate(raw)

    def remove_ping(self, job_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/ping/remove/{job_id}")
        return ApiResponse.model_validate(raw)

    # -- Port Probe --------------------------------------------------------

    def get_portprobe_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/portprobe/get")

    def set_portprobe_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/portprobe/set", json=data)
        return ApiResponse.model_validate(raw)

    # -- System ------------------------------------------------------------

    def system_memory(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/memory")

    def system_disk(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/system_disk")

    def system_information(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/system_information")

    def system_mbuf(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/system_mbuf")

    def system_resources(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/system_resources")

    def system_swap(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/system_swap")

    def system_temperature(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/system_temperature")

    def system_time(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/system_time")

    # -- System Health -----------------------------------------------------

    def export_health_csv(self, rrd: str = "", detail: int = -1) -> dict[str, Any]:
        return self._client._get(f"{_M}/systemhealth/export_as_c_s_v/{rrd}/{detail}")

    def get_health_interfaces(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/systemhealth/get_interfaces")

    def get_rrd_list(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/systemhealth/get_rrd_list")

    def get_system_health(self, rrd: str = "", detail: int = -1) -> dict[str, Any]:
        return self._client._get(f"{_M}/systemhealth/get_system_health/{rrd}/{detail}")

    # -- Traceroute --------------------------------------------------------

    def get_traceroute_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/traceroute/get")

    def set_traceroute_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/traceroute/set", json=data)
        return ApiResponse.model_validate(raw)

    # -- Traffic -----------------------------------------------------------

    def traffic_interface(self) -> dict[str, Any]:
        """Maps to GET diagnostics/traffic/_interface."""
        return self._client._get(f"{_M}/traffic/_interface")

    def traffic_top(self, interfaces: str) -> dict[str, Any]:
        """Maps to GET diagnostics/traffic/_top."""
        return self._client._get(f"{_M}/traffic/_top/{interfaces}")

    def traffic_stream(self, poll_interval: int = 1) -> dict[str, Any]:
        return self._client._get(f"{_M}/traffic/stream/{poll_interval}")
