# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import re
from typing import Any, List, Optional, Tuple

VERSION_METRIC_NAME = "server"

COUNT_METRICS = {
    "proxy.process.http.origin_server_total_request_bytes": "process.http.origin_server_total_request_bytes",
    "proxy.process.http.origin_server_total_response_bytes": "process.http.origin_server_total_response_bytes",
    "proxy.process.user_agent_total_bytes": "process.user_agent_total_bytes",
    "proxy.process.origin_server_total_bytes": "process.origin_server_total_bytes",
    "proxy.process.http.origin_server_total_request_bytes": "process.http.origin_server_total_request_bytes",
    "proxy.process.http.origin_server_total_response_bytes": "process.http.origin_server_total_response_bytes",
    "proxy.process.user_agent_total_bytes": "process.user_agent_total_bytes",
    "proxy.process.origin_server_total_bytes": "process.origin_server_total_bytes",
    "proxy.process.cache_total_hits": "process.cache.total_hits",
    "proxy.process.cache_total_misses": "process.cache.total_misses",
    "proxy.process.cache_total_requests": "process.cache.total_requests",
    "proxy.process.cache_total_hits_bytes": "process.cache.total_hits_bytes",
    "proxy.process.cache_total_misses_bytes": "process.cache.total_misses_bytes",
    "proxy.process.cache_total_bytes": "process.cache.total_bytes",
    "proxy.process.http.user_agent_total_request_bytes": "process.http.user_agent_total_request_bytes",
    "proxy.process.http.user_agent_total_response_bytes": "process.http.user_agent_total_response_bytes",
    "proxy.process.http.completed_requests": "process.http.completed_requests",
    "proxy.process.http.total_incoming_connections": "process.http.total_incoming_connections",
    "proxy.process.http.total_client_connections": "process.http.total_client_connections",
    "proxy.process.http.total_client_connections_ipv4": "process.http.total_client_connections_ipv4",
    "proxy.process.http.total_client_connections_ipv6": "process.http.total_client_connections_ipv6",
    "proxy.process.http.total_server_connections": "process.http.total_server_connections",
    "proxy.process.http.total_parent_proxy_connections": "process.http.total_parent_proxy_connections",
    "proxy.process.http.total_parent_retries": "process.http.total_parent_retries",
    "proxy.process.http.total_parent_switches": "process.http.total_parent_switches",
    "proxy.process.http.total_parent_retries_exhausted": "process.http.total_parent_retries_exhausted",
    "proxy.process.http.total_parent_marked_down_count": "process.http.total_parent_marked_down_count",
    "proxy.process.http.background_fill_total_count": "process.http.background_fill_total_count",
    "proxy.process.http.transaction_counts.errors.pre_accept_hangups": (
        "process.http.transaction_counts.errors.pre_accept_hangups"
    ),
    "proxy.process.http.incoming_requests": "process.http.incoming_requests",
    "proxy.process.http.outgoing_requests": "process.http.outgoing_requests",
    "proxy.process.http.incoming_responses": "process.http.incoming_responses",
    "proxy.process.http.invalid_client_requests": "process.http.invalid_client_requests",
    "proxy.process.http.missing_host_hdr": "process.http.missing_host_hdr",
    "proxy.process.http.get_requests": "process.http.get_requests",
    "proxy.process.http.head_requests": "process.http.head_requests",
    "proxy.process.http.trace_requests": "process.http.trace_requests",
    "proxy.process.http.options_requests": "process.http.options_requests",
    "proxy.process.http.post_requests": "process.http.post_requests",
    "proxy.process.http.put_requests": "process.http.put_requests",
    "proxy.process.http.push_requests": "process.http.push_requests",
    "proxy.process.http.delete_requests": "process.http.delete_requests",
    "proxy.process.http.purge_requests": "process.http.purge_requests",
    "proxy.process.http.connect_requests": "process.http.connect_requests",
    "proxy.process.http.extension_method_requests": "process.http.extension_method_requests",
    "proxy.process.http.broken_server_connections": "process.http.broken_server_connections",
    "proxy.process.http.cache_lookups": "process.http.cache_lookups",
    "proxy.process.http.cache_writes": "process.http.cache_writes",
    "proxy.process.http.cache_updates": "process.http.cache_updates",
    "proxy.process.http.cache_deletes": "process.http.cache_deletes",
    "proxy.process.http.tunnels": "process.http.tunnels",
    "proxy.process.http.parent_proxy_transaction_time": "process.http.parent_proxy_transaction_time",
    "proxy.process.http.user_agent_request_header_total_size": "process.http.user_agent_request_header_total_size",
    "proxy.process.http.user_agent_response_header_total_size": "process.http.user_agent_response_header_total_size",
    "proxy.process.http.user_agent_request_document_total_size": "process.http.user_agent_request_document_total_size",
    "proxy.process.http.user_agent_response_document_total_size": (
        "process.http.user_agent_response_document_total_size"
    ),
    "proxy.process.http.origin_server_request_header_total_size": (
        "process.http.origin_server_request_header_total_size"
    ),
    "proxy.process.http.origin_server_response_header_total_size": (
        "process.http.origin_server_response_header_total_size"
    ),
    "proxy.process.http.origin_server_request_document_total_size": (
        "process.http.origin_server_request_document_total_size"
    ),
    "proxy.process.http.origin_server_response_document_total_size": (
        "process.http.origin_server_response_document_total_size"
    ),
    "proxy.process.http.parent_proxy_request_total_bytes": "process.http.parent_proxy_request_total_bytes",
    "proxy.process.http.parent_proxy_response_total_bytes": "process.http.parent_proxy_response_total_bytes",
    "proxy.process.http.pushed_response_header_total_size": "process.http.pushed_response_header_total_size",
    "proxy.process.http.pushed_document_total_size": "process.http.pushed_document_total_size",
    "proxy.process.http.response_document_size_100": "process.http.response_document_size_100",
    "proxy.process.http.response_document_size_1K": "process.http.response_document_size_1K",
    "proxy.process.http.response_document_size_3K": "process.http.response_document_size_3K",
    "proxy.process.http.response_document_size_5K": "process.http.response_document_size_5K",
    "proxy.process.http.response_document_size_10K": "process.http.response_document_size_10K",
    "proxy.process.http.response_document_size_1M": "process.http.response_document_size_1M",
    "proxy.process.http.response_document_size_inf": "process.http.response_document_size_inf",
    "proxy.process.http.request_document_size_100": "process.http.request_document_size_100",
    "proxy.process.http.request_document_size_1K": "process.http.request_document_size_1K",
    "proxy.process.http.request_document_size_3K": "process.http.request_document_size_3K",
    "proxy.process.http.request_document_size_5K": "process.http.request_document_size_5K",
    "proxy.process.http.request_document_size_10K": "process.http.request_document_size_10K",
    "proxy.process.http.request_document_size_1M": "process.http.request_document_size_1M",
    "proxy.process.http.request_document_size_inf": "process.http.request_document_size_inf",
    "proxy.process.http.total_transactions_time": "process.http.total_transactions_time",
    "proxy.process.http.cache_hit_fresh": "process.http.cache.hit_fresh",
    "proxy.process.http.cache_hit_mem_fresh": "process.http.cache.hit_mem_fresh",
    "proxy.process.http.cache_hit_revalidated": "process.http.cache.hit_revalidated",
    "proxy.process.http.cache_hit_ims": "process.http.cache.hit_ims",
    "proxy.process.http.cache_hit_stale_served": "process.http.cache.hit_stale_served",
    "proxy.process.http.cache_miss_cold": "process.http.cache.miss_cold",
    "proxy.process.http.cache_miss_changed": "process.http.cache.miss_changed",
    "proxy.process.http.cache_miss_client_no_cache": "process.http.cache.miss_client_no_cache",
    "proxy.process.http.cache_miss_client_not_cacheable": "process.http.cache.miss_client_not_cacheable",
    "proxy.process.http.cache_miss_ims": "process.http.cache.miss_ims",
    "proxy.process.http.cache_read_error": "process.http.cache.read_error",
    "proxy.process.http.user_agent_speed_bytes_per_sec_100": "process.http.user_agent_speed_bytes_per_sec_100",
    "proxy.process.http.user_agent_speed_bytes_per_sec_1K": "process.http.user_agent_speed_bytes_per_sec_1K",
    "proxy.process.http.user_agent_speed_bytes_per_sec_10K": "process.http.user_agent_speed_bytes_per_sec_10K",
    "proxy.process.http.user_agent_speed_bytes_per_sec_100K": "process.http.user_agent_speed_bytes_per_sec_100K",
    "proxy.process.http.user_agent_speed_bytes_per_sec_1M": "process.http.user_agent_speed_bytes_per_sec_1M",
    "proxy.process.http.user_agent_speed_bytes_per_sec_10M": "process.http.user_agent_speed_bytes_per_sec_10M",
    "proxy.process.http.user_agent_speed_bytes_per_sec_100M": "process.http.user_agent_speed_bytes_per_sec_100M",
    "proxy.process.http.origin_server_speed_bytes_per_sec_100": "process.http.origin_server_speed_bytes_per_sec_100",
    "proxy.process.http.origin_server_speed_bytes_per_sec_1K": "process.http.origin_server_speed_bytes_per_sec_1K",
    "proxy.process.http.origin_server_speed_bytes_per_sec_10K": "process.http.origin_server_speed_bytes_per_sec_10K",
    "proxy.process.http.origin_server_speed_bytes_per_sec_100K": "process.http.origin_server_speed_bytes_per_sec_100K",
    "proxy.process.http.origin_server_speed_bytes_per_sec_1M": "process.http.origin_server_speed_bytes_per_sec_1M",
    "proxy.process.http.origin_server_speed_bytes_per_sec_10M": "process.http.origin_server_speed_bytes_per_sec_10M",
    "proxy.process.http.origin_server_speed_bytes_per_sec_100M": "process.http.origin_server_speed_bytes_per_sec_100M",
    "proxy.process.http.tcp_hit_count_stat": "process.http.tcp.hit_count",
    "proxy.process.http.tcp_miss_count_stat": "process.http.tcp.miss_count",
    "proxy.process.http.tcp_expired_miss_count_stat": "process.http.tcp.expired_miss_count",
    "proxy.process.http.tcp_refresh_hit_count_stat": "process.http.tcp.refresh_hit_count",
    "proxy.process.http.tcp_refresh_miss_count_stat": "process.http.tcp.refresh_miss_count",
    "proxy.process.http.tcp_client_refresh_count_stat": "process.http.tcp.client_refresh_count",
    "proxy.process.http.tcp_ims_hit_count_stat": "process.http.tcp.ims_hit_count",
    "proxy.process.http.tcp_ims_miss_count_stat": "process.http.tcp.ims_miss_count",
    "proxy.process.http.err_client_abort_count_stat": "process.http.error.client_abort_count",
    "proxy.process.http.err_client_read_error_count_stat": "process.http.error.client_read_error_count",
    "proxy.process.http.err_connect_fail_count_stat": "process.http.errpr.connect_fail_count",
    "proxy.process.http.misc_count_stat": "process.http.misc_count",
    "proxy.process.http.cache_write_errors": "process.http.cache_write_errors",
    "proxy.process.http.cache_read_errors": "process.http.cache_read_errors",
    "proxy.process.http.transaction_counts.hit_fresh": "process.http.transaction_counts.hit_fresh",
    "proxy.process.http.transaction_totaltime.hit_fresh": "process.http.transaction_totaltime.hit_fresh",
    "proxy.process.http.transaction_counts.hit_fresh.process": "process.http.transaction_counts.hit_fresh.process",
    "proxy.process.http.transaction_totaltime.hit_fresh.process": (
        "process.http.transaction_totaltime.hit_fresh.process"
    ),
    "proxy.process.http.transaction_counts.hit_revalidated": "process.http.transaction_counts.hit_revalidated",
    "proxy.process.http.transaction_totaltime.hit_revalidated": "process.http.transaction_totaltime.hit_revalidated",
    "proxy.process.http.transaction_counts.miss_cold": "process.http.transaction_counts.miss_cold",
    "proxy.process.http.transaction_totaltime.miss_cold": "process.http.transaction_totaltime.miss_cold",
    "proxy.process.http.transaction_counts.miss_not_cacheable": "process.http.transaction_counts.miss_not_cacheable",
    "proxy.process.http.transaction_totaltime.miss_not_cacheable": (
        "process.http.transaction_totaltime.miss_not_cacheable"
    ),
    "proxy.process.http.transaction_counts.miss_changed": "process.http.transaction_counts.miss_changed",
    "proxy.process.http.transaction_totaltime.miss_changed": "process.http.transaction_totaltime.miss_changed",
    "proxy.process.http.transaction_counts.miss_client_no_cache": (
        "process.http.transaction_counts.miss_client_no_cache"
    ),
    "proxy.process.http.transaction_totaltime.miss_client_no_cache": (
        "process.http.transaction_totaltime.miss_client_no_cache"
    ),
    "proxy.process.http.transaction_counts.errors.aborts": "process.http.transaction_counts.errors.aborts",
    "proxy.process.http.transaction_totaltime.errors.aborts": "process.http.transaction_totaltime.errors.aborts",
    "proxy.process.http.transaction_counts.errors.possible_aborts": (
        "process.http.transaction_counts.errors.possible_aborts"
    ),
    "proxy.process.http.transaction_totaltime.errors.possible_aborts": (
        "process.http.transaction_totaltime.errors.possible_aborts"
    ),
    "proxy.process.http.transaction_counts.errors.connect_failed": (
        "process.http.transaction_counts.errors.connect_failed"
    ),
    "proxy.process.http.transaction_totaltime.errors.connect_failed": (
        "process.http.transaction_totaltime.errors.connect_failed"
    ),
    "proxy.process.http.transaction_counts.errors.other": "process.http.transaction_counts.errors.other",
    "proxy.process.http.transaction_totaltime.errors.other": "process.http.transaction_totaltime.errors.other",
    "proxy.process.http.transaction_counts.other.unclassified": "process.http.transaction_counts.other.unclassified",
    "proxy.process.http.transaction_totaltime.other.unclassified": (
        "process.http.transaction_totaltime.other.unclassified"
    ),
    "proxy.process.http.disallowed_post_100_continue": "process.http.disallowed_post_100_continue",
    "proxy.process.http.total_x_redirect_count": "process.http.total_x_redirect_count",
    "proxy.process.https.incoming_requests": "process.https.incoming_requests",
    "proxy.process.https.total_client_connections": "process.https.total_client_connections",
    "proxy.process.http.origin_connections_throttled_out": "process.http.origin_connections_throttled_out",
    "proxy.process.http.post_body_too_large": "process.http.post_body_too_large",
    # TODO http milestone counts
    "proxy.process.http.milestone.ua_begin": "process.http.milestone.ua_begin",
    "proxy.process.http.milestone.ua_first_read": "process.http.milestone.ua_first_read",
    "proxy.process.http.milestone.ua_read_header_done": "process.http.milestone.ua_read_header_done",
    "proxy.process.http.milestone.ua_begin_write": "process.http.milestone.ua_begin_write",
    "proxy.process.http.milestone.ua_close": "process.http.milestone.ua_close",
    "proxy.process.http.milestone.server_first_connect": "process.http.milestone.server_first_connect",
    "proxy.process.http.milestone.server_connect": "process.http.milestone.server_connect",
    "proxy.process.http.milestone.server_connect_end": "process.http.milestone.server_connect_end",
    "proxy.process.http.milestone.server_begin_write": "process.http.milestone.server_begin_write",
    "proxy.process.http.milestone.server_first_read": "process.http.milestone.server_first_read",
    "proxy.process.http.milestone.server_read_header_done": "process.http.milestone.server_read_header_done",
    "proxy.process.http.milestone.server_close": "process.http.milestone.server_close",
    "proxy.process.http.milestone.cache_open_read_begin": "process.http.milestone.cache_open_read_begin",
    "proxy.process.http.milestone.cache_open_read_end": "process.http.milestone.cache_open_read_end",
    "proxy.process.http.milestone.cache_open_write_begin": "process.http.milestone.cache_open_write_begin",
    "proxy.process.http.milestone.cache_open_write_end": "process.http.milestone.cache_open_write_end",
    "proxy.process.http.milestone.dns_lookup_begin": "process.http.milestone.dns_lookup_begin",
    "proxy.process.http.milestone.dns_lookup_end": "process.http.milestone.dns_lookup_end",
    "proxy.process.http.milestone.sm_start": "process.http.milestone.sm_start",
    "proxy.process.http.milestone.sm_finish": "process.http.milestone.sm_finish",
    "proxy.process.http.dead_server.no_requests": "process.http.dead_server.no_requests",
    "proxy.process.net.calls_to_read": "process.net.calls_to_read",
    "proxy.process.net.calls_to_read_nodata": "process.net.calls_to_read_nodata",
    "proxy.process.net.calls_to_readfromnet": "process.net.calls_to_readfromnet",
    "proxy.process.net.calls_to_readfromnet_afterpoll": "process.net.calls_to_readfromnet_afterpoll",
    "proxy.process.net.calls_to_write": "process.net.calls_to_write",
    "proxy.process.net.calls_to_write_nodata": "process.net.calls_to_write_nodata",
    "proxy.process.net.calls_to_writetonet": "process.net.calls_to_writetonet",
    "proxy.process.net.calls_to_writetonet_afterpoll": "process.net.calls_to_writetonet_afterpoll",
    "proxy.process.net.net_handler_run": "process.net.net_handler_run",
    "proxy.process.net.read_bytes": "process.net.read_bytes",
    "proxy.process.net.write_bytes": "process.net.write_bytes",
    "proxy.process.net.inactivity_cop_lock_acquire_failure": "process.net.inactivity_cop_lock_acquire_failure",  # TODO
    "proxy.process.net.fastopen_out.attempts": "process.net.fastopen_out.attempts",
    "proxy.process.net.fastopen_out.successes": "process.net.fastopen_out.successes",
    "proxy.process.socks.connections_successful": "process.socks.connections_successful",
    "proxy.process.socks.connections_unsuccessful": "process.socks.connections_unsuccessful",
    "proxy.process.net.connections_throttled_in": "process.net.connections_throttled_in",
    "proxy.process.net.connections_throttled_out": "process.net.connections_throttled_out",
    "proxy.process.net.max.requests_throttled_in": "process.net.max.requests_throttled_in",
    "proxy.process.hostdb.total_lookups": "process.hostdb.total_lookups",
    "proxy.process.hostdb.total_hits": "process.hostdb.total_hits",
    "proxy.process.hostdb.re_dns_on_reload": "process.hostdb.re_dns_on_reload",
    "proxy.process.dns.total_dns_lookups": "process.dns.total_dns_lookups",
    "proxy.process.dns.lookup_successes": "process.dns.lookup_successes",
    "proxy.process.dns.lookup_failures": "process.dns.lookup_failures",
    "proxy.process.dns.retries": "process.dns.retries",
    "proxy.process.dns.max_retries_exceeded": "process.dns.max_retries_exceeded",
    "proxy.process.http2.total_client_streams": "process.http2.total_client_streams",
    "proxy.process.http2.total_transactions_time": "process.http2.total_transactions_time",
    "proxy.process.http2.total_client_connections": "process.http2.total_client_connections",
    "proxy.process.http2.connection_errors": "process.http2.connection_errors",
    "proxy.process.http2.stream_errors": "process.http2.stream_errors",
    "proxy.process.http2.session_die_default": "process.http2.session_die_default",
    "proxy.process.http2.session_die_other": "process.http2.session_die_other",
    "proxy.process.http2.session_die_eos": "process.http2.session_die_eos",
    "proxy.process.http2.session_die_active": "process.http2.session_die_active",
    "proxy.process.http2.session_die_inactive": "process.http2.session_die_inactive",
    "proxy.process.http2.session_die_error": "process.http2.session_die_error",
    "proxy.process.http2.session_die_high_error_rate": "process.http2.session_die_high_error_rate",
    "proxy.process.http2.max_settings_per_frame_exceeded": "process.http2.max_settings_per_frame_exceeded",
    "proxy.process.http2.max_settings_per_minute_exceeded": "process.http2.max_settings_per_minute_exceeded",
    "proxy.process.http2.max_settings_frames_per_minute_exceeded": (
        "process.http2.max_settings_frames_per_minute_exceeded"
    ),
    "proxy.process.http2.max_ping_frames_per_minute_exceeded": "process.http2.max_ping_frames_per_minute_exceeded",
    "proxy.process.http2.max_priority_frames_per_minute_exceeded": (
        "process.http2.max_priority_frames_per_minute_exceeded"
    ),
    "proxy.process.http2.insufficient_avg_window_update": "process.http2.insufficient_avg_window_update",
    "proxy.process.log.event_log_error_ok": "process.log.event_log_error_ok",
    "proxy.process.log.event_log_error_skip": "process.log.event_log_error_skip",
    "proxy.process.log.event_log_error_aggr": "process.log.event_log_error_aggr",
    "proxy.process.log.event_log_error_full": "process.log.event_log_error_full",
    "proxy.process.log.event_log_error_fail": "process.log.event_log_error_fail",
    "proxy.process.log.event_log_access_ok": "process.log.event_log_access_ok",
    "proxy.process.log.event_log_access_skip": "process.log.event_log_access_skip",
    "proxy.process.log.event_log_access_aggr": "process.log.event_log_access_aggr",
    "proxy.process.log.event_log_access_full": "process.log.event_log_access_full",
    "proxy.process.log.event_log_access_fail": "process.log.event_log_access_fail",
    "proxy.process.log.num_sent_to_network": "process.log.num_sent_to_network",
    "proxy.process.log.num_lost_before_sent_to_network": "process.log.num_lost_before_sent_to_network",
    "proxy.process.log.num_received_from_network": "process.log.num_received_from_network",
    "proxy.process.log.num_flush_to_disk": "process.log.num_flush_to_disk",
    "proxy.process.log.num_lost_before_flush_to_disk": "process.log.num_lost_before_flush_to_disk",
    "proxy.process.log.bytes_lost_before_preproc": "process.log.bytes_lost_before_preproc",
    "proxy.process.log.bytes_sent_to_network": "process.log.bytes_sent_to_network",
    "proxy.process.log.bytes_lost_before_sent_to_network": "process.log.bytes_lost_before_sent_to_network",
    "proxy.process.log.bytes_received_from_network": "process.log.bytes_received_from_network",
    "proxy.process.log.bytes_flush_to_disk": "process.log.bytes_flush_to_disk",
    "proxy.process.log.bytes_lost_before_flush_to_disk": "process.log.bytes_lost_before_flush_to_disk",
    "proxy.process.log.bytes_written_to_disk": "process.log.bytes_written_to_disk",
    "proxy.process.log.bytes_lost_before_written_to_disk": "process.log.bytes_lost_before_written_to_disk",
    "proxy.process.ssl.user_agent_other_errors": "process.ssl.user_agent_other_errors",
    "proxy.process.ssl.user_agent_expired_cert": "process.ssl.user_agent_expired_cert",
    "proxy.process.ssl.user_agent_revoked_cert": "process.ssl.user_agent_revoked_cert",
    "proxy.process.ssl.user_agent_unknown_cert": "process.ssl.user_agent_unknown_cert",
    "proxy.process.ssl.user_agent_cert_verify_failed": "process.ssl.user_agent_cert_verify_failed",
    "proxy.process.ssl.user_agent_bad_cert": "process.ssl.user_agent_bad_cert",
    "proxy.process.ssl.user_agent_decryption_failed": "process.ssl.user_agent_decryption_failed",
    "proxy.process.ssl.user_agent_wrong_version": "process.ssl.user_agent_wrong_version",
    "proxy.process.ssl.user_agent_unknown_ca": "process.ssl.user_agent_unknown_ca",
    "proxy.process.ssl.origin_server_other_errors": "process.ssl.origin_server_other_errors",
    "proxy.process.ssl.origin_server_expired_cert": "process.ssl.origin_server_expired_cert",
    "proxy.process.ssl.origin_server_revoked_cert": "process.ssl.origin_server_revoked_cert",
    "proxy.process.ssl.origin_server_unknown_cert": "process.ssl.origin_server_unknown_cert",
    "proxy.process.ssl.origin_server_cert_verify_failed": "process.ssl.origin_server_cert_verify_failed",
    "proxy.process.ssl.origin_server_bad_cert": "process.ssl.origin_server_bad_cert",
    "proxy.process.ssl.origin_server_decryption_failed": "process.ssl.origin_server_decryption_failed",
    "proxy.process.ssl.origin_server_wrong_version": "process.ssl.origin_server_wrong_version",
    "proxy.process.ssl.origin_server_unknown_ca": "process.ssl.origin_server_unknown_ca",
    "proxy.process.ssl.total_handshake_time": "process.ssl.total_handshake_time",
    "proxy.process.ssl.total_attempts_handshake_count_in": "process.ssl.total_attempts_handshake_count_in",
    "proxy.process.ssl.total_success_handshake_count_in": "process.ssl.total_success_handshake_count_in",
    "proxy.process.ssl.total_attempts_handshake_count_out": "process.ssl.total_attempts_handshake_count_out",
    "proxy.process.ssl.total_success_handshake_count_out": "process.ssl.total_success_handshake_count_out",
    "proxy.process.ssl.total_tickets_created": "process.ssl.total_tickets_created",
    "proxy.process.ssl.total_tickets_verified": "process.ssl.total_tickets_verified",
    "proxy.process.ssl.total_tickets_not_found": "process.ssl.total_tickets_not_found",
    "proxy.process.ssl.total_tickets_renewed": "process.ssl.total_tickets_renewed",
    "proxy.process.ssl.total_tickets_verified_old_key": "process.ssl.total_tickets_verified_old_key",
    "proxy.process.ssl.total_ticket_keys_renewed": "process.ssl.total_ticket_keys_renewed",
    "proxy.process.ssl.ssl_session_cache_hit": "process.ssl.ssl_session_cache_hit",
    "proxy.process.ssl.ssl_session_cache_new_session": "process.ssl.ssl_session_cache_new_session",
    "proxy.process.ssl.ssl_session_cache_miss": "process.ssl.ssl_session_cache_miss",
    "proxy.process.ssl.ssl_session_cache_eviction": "process.ssl.ssl_session_cache_eviction",
    "proxy.process.ssl.ssl_session_cache_lock_contention": "process.ssl.ssl_session_cache_lock_contention",
    "proxy.process.ssl.default_record_size_count": "process.ssl.default_record_size_count",
    "proxy.process.ssl.max_record_size_count": "process.ssl.max_record_size_count",
    "proxy.process.ssl.redo_record_size_count": "process.ssl.redo_record_size_count",
    "proxy.process.ssl.ssl_error_syscall": "process.ssl.ssl_error_syscall",
    "proxy.process.ssl.ssl_error_ssl": "process.ssl.ssl_error_ssl",
    "proxy.process.ssl.ssl_error_async": "process.ssl.ssl_error_async",
    "proxy.process.ssl.ssl_sni_name_set_failure": "process.ssl.ssl_sni_name_set_failure",
    "proxy.process.ssl.ssl_ocsp_revoked_cert_stat": "process.ssl.ssl_ocsp_revoked_cert_stat",
    "proxy.process.ssl.ssl_ocsp_unknown_cert_stat": "process.ssl.ssl_ocsp_unknown_cert_stat",
    "proxy.process.ssl.ssl_total_sslv3": "process.ssl.ssl_total_sslv3",
    "proxy.process.ssl.ssl_total_tlsv1": "process.ssl.ssl_total_tlsv1",
    "proxy.process.ssl.ssl_total_tlsv11": "process.ssl.ssl_total_tlsv11",
    "proxy.process.ssl.ssl_total_tlsv12": "process.ssl.ssl_total_tlsv12",
    "proxy.process.ssl.ssl_total_tlsv13": "process.ssl.ssl_total_tlsv13",
    "proxy.process.http.origin_shutdown.pool_lock_contention": "process.http.origin_shutdown.pool_lock_contention",
    "proxy.process.http.origin_shutdown.migration_failure": "process.http.origin_shutdown.migration_failure",
    "proxy.process.http.origin_shutdown.tunnel_server": "process.http.origin_shutdown.tunnel_server",
    "proxy.process.http.origin_shutdown.tunnel_server_no_keep_alive": (
        "process.http.origin_shutdown.tunnel_server_no_keep_alive"
    ),
    "proxy.process.http.origin_shutdown.tunnel_server_eos": "process.http.origin_shutdown.tunnel_server_eos",
    "proxy.process.http.origin_shutdown.tunnel_server_plugin_tunnel": (
        "process.http.origin_shutdown.tunnel_server_plugin_tunnel"
    ),
    "proxy.process.http.origin_shutdown.tunnel_server_detach": "process.http.origin_shutdown.tunnel_server_detach",
    "proxy.process.http.origin_shutdown.tunnel_client": "process.http.origin_shutdown.tunnel_client",
    "proxy.process.http.origin_shutdown.tunnel_transform_read": "process.http.origin_shutdown.tunnel_transform_read",
    "proxy.process.http.origin_shutdown.release_no_sharing": "process.http.origin_shutdown.release_no_sharing",
    "proxy.process.http.origin_shutdown.release_no_server": "process.http.origin_shutdown.release_no_server",
    "proxy.process.http.origin_shutdown.release_no_keep_alive": "process.http.origin_shutdown.release_no_keep_alive",
    "proxy.process.http.origin_shutdown.release_invalid_response": (
        "process.http.origin_shutdown.release_invalid_response"
    ),
    "proxy.process.http.origin_shutdown.release_invalid_request": (
        "process.http.origin_shutdown.release_invalid_request"
    ),
    "proxy.process.http.origin_shutdown.release_modified": "process.http.origin_shutdown.release_modified",
    "proxy.process.http.origin_shutdown.release_misc": "process.http.origin_shutdown.release_misc",
    "proxy.process.http.origin_shutdown.cleanup_entry": "process.http.origin_shutdown.cleanup_entry",
    "proxy.process.http.origin_shutdown.tunnel_abort": "process.http.origin_shutdown.tunnel_abort",
    "proxy.process.http.origin.connect.adjust_thread": "process.http.origin.connect.adjust_thread",
    "proxy.process.http.cache.open_write.adjust_thread": "process.http.cache.open_write.adjust_thread",
    "proxy.process.net.default_inactivity_timeout_applied": "process.net.default_inactivity_timeout_applied",
    "proxy.process.net.default_inactivity_timeout_count": "process.net.default_inactivity_timeout_count",
    "proxy.process.net.dynamic_keep_alive_timeout_in_count": "process.net.dynamic_keep_alive_timeout_in_count",
    "proxy.process.net.dynamic_keep_alive_timeout_in_total": "process.net.dynamic_keep_alive_timeout_in_total",
    "proxy.process.tcp.total_accepts": "process.tcp.total_accepts",
    "proxy.process.cache.bytes_used": "process.cache.bytes_used",
    "proxy.process.cache.bytes_total": "process.cache.bytes_total",
    "proxy.process.cache.ram_cache.total_bytes": "process.cache.ram_cache.total_bytes",  # TODO
    "proxy.process.cache.ram_cache.bytes_used": "process.cache.ram_cache.bytes_used",
    "proxy.process.cache.ram_cache.hits": "process.cache.ram_cache.hits",
    "proxy.process.cache.ram_cache.misses": "process.cache.ram_cache.misses",
    "proxy.process.cache.pread_count": "process.cache.pread_count",
    # TODO cache active
    "proxy.process.cache.lookup.active": "process.cache.lookup.active",
    "proxy.process.cache.lookup.success": "process.cache.lookup.success",
    "proxy.process.cache.lookup.failure": "process.cache.lookup.failure",
    "proxy.process.cache.read.active": "process.cache.read.active",
    "proxy.process.cache.read.success": "process.cache.read.success",
    "proxy.process.cache.read.failure": "process.cache.read.failure",
    "proxy.process.cache.write.active": "process.cache.write.active",
    "proxy.process.cache.write.success": "process.cache.write.success",
    "proxy.process.cache.write.failure": "process.cache.write.failure",
    "proxy.process.cache.write.backlog.failure": "process.cache.write.backlog.failure",
    "proxy.process.cache.update.active": "process.cache.update.active",
    "proxy.process.cache.update.success": "process.cache.update.success",
    "proxy.process.cache.update.failure": "process.cache.update.failure",
    "proxy.process.cache.remove.active": "process.cache.remove.active",
    "proxy.process.cache.remove.success": "process.cache.remove.success",
    "proxy.process.cache.remove.failure": "process.cache.remove.failure",
    "proxy.process.cache.evacuate.active": "process.cache.evacuate.active",
    "proxy.process.cache.evacuate.success": "process.cache.evacuate.success",
    "proxy.process.cache.evacuate.failure": "process.cache.evacuate.failure",
    "proxy.process.cache.scan.active": "process.cache.scan.active",
    "proxy.process.cache.scan.success": "process.cache.scan.success",
    "proxy.process.cache.scan.failure": "process.cache.scan.failure",
    "proxy.process.hostdb.cache.total_inserts": "process.hostdb.cache.total_inserts",
    "proxy.process.hostdb.cache.total_failed_inserts": "process.hostdb.cache.total_failed_inserts",
    "proxy.process.hostdb.cache.total_lookups": "process.hostdb.cache.total_lookups",
    "proxy.process.hostdb.cache.total_hits": "process.hostdb.cache.total_hits",
    "proxy.process.ssl.user_agent_sessions": "process.ssl.user_agent_sessions",
    "proxy.process.ssl.user_agent_session_hit": "process.ssl.user_agent_session_hit",
    "proxy.process.ssl.user_agent_session_miss": "process.ssl.user_agent_session_miss",
    "proxy.process.ssl.user_agent_session_timeout": "process.ssl.user_agent_session_timeout",
}

GAUGE_METRICS = {
    "proxy.node.restarts.proxy.restart_count": "node.restarts.proxy.restart_count",
    "proxy.node.restarts.manager.start_time": "node.restarts.manager.start_time",
    "proxy.node.restarts.proxy.start_time": "node.restarts.proxy.start_time",
    "proxy.node.restarts.proxy.cache_ready_time": "node.restarts.proxy.cache_ready_time",
    "proxy.node.restarts.proxy.stop_time": "node.restarts.proxy.stop_time",
    "proxy.process.current_server_connections": "process.current_server_connections",
    "proxy.node.proxy_running": "node.proxy_running",
    "proxy.process.http.avg_transactions_per_client_connection": "process.http.avg_transactions_per_client_connection",
    "proxy.process.http.avg_transactions_per_server_connection": "process.http.avg_transactions_per_server_connection",
    # Tcp: look into counts
    "proxy.process.http.tcp_hit_user_agent_bytes_stat": "process.http.tcp.hit_user_agent_bytes",
    "proxy.process.http.tcp_hit_origin_server_bytes_stat": "process.http.tcp.hit_origin_server_bytes",
    "proxy.process.http.tcp_miss_user_agent_bytes_stat": "process.http.tcp.miss_user_agent_bytes",
    "proxy.process.http.tcp_miss_origin_server_bytes_stat": "process.http.tcp.miss_origin_server_bytes",
    "proxy.process.http.tcp_expired_miss_user_agent_bytes_stat": "process.http.tcp.expired_miss_user_agent_bytes",
    "proxy.process.http.tcp_expired_miss_origin_server_bytes_stat": "process.http.tcp.expired_miss_origin_server_bytes",
    "proxy.process.http.tcp_refresh_hit_user_agent_bytes_stat": "process.http.tcp.refresh_hit_user_agent_bytes",
    "proxy.process.http.tcp_refresh_hit_origin_server_bytes_stat": "process.http.tcp.refresh_hit_origin_server_bytes",
    "proxy.process.http.tcp_refresh_miss_user_agent_bytes_stat": "process.http.tcp.refresh_miss_user_agent_bytes",
    "proxy.process.http.tcp_refresh_miss_origin_server_bytes_stat": "process.http.tcp.refresh_miss_origin_server_bytes",
    "proxy.process.http.tcp_client_refresh_user_agent_bytes_stat": "process.http.tcp.client_refresh_user_agent_bytes",
    "proxy.process.http.tcp_client_refresh_origin_server_bytes_stat": (
        "process.http.tcp.client_refresh_origin_server_bytes"
    ),
    "proxy.process.http.tcp_ims_hit_user_agent_bytes_stat": "process.http.tcp.ims_hit_user_agent_bytes",
    "proxy.process.http.tcp_ims_hit_origin_server_bytes_stat": "process.http.tcp.ims_hit_origin_server_bytes",
    "proxy.process.http.tcp_ims_miss_user_agent_bytes_stat": "process.http.tcp.ims_miss_user_agent_bytes",
    "proxy.process.http.tcp_ims_miss_origin_server_bytes_stat": "process.http.tcp.ims_miss_origin_server_bytes",
    "proxy.process.http.err_client_abort_user_agent_bytes_stat": "process.http.error.client_abort_user_agent_bytes",
    "proxy.process.http.err_client_abort_origin_server_bytes_stat": (
        "process.http.error.client_abort_origin_server_bytes"
    ),
    "proxy.process.http.err_client_read_error_user_agent_bytes_stat": (
        "process.http.error.client_read_error_user_agent_bytes"
    ),
    "proxy.process.http.err_client_read_error_origin_server_bytes_stat": (
        "process.http.error.client_read_error_origin_server_bytes"
    ),
    "proxy.process.http.err_connect_fail_user_agent_bytes_stat": "process.http.error.connect_fail_user_agent_bytes",
    "proxy.process.http.err_connect_fail_origin_server_bytes_stat": (
        "process.http.error.connect_fail_origin_server_bytes"
    ),
    "proxy.process.http.misc_user_agent_bytes_stat": "process.http.misc_user_agent_bytes",
    "proxy.process.http.http_misc_origin_server_bytes_stat": "process.http.http_misc_origin_server_bytes",
    "proxy.process.http.background_fill_bytes_aborted_stat": "process.http.background_fill_bytes_aborted",
    "proxy.process.http.background_fill_bytes_completed_stat": "process.http.background_fill_bytes_completed",
    "proxy.process.cache.read_per_sec": "process.cache.read_per_sec",
    "proxy.process.cache.write_per_sec": "process.cache.write_per_sec",
    "proxy.process.cache.KB_read_per_sec": "process.cache.KB_read_per_sec",
    "proxy.process.cache.KB_write_per_sec": "process.cache.KB_write_per_sec",
    "proxy.process.hostdb.ttl": "process.hostdb.ttl",
    "proxy.process.hostdb.ttl_expires": "process.hostdb.ttl_expires",
    "proxy.process.hostdb.insert_duplicate_to_pending_dns": "process.hostdb.insert_duplicate_to_pending_dns",  # TODO
    "proxy.process.dns.lookup_avg_time": "process.dns.lookup_avg_time",
    "proxy.process.dns.fail_avg_time": "process.dns.fail_avg_time",
    "proxy.process.dns.tcp_retries": "process.dns.tcp_retries",
    "proxy.process.dns.tcp_reset": "process.dns.tcp_reset",
    "proxy.process.ssl.ssl_ocsp_refreshed_cert": "process.ssl.ocsp_refreshed_cert",
    "proxy.process.ssl.ssl_ocsp_refresh_cert_failure": "process.ssl.ocsp_refresh_cert_failure",
    "proxy.process.ssl.early_data_received": "process.ssl.early_data_received",
    "proxy.node.config.reconfigure_time": "node.config.reconfigure_time",
    "proxy.node.config.reconfigure_required": "node.config.reconfigure_required",
    "proxy.node.config.restart_required.proxy": "node.config.restart_required.proxy",
    "proxy.node.config.restart_required.manager": "node.config.restart_required.manager",
    "proxy.node.config.draining": "node.config.draining",
    "proxy.process.http.background_fill_current_count": "process.http.background_fill_current_count",
    "proxy.process.http.current_client_connections": "process.http.current_client_connections",
    "proxy.process.http.current_active_client_connections": "process.http.current_active_client_connections",
    "proxy.process.http.websocket.current_active_client_connections": (
        "process.http.websocket.current_active_client_connections"
    ),
    "proxy.process.http.current_client_transactions": "process.http.current_client_transactions",
    "proxy.process.http.current_server_transactions": "process.http.current_server_transactions",
    "proxy.process.http.current_parent_proxy_connections": "process.http.current_parent_proxy_connections",  # TODO
    "proxy.process.http.current_server_connections": "process.http.current_server_connections",
    "proxy.process.http.current_cache_connections": "process.http.current_cache_connections",
    "proxy.process.http.pooled_server_connections": "proxy.process.http.pooled_server_connections",
    "proxy.process.net.accepts_currently_open": "process.net.accepts_currently_open",  # TODO
    "proxy.process.net.connections_currently_open": "process.net.connections_currently_open",
    "proxy.process.socks.connections_currently_open": "process.socks.connections_currently_open",
    "proxy.process.cache.percent_full": "process.cache.percent_full",
    # TODO cache
    "proxy.process.cache.direntries.total": "process.cache.direntries.total",
    "proxy.process.cache.direntries.used": "process.cache.direntries.used",
    "proxy.process.cache.directory_collision": "process.cache.directory_collision",
    "proxy.process.cache.frags_per_doc.1": "process.cache.frags_per_doc.1",
    "proxy.process.cache.frags_per_doc.2": "process.cache.frags_per_doc.2",
    "proxy.process.cache.frags_per_doc.3+": "process.cache.frags_per_doc.3+",
    "proxy.process.cache.read_busy.success": "process.cache.read_busy.success",
    "proxy.process.cache.read_busy.failure": "process.cache.read_busy.failure",
    "proxy.process.cache.write_bytes_stat": "process.cache.write_bytes_stat",
    "proxy.process.cache.vector_marshals": "process.cache.vector_marshals",
    "proxy.process.cache.hdr_marshals": "process.cache.hdr_marshals",
    "proxy.process.cache.hdr_marshal_bytes": "process.cache.hdr_marshal_bytes",
    "proxy.process.cache.gc_bytes_evacuated": "process.cache.gc_bytes_evacuated",
    "proxy.process.cache.gc_frags_evacuated": "process.cache.gc_frags_evacuated",
    "proxy.process.cache.wrap_count": "process.cache.wrap_count",
    "proxy.process.cache.sync.count": "process.cache.sync.count",
    "proxy.process.cache.sync.bytes": "process.cache.sync.bytes",
    "proxy.process.cache.sync.time": "process.cache.sync.time",
    "proxy.process.cache.span.errors.read": "process.cache.span.errors.read",
    "proxy.process.cache.span.errors.write": "process.cache.span.errors.write",
    "proxy.process.cache.span.failing": "process.cache.span.failing",
    "proxy.process.cache.span.offline": "process.cache.span.offline",
    "proxy.process.cache.span.online": "process.cache.span.online",
    "proxy.process.dns.success_avg_time": "process.dns.success_avg_time",
    "proxy.process.dns.in_flight": "process.dns.in_flight",
    "proxy.process.eventloop.count.10s": "process.eventloop.count.10s",
    "proxy.process.eventloop.events.10s": "process.eventloop.events.10s",
    "proxy.process.eventloop.events.min.10s": "process.eventloop.events.min.10s",
    "proxy.process.eventloop.events.max.10s": "process.eventloop.events.max.10s",
    "proxy.process.eventloop.wait.10s": "process.eventloop.wait.10s",
    "proxy.process.eventloop.time.min.10s": "process.eventloop.time.min.10s",
    "proxy.process.eventloop.time.max.10s": "process.eventloop.time.max.10s",
    "proxy.process.eventloop.count.100s": "process.eventloop.count.100s",
    "proxy.process.eventloop.events.100s": "process.eventloop.events.100s",
    "proxy.process.eventloop.events.min.100s": "process.eventloop.events.min.100s",
    "proxy.process.eventloop.events.max.100s": "process.eventloop.events.max.100s",
    "proxy.process.eventloop.wait.100s": "process.eventloop.wait.100s",
    "proxy.process.eventloop.time.min.100s": "process.eventloop.time.min.100s",
    "proxy.process.eventloop.time.max.100s": "process.eventloop.time.max.100s",
    "proxy.process.eventloop.count.1000s": "process.eventloop.count.1000s",
    "proxy.process.eventloop.events.1000s": "process.eventloop.events.1000s",
    "proxy.process.eventloop.events.min.1000s": "process.eventloop.events.min.1000s",
    "proxy.process.eventloop.events.max.1000s": "process.eventloop.events.max.1000s",
    "proxy.process.eventloop.wait.1000s": "process.eventloop.wait.1000s",
    "proxy.process.eventloop.time.min.1000s": "process.eventloop.time.min.1000s",
    "proxy.process.eventloop.time.max.1000s": "process.eventloop.time.max.1000s",
    "proxy.process.traffic_server.memory.rss": "process.traffic_server.memory.rss",
    "proxy.process.http2.current_client_connections": "process.http2.current_client_connections",
    "proxy.process.http2.current_active_client_connections": "process.http2.current_active_client_connections",
    "proxy.process.http2.current_client_streams": "process.http2.current_client_streams",
    "proxy.process.hostdb.cache.current_items": "process.hostdb.cache.current_items",
    "proxy.process.hostdb.cache.current_size": "process.hostdb.cache.current_size",
    "proxy.process.hostdb.cache.last_sync.time": "process.hostdb.cache.last_sync.time",
    "proxy.process.hostdb.cache.last_sync.total_items": "process.hostdb.cache.last_sync.total_items",
    "proxy.process.hostdb.cache.last_sync.total_size": "process.hostdb.cache.last_sync.total_size",
    "proxy.process.log.log_files_open": "process.log.log_files_open",
    "proxy.process.log.log_files_space_used": "process.log.log_files_space_used",
}

REGEX_METRICS = [
    {
        'regex': r'proxy.process.ssl.cipher.user_agent.(.*)',
        'name': 'process.ssl.cipher.user_agent',
        'tags': ('cipher',),
    },
    {'regex': r'proxy.process.http.(1[0-9]{2})_responses', 'name': 'process.http.1xx_responses', 'tags': ('code',)},
    {'regex': r'proxy.process.http.(2[0-9]{2})_responses', 'name': 'process.http.2xx_responses', 'tags': ('code',)},
    {'regex': r'proxy.process.http.(3[0-9]{2})_responses', 'name': 'process.http.3xx_responses', 'tags': ('code',)},
    {'regex': r'proxy.process.http.(4[0-9]{2})_responses', 'name': 'process.http.4xx_responses', 'tags': ('code',)},
    {'regex': r'proxy.process.http.(5[0-9]{2})_responses', 'name': 'process.http.5xx_responses', 'tags': ('code',)},
    {
        'regex': r'proxy.process.cache.(.*?)\.bytes_used',
        'name': 'proxy.process.cache.bytes_used',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.bytes_total',
        'name': 'proxy.process.cache.bytes_total',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.ram_cache.total_bytes',
        'name': 'proxy.process.cache.ram_cache.total_bytes',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.ram_cache.bytes_used',
        'name': 'proxy.process.cache.ram_cache.bytes_used',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.ram_cache.hits',
        'name': 'proxy.process.cache.ram_cache.hits',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.ram_cache.misses',
        'name': 'proxy.process.cache.ram_cache.misses',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.pread_count',
        'name': 'proxy.process.cache.pread_count',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.percent_full',
        'name': 'proxy.process.cache.percent_full',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.lookup.active',
        'name': 'proxy.process.cache.lookup.active',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.lookup.success',
        'name': 'proxy.process.cache.lookup.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.lookup.failure',
        'name': 'proxy.process.cache.lookup.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.read.active',
        'name': 'proxy.process.cache.read.active',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.read.success',
        'name': 'proxy.process.cache.read.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.read.failure',
        'name': 'proxy.process.cache.read.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.write.active',
        'name': 'proxy.process.cache.write.active',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.write.success',
        'name': 'proxy.process.cache.write.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.write.failure',
        'name': 'proxy.process.cache.write.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.write.backlog.failure',
        'name': 'proxy.process.cache.write.backlog.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.update.active',
        'name': 'proxy.process.cache.update.active',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.update.success',
        'name': 'proxy.process.cache.update.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.update.failure',
        'name': 'proxy.process.cache.update.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.remove.active',
        'name': 'proxy.process.cache.remove.active',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.remove.success',
        'name': 'proxy.process.cache.remove.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.remove.failure',
        'name': 'proxy.process.cache.remove.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.evacuate.active',
        'name': 'proxy.process.cache.evacuate.active',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.evacuate.success',
        'name': 'proxy.process.cache.evacuate.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.evacuate.failure',
        'name': 'proxy.process.cache.evacuate.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.scan.active',
        'name': 'proxy.process.cache.scan.active',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.scan.success',
        'name': 'proxy.process.cache.scan.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.scan.failure',
        'name': 'proxy.process.cache.scan.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.direntries.total',
        'name': 'proxy.process.cache.direntries.total',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.direntries.used',
        'name': 'proxy.process.cache.direntries.used',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.directory_collision',
        'name': 'proxy.process.cache.directory_collision',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.frags_per_doc.1',
        'name': 'proxy.process.cache.frags_per_doc.1',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.frags_per_doc.2',
        'name': 'proxy.process.cache.frags_per_doc.2',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.frags_per_doc.3+',
        'name': 'proxy.process.cache.frags_per_doc.3+',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.read_busy.success',
        'name': 'proxy.process.cache.read_busy.success',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.read_busy.failure',
        'name': 'proxy.process.cache.read_busy.failure',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.write_bytes_stat',
        'name': 'proxy.process.cache.write_bytes_stat',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.vector_marshals',
        'name': 'proxy.process.cache.vector_marshals',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.hdr_marshals',
        'name': 'proxy.process.cache.hdr_marshals',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.hdr_marshal_bytes',
        'name': 'proxy.process.cache.hdr_marshal_bytes',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.gc_bytes_evacuated',
        'name': 'proxy.process.cache.gc_bytes_evacuated',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.gc_frags_evacuated',
        'name': 'proxy.process.cache.gc_frags_evacuated',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.sync.count',
        'name': 'proxy.process.cache.sync.count',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.sync.bytes',
        'name': 'proxy.process.cache.sync.bytes',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.sync.time',
        'name': 'proxy.process.cache.sync.time',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.span.errors.read',
        'name': 'proxy.process.cache.span.errors.read',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.span.errors.write',
        'name': 'proxy.process.cache.span.errors.write',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.span.failing',
        'name': 'proxy.process.cache.span.failing',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.span.offline',
        'name': 'proxy.process.cache.span.offline',
        'tags': ('cache_volume',),
    },
    {
        'regex': r'proxy.process.cache.(.*?)\.span.online',
        'name': 'proxy.process.cache.span.online',
        'tags': ('cache_volume',),
    },
]


def build_metric(metric_name, logger):
    # type: (str, Any) -> Tuple[Optional[str], Optional[List[str]]]
    """
    proxy.node.restarts.proxy.restart_count
    proxy.process.cache.volume_1.span.offline
    proxy.process.http.101_responses
    """
    additional_tags = []
    name = metric_name
    found = False

    if COUNT_METRICS.get(metric_name):
        name = COUNT_METRICS.get(metric_name)
    elif GAUGE_METRICS.get(metric_name):
        name = GAUGE_METRICS.get(metric_name)
    else:
        found = False
        for regex in REGEX_METRICS:
            tags_values = []  # type: List[str]
            results = re.findall(str(regex['regex']), metric_name)

            if len(results) > 0 and isinstance(results[0], tuple):
                tags_values = list(results[0])
            else:
                tags_values = results

            if len(tags_values) == len(regex['tags']):
                found = True
                name = str(regex['name'])
                for i in range(len(regex['tags'])):
                    additional_tags.append('{}:{}'.format(regex['tags'][i], tags_values[i]))
                break

        if not found:
            logger.debug('Ignoring metric %s', metric_name)
            return None, None

    logger.debug('Found metric %s (%s)', name, metric_name)

    return name, additional_tags
