# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import os

from datadog_checks.dev import get_docker_hostname

HERE = os.path.dirname(os.path.abspath(__file__))
COMPOSE_FILE = os.path.join(HERE, 'compose', 'docker-compose.yaml')
ROOT = os.path.dirname(os.path.dirname(HERE))
HOST = get_docker_hostname()
TRAFFIC_SERVER_VERSION = os.environ['TRAFFIC_SERVER_VERSION']

TRAFFIC_SERVER_URL = 'http://{}:8080/_stats'.format(HOST)

INSTANCE = {'traffic_server_url': TRAFFIC_SERVER_URL, 'tags': ['optional:tag1']}
INSTANCE_NO_URL = {'traffic_server_ur': TRAFFIC_SERVER_URL, 'tags': ['optional:tag1']}
INSTANCE_BAD_URL = {'traffic_server_url': '{}s'.format(TRAFFIC_SERVER_URL), 'tags': ['optional:tag1']}

# metrics that are not available in the e2e environment
NON_E2E_METRICS = [
    'process.http.origin_server_total_request_bytes',
    'process.origin_server_total_bytes',
    'process.user_agent_total_bytes',
    'process.cache.total_hits_bytes',
    'process.http.origin_server_total_response_bytes',
    'process.http.user_agent_total_request_bytes',
    'process.cache.total_misses_bytes',
    'process.cache.total_bytes',
    'process.cache.total_misses',
    'process.http.user_agent_total_response_bytes',
    'process.cache.total_hits',
    'process.cache.total_requests',
    'process.current_server_connections',
    'node.proxy_running',
]

EXPECTED_METRICS = [
    'traffic_server.node.config.draining',
    'traffic_server.node.config.reconfigure_required',
    'traffic_server.node.config.reconfigure_time',
    'traffic_server.node.config.restart_required.manager',
    'traffic_server.node.config.restart_required.proxy',
    'traffic_server.node.restarts.manager.start_time',
    'traffic_server.node.restarts.proxy.cache_ready_time',
    'traffic_server.node.restarts.proxy.restart_count',
    'traffic_server.node.restarts.proxy.start_time',
    'traffic_server.node.restarts.proxy.stop_time',
    'traffic_server.process.cache.KB_read_per_sec',
    'traffic_server.process.cache.KB_write_per_sec',
    'traffic_server.process.cache.bytes_total',
    'traffic_server.process.cache.bytes_used',
    'traffic_server.process.cache.directory_collision',
    'traffic_server.process.cache.direntries.total',
    'traffic_server.process.cache.direntries.used',
    'traffic_server.process.cache.evacuate.active',
    'traffic_server.process.cache.evacuate.failure',
    'traffic_server.process.cache.evacuate.success',
    'traffic_server.process.cache.frags_per_doc.1',
    'traffic_server.process.cache.frags_per_doc.2',
    'traffic_server.process.cache.frags_per_doc.3+',
    'traffic_server.process.cache.gc_bytes_evacuated',
    'traffic_server.process.cache.gc_frags_evacuated',
    'traffic_server.process.cache.hdr_marshal_bytes',
    'traffic_server.process.cache.hdr_marshals',
    'traffic_server.process.cache.lookup.active',
    'traffic_server.process.cache.lookup.failure',
    'traffic_server.process.cache.lookup.success',
    'traffic_server.process.cache.percent_full',
    'traffic_server.process.cache.pread_count',
    'traffic_server.process.cache.ram_cache.bytes_used',
    'traffic_server.process.cache.ram_cache.hits',
    'traffic_server.process.cache.ram_cache.misses',
    'traffic_server.process.cache.ram_cache.total_bytes',
    'traffic_server.process.cache.read.active',
    'traffic_server.process.cache.read.failure',
    'traffic_server.process.cache.read.success',
    'traffic_server.process.cache.read_busy.failure',
    'traffic_server.process.cache.read_busy.success',
    'traffic_server.process.cache.read_per_sec',
    'traffic_server.process.cache.remove.active',
    'traffic_server.process.cache.remove.failure',
    'traffic_server.process.cache.remove.success',
    'traffic_server.process.cache.scan.active',
    'traffic_server.process.cache.scan.failure',
    'traffic_server.process.cache.scan.success',
    'traffic_server.process.cache.span.errors.read',
    'traffic_server.process.cache.span.errors.write',
    'traffic_server.process.cache.span.failing',
    'traffic_server.process.cache.span.offline',
    'traffic_server.process.cache.span.online',
    'traffic_server.process.cache.sync.bytes',
    'traffic_server.process.cache.sync.count',
    'traffic_server.process.cache.sync.time',
    'traffic_server.process.cache.update.active',
    'traffic_server.process.cache.update.failure',
    'traffic_server.process.cache.update.success',
    'traffic_server.process.cache.vector_marshals',
    'traffic_server.process.cache.wrap_count',
    'traffic_server.process.cache.write.active',
    'traffic_server.process.cache.write.backlog.failure',
    'traffic_server.process.cache.write.failure',
    'traffic_server.process.cache.write.success',
    'traffic_server.process.cache.write_bytes_stat',
    'traffic_server.process.cache.write_per_sec',
    'traffic_server.process.dns.fail_avg_time',
    'traffic_server.process.dns.in_flight',
    'traffic_server.process.dns.lookup_avg_time',
    'traffic_server.process.dns.lookup_failures',
    'traffic_server.process.dns.lookup_successes',
    'traffic_server.process.dns.max_retries_exceeded',
    'traffic_server.process.dns.retries',
    'traffic_server.process.dns.success_avg_time',
    'traffic_server.process.dns.tcp_reset',
    'traffic_server.process.dns.tcp_retries',
    'traffic_server.process.dns.total_dns_lookups',
    'traffic_server.process.eventloop.count.1000s',
    'traffic_server.process.eventloop.count.100s',
    'traffic_server.process.eventloop.count.10s',
    'traffic_server.process.eventloop.events.1000s',
    'traffic_server.process.eventloop.events.100s',
    'traffic_server.process.eventloop.events.10s',
    'traffic_server.process.eventloop.events.max.1000s',
    'traffic_server.process.eventloop.events.max.100s',
    'traffic_server.process.eventloop.events.max.10s',
    'traffic_server.process.eventloop.events.min.1000s',
    'traffic_server.process.eventloop.events.min.100s',
    'traffic_server.process.eventloop.events.min.10s',
    'traffic_server.process.eventloop.time.max.1000s',
    'traffic_server.process.eventloop.time.max.100s',
    'traffic_server.process.eventloop.time.max.10s',
    'traffic_server.process.eventloop.time.min.1000s',
    'traffic_server.process.eventloop.time.min.100s',
    'traffic_server.process.eventloop.time.min.10s',
    'traffic_server.process.eventloop.wait.1000s',
    'traffic_server.process.eventloop.wait.100s',
    'traffic_server.process.eventloop.wait.10s',
    'traffic_server.process.hostdb.cache.current_items',
    'traffic_server.process.hostdb.cache.current_size',
    'traffic_server.process.hostdb.cache.last_sync.time',
    'traffic_server.process.hostdb.cache.last_sync.total_items',
    'traffic_server.process.hostdb.cache.last_sync.total_size',
    'traffic_server.process.hostdb.cache.total_failed_inserts',
    'traffic_server.process.hostdb.cache.total_hits',
    'traffic_server.process.hostdb.cache.total_inserts',
    'traffic_server.process.hostdb.cache.total_lookups',
    'traffic_server.process.hostdb.insert_duplicate_to_pending_dns',
    'traffic_server.process.hostdb.re_dns_on_reload',
    'traffic_server.process.hostdb.total_hits',
    'traffic_server.process.hostdb.total_lookups',
    'traffic_server.process.hostdb.ttl',
    'traffic_server.process.hostdb.ttl_expires',
    'traffic_server.process.http.1xx_responses',
    'traffic_server.process.http.2xx_responses',
    'traffic_server.process.http.3xx_responses',
    'traffic_server.process.http.4xx_responses',
    'traffic_server.process.http.5xx_responses',
    'traffic_server.process.http.avg_transactions_per_client_connection',
    'traffic_server.process.http.avg_transactions_per_server_connection',
    'traffic_server.process.http.background_fill_bytes_aborted',
    'traffic_server.process.http.background_fill_bytes_completed',
    'traffic_server.process.http.background_fill_current_count',
    'traffic_server.process.http.background_fill_total_count',
    'traffic_server.process.http.broken_server_connections',
    'traffic_server.process.http.cache.hit_fresh',
    'traffic_server.process.http.cache.hit_ims',
    'traffic_server.process.http.cache.hit_mem_fresh',
    'traffic_server.process.http.cache.hit_revalidated',
    'traffic_server.process.http.cache.hit_stale_served',
    'traffic_server.process.http.cache.miss_changed',
    'traffic_server.process.http.cache.miss_client_no_cache',
    'traffic_server.process.http.cache.miss_client_not_cacheable',
    'traffic_server.process.http.cache.miss_cold',
    'traffic_server.process.http.cache.miss_ims',
    'traffic_server.process.http.cache.open_write.adjust_thread',
    'traffic_server.process.http.cache.read_error',
    'traffic_server.process.http.cache_deletes',
    'traffic_server.process.http.cache_lookups',
    'traffic_server.process.http.cache_read_errors',
    'traffic_server.process.http.cache_updates',
    'traffic_server.process.http.cache_write_errors',
    'traffic_server.process.http.cache_writes',
    'traffic_server.process.http.completed_requests',
    'traffic_server.process.http.connect_requests',
    'traffic_server.process.http.current_active_client_connections',
    'traffic_server.process.http.current_cache_connections',
    'traffic_server.process.http.current_client_connections',
    'traffic_server.process.http.current_client_transactions',
    'traffic_server.process.http.current_parent_proxy_connections',
    'traffic_server.process.http.current_server_connections',
    'traffic_server.process.http.current_server_transactions',
    'traffic_server.process.http.dead_server.no_requests',
    'traffic_server.process.http.delete_requests',
    'traffic_server.process.http.disallowed_post_100_continue',
    'traffic_server.process.http.error.client_abort_count',
    'traffic_server.process.http.error.client_abort_origin_server_bytes',
    'traffic_server.process.http.error.client_abort_user_agent_bytes',
    'traffic_server.process.http.error.client_read_error_count',
    'traffic_server.process.http.error.client_read_error_origin_server_bytes',
    'traffic_server.process.http.error.client_read_error_user_agent_bytes',
    'traffic_server.process.http.error.connect_fail_origin_server_bytes',
    'traffic_server.process.http.error.connect_fail_user_agent_bytes',
    'traffic_server.process.http.errpr.connect_fail_count',
    'traffic_server.process.http.extension_method_requests',
    'traffic_server.process.http.get_requests',
    'traffic_server.process.http.head_requests',
    'traffic_server.process.http.http_misc_origin_server_bytes',
    'traffic_server.process.http.incoming_requests',
    'traffic_server.process.http.incoming_responses',
    'traffic_server.process.http.invalid_client_requests',
    'traffic_server.process.http.milestone.cache_open_read_begin',
    'traffic_server.process.http.milestone.cache_open_read_end',
    'traffic_server.process.http.milestone.cache_open_write_begin',
    'traffic_server.process.http.milestone.cache_open_write_end',
    'traffic_server.process.http.milestone.dns_lookup_begin',
    'traffic_server.process.http.milestone.dns_lookup_end',
    'traffic_server.process.http.milestone.server_begin_write',
    'traffic_server.process.http.milestone.server_close',
    'traffic_server.process.http.milestone.server_connect',
    'traffic_server.process.http.milestone.server_connect_end',
    'traffic_server.process.http.milestone.server_first_connect',
    'traffic_server.process.http.milestone.server_first_read',
    'traffic_server.process.http.milestone.server_read_header_done',
    'traffic_server.process.http.milestone.sm_finish',
    'traffic_server.process.http.milestone.sm_start',
    'traffic_server.process.http.milestone.ua_begin',
    'traffic_server.process.http.milestone.ua_begin_write',
    'traffic_server.process.http.milestone.ua_close',
    'traffic_server.process.http.milestone.ua_first_read',
    'traffic_server.process.http.milestone.ua_read_header_done',
    'traffic_server.process.http.misc_count',
    'traffic_server.process.http.misc_user_agent_bytes',
    'traffic_server.process.http.missing_host_hdr',
    'traffic_server.process.http.options_requests',
    'traffic_server.process.http.origin.connect.adjust_thread',
    'traffic_server.process.http.origin_connections_throttled_out',
    'traffic_server.process.http.origin_server_request_document_total_size',
    'traffic_server.process.http.origin_server_request_header_total_size',
    'traffic_server.process.http.origin_server_response_document_total_size',
    'traffic_server.process.http.origin_server_response_header_total_size',
    'traffic_server.process.http.origin_server_speed_bytes_per_sec_100',
    'traffic_server.process.http.origin_server_speed_bytes_per_sec_100K',
    'traffic_server.process.http.origin_server_speed_bytes_per_sec_100M',
    'traffic_server.process.http.origin_server_speed_bytes_per_sec_10K',
    'traffic_server.process.http.origin_server_speed_bytes_per_sec_10M',
    'traffic_server.process.http.origin_server_speed_bytes_per_sec_1K',
    'traffic_server.process.http.origin_server_speed_bytes_per_sec_1M',
    'traffic_server.process.http.origin_shutdown.cleanup_entry',
    'traffic_server.process.http.origin_shutdown.migration_failure',
    'traffic_server.process.http.origin_shutdown.pool_lock_contention',
    'traffic_server.process.http.origin_shutdown.release_invalid_request',
    'traffic_server.process.http.origin_shutdown.release_invalid_response',
    'traffic_server.process.http.origin_shutdown.release_misc',
    'traffic_server.process.http.origin_shutdown.release_modified',
    'traffic_server.process.http.origin_shutdown.release_no_keep_alive',
    'traffic_server.process.http.origin_shutdown.release_no_server',
    'traffic_server.process.http.origin_shutdown.release_no_sharing',
    'traffic_server.process.http.origin_shutdown.tunnel_abort',
    'traffic_server.process.http.origin_shutdown.tunnel_client',
    'traffic_server.process.http.origin_shutdown.tunnel_server',
    'traffic_server.process.http.origin_shutdown.tunnel_server_detach',
    'traffic_server.process.http.origin_shutdown.tunnel_server_eos',
    'traffic_server.process.http.origin_shutdown.tunnel_server_no_keep_alive',
    'traffic_server.process.http.origin_shutdown.tunnel_server_plugin_tunnel',
    'traffic_server.process.http.origin_shutdown.tunnel_transform_read',
    'traffic_server.process.http.outgoing_requests',
    'traffic_server.process.http.parent_proxy_request_total_bytes',
    'traffic_server.process.http.parent_proxy_response_total_bytes',
    'traffic_server.process.http.parent_proxy_transaction_time',
    'traffic_server.process.http.post_body_too_large',
    'traffic_server.process.http.post_requests',
    'traffic_server.process.http.purge_requests',
    'traffic_server.process.http.push_requests',
    'traffic_server.process.http.pushed_document_total_size',
    'traffic_server.process.http.pushed_response_header_total_size',
    'traffic_server.process.http.put_requests',
    'traffic_server.process.http.request_document_size_100',
    'traffic_server.process.http.request_document_size_10K',
    'traffic_server.process.http.request_document_size_1K',
    'traffic_server.process.http.request_document_size_1M',
    'traffic_server.process.http.request_document_size_3K',
    'traffic_server.process.http.request_document_size_5K',
    'traffic_server.process.http.request_document_size_inf',
    'traffic_server.process.http.response_document_size_100',
    'traffic_server.process.http.response_document_size_10K',
    'traffic_server.process.http.response_document_size_1K',
    'traffic_server.process.http.response_document_size_1M',
    'traffic_server.process.http.response_document_size_3K',
    'traffic_server.process.http.response_document_size_5K',
    'traffic_server.process.http.response_document_size_inf',
    'traffic_server.process.http.tcp.client_refresh_count',
    'traffic_server.process.http.tcp.client_refresh_origin_server_bytes',
    'traffic_server.process.http.tcp.client_refresh_user_agent_bytes',
    'traffic_server.process.http.tcp.expired_miss_count',
    'traffic_server.process.http.tcp.expired_miss_origin_server_bytes',
    'traffic_server.process.http.tcp.expired_miss_user_agent_bytes',
    'traffic_server.process.http.tcp.hit_count',
    'traffic_server.process.http.tcp.hit_origin_server_bytes',
    'traffic_server.process.http.tcp.hit_user_agent_bytes',
    'traffic_server.process.http.tcp.ims_hit_count',
    'traffic_server.process.http.tcp.ims_hit_origin_server_bytes',
    'traffic_server.process.http.tcp.ims_hit_user_agent_bytes',
    'traffic_server.process.http.tcp.ims_miss_count',
    'traffic_server.process.http.tcp.ims_miss_origin_server_bytes',
    'traffic_server.process.http.tcp.ims_miss_user_agent_bytes',
    'traffic_server.process.http.tcp.miss_count',
    'traffic_server.process.http.tcp.miss_origin_server_bytes',
    'traffic_server.process.http.tcp.miss_origin_server_bytes',
    'traffic_server.process.http.tcp.miss_user_agent_bytes',
    'traffic_server.process.http.tcp.miss_user_agent_bytes',
    'traffic_server.process.http.tcp.refresh_hit_count',
    'traffic_server.process.http.tcp.refresh_hit_origin_server_bytes',
    'traffic_server.process.http.tcp.refresh_hit_user_agent_bytes',
    'traffic_server.process.http.tcp.refresh_miss_count',
    'traffic_server.process.http.tcp.refresh_miss_origin_server_bytes',
    'traffic_server.process.http.tcp.refresh_miss_user_agent_bytes',
    'traffic_server.process.http.total_client_connections',
    'traffic_server.process.http.total_client_connections_ipv4',
    'traffic_server.process.http.total_client_connections_ipv6',
    'traffic_server.process.http.total_incoming_connections',
    'traffic_server.process.http.total_parent_marked_down_count',
    'traffic_server.process.http.total_parent_proxy_connections',
    'traffic_server.process.http.total_parent_retries',
    'traffic_server.process.http.total_parent_retries_exhausted',
    'traffic_server.process.http.total_parent_switches',
    'traffic_server.process.http.total_server_connections',
    'traffic_server.process.http.total_transactions_time',
    'traffic_server.process.http.total_x_redirect_count',
    'traffic_server.process.http.trace_requests',
    'traffic_server.process.http.transaction_counts.errors.aborts',
    'traffic_server.process.http.transaction_counts.errors.connect_failed',
    'traffic_server.process.http.transaction_counts.errors.other',
    'traffic_server.process.http.transaction_counts.errors.possible_aborts',
    'traffic_server.process.http.transaction_counts.errors.pre_accept_hangups',
    'traffic_server.process.http.transaction_counts.hit_fresh',
    'traffic_server.process.http.transaction_counts.hit_fresh.process',
    'traffic_server.process.http.transaction_counts.hit_revalidated',
    'traffic_server.process.http.transaction_counts.miss_changed',
    'traffic_server.process.http.transaction_counts.miss_client_no_cache',
    'traffic_server.process.http.transaction_counts.miss_cold',
    'traffic_server.process.http.transaction_counts.miss_not_cacheable',
    'traffic_server.process.http.transaction_counts.other.unclassified',
    'traffic_server.process.http.transaction_totaltime.errors.aborts',
    'traffic_server.process.http.transaction_totaltime.errors.connect_failed',
    'traffic_server.process.http.transaction_totaltime.errors.other',
    'traffic_server.process.http.transaction_totaltime.errors.possible_aborts',
    'traffic_server.process.http.transaction_totaltime.hit_fresh',
    'traffic_server.process.http.transaction_totaltime.hit_fresh.process',
    'traffic_server.process.http.transaction_totaltime.hit_revalidated',
    'traffic_server.process.http.transaction_totaltime.miss_changed',
    'traffic_server.process.http.transaction_totaltime.miss_client_no_cache',
    'traffic_server.process.http.transaction_totaltime.miss_cold',
    'traffic_server.process.http.transaction_totaltime.miss_not_cacheable',
    'traffic_server.process.http.transaction_totaltime.other.unclassified',
    'traffic_server.process.http.tunnels',
    'traffic_server.process.http.user_agent_request_document_total_size',
    'traffic_server.process.http.user_agent_request_header_total_size',
    'traffic_server.process.http.user_agent_response_document_total_size',
    'traffic_server.process.http.user_agent_response_header_total_size',
    'traffic_server.process.http.user_agent_speed_bytes_per_sec_100',
    'traffic_server.process.http.user_agent_speed_bytes_per_sec_100K',
    'traffic_server.process.http.user_agent_speed_bytes_per_sec_100M',
    'traffic_server.process.http.user_agent_speed_bytes_per_sec_10K',
    'traffic_server.process.http.user_agent_speed_bytes_per_sec_10M',
    'traffic_server.process.http.user_agent_speed_bytes_per_sec_1K',
    'traffic_server.process.http.user_agent_speed_bytes_per_sec_1M',
    'traffic_server.process.http.websocket.current_active_client_connections',
    'traffic_server.process.http2.connection_errors',
    'traffic_server.process.http2.current_active_client_connections',
    'traffic_server.process.http2.current_client_connections',
    'traffic_server.process.http2.current_client_streams',
    'traffic_server.process.http2.insufficient_avg_window_update',
    'traffic_server.process.http2.max_ping_frames_per_minute_exceeded',
    'traffic_server.process.http2.max_settings_frames_per_minute_exceeded',
    'traffic_server.process.http2.max_settings_per_frame_exceeded',
    'traffic_server.process.http2.max_settings_per_minute_exceeded',
    'traffic_server.process.http2.session_die_active',
    'traffic_server.process.http2.session_die_default',
    'traffic_server.process.http2.session_die_eos',
    'traffic_server.process.http2.session_die_error',
    'traffic_server.process.http2.session_die_high_error_rate',
    'traffic_server.process.http2.session_die_inactive',
    'traffic_server.process.http2.session_die_other',
    'traffic_server.process.http2.stream_errors',
    'traffic_server.process.http2.total_client_connections',
    'traffic_server.process.http2.total_client_streams',
    'traffic_server.process.http2.total_transactions_time',
    'traffic_server.process.https.incoming_requests',
    'traffic_server.process.https.total_client_connections',
    'traffic_server.process.log.bytes_flush_to_disk',
    'traffic_server.process.log.bytes_lost_before_flush_to_disk',
    'traffic_server.process.log.bytes_lost_before_preproc',
    'traffic_server.process.log.bytes_lost_before_sent_to_network',
    'traffic_server.process.log.bytes_lost_before_written_to_disk',
    'traffic_server.process.log.bytes_received_from_network',
    'traffic_server.process.log.bytes_sent_to_network',
    'traffic_server.process.log.bytes_written_to_disk',
    'traffic_server.process.log.event_log_access_aggr',
    'traffic_server.process.log.event_log_access_fail',
    'traffic_server.process.log.event_log_access_full',
    'traffic_server.process.log.event_log_access_ok',
    'traffic_server.process.log.event_log_access_skip',
    'traffic_server.process.log.event_log_error_aggr',
    'traffic_server.process.log.event_log_error_fail',
    'traffic_server.process.log.event_log_error_full',
    'traffic_server.process.log.event_log_error_ok',
    'traffic_server.process.log.event_log_error_skip',
    'traffic_server.process.log.log_files_open',
    'traffic_server.process.log.log_files_space_used',
    'traffic_server.process.log.num_flush_to_disk',
    'traffic_server.process.log.num_lost_before_flush_to_disk',
    'traffic_server.process.log.num_lost_before_sent_to_network',
    'traffic_server.process.log.num_received_from_network',
    'traffic_server.process.log.num_sent_to_network',
    'traffic_server.process.net.accepts_currently_open',
    'traffic_server.process.net.calls_to_read',
    'traffic_server.process.net.calls_to_read_nodata',
    'traffic_server.process.net.calls_to_readfromnet',
    'traffic_server.process.net.calls_to_readfromnet_afterpoll',
    'traffic_server.process.net.calls_to_write',
    'traffic_server.process.net.calls_to_write_nodata',
    'traffic_server.process.net.calls_to_writetonet',
    'traffic_server.process.net.calls_to_writetonet_afterpoll',
    'traffic_server.process.net.connections_currently_open',
    'traffic_server.process.net.connections_throttled_in',
    'traffic_server.process.net.connections_throttled_out',
    'traffic_server.process.net.default_inactivity_timeout_applied',
    'traffic_server.process.net.default_inactivity_timeout_count',
    'traffic_server.process.net.dynamic_keep_alive_timeout_in_count',
    'traffic_server.process.net.dynamic_keep_alive_timeout_in_total',
    'traffic_server.process.net.fastopen_out.attempts',
    'traffic_server.process.net.fastopen_out.successes',
    'traffic_server.process.net.inactivity_cop_lock_acquire_failure',
    'traffic_server.process.net.max.requests_throttled_in',
    'traffic_server.process.net.net_handler_run',
    'traffic_server.process.net.read_bytes',
    'traffic_server.process.net.write_bytes',
    'traffic_server.process.socks.connections_currently_open',
    'traffic_server.process.socks.connections_successful',
    'traffic_server.process.socks.connections_unsuccessful',
    'traffic_server.process.ssl.cipher.user_agent',
    'traffic_server.process.ssl.early_data_received',
    'traffic_server.process.ssl.max_record_size_count',
    'traffic_server.process.ssl.ocsp_refresh_cert_failure',
    'traffic_server.process.ssl.ocsp_refreshed_cert',
    'traffic_server.process.ssl.origin_server_bad_cert',
    'traffic_server.process.ssl.origin_server_cert_verify_failed',
    'traffic_server.process.ssl.origin_server_decryption_failed',
    'traffic_server.process.ssl.origin_server_expired_cert',
    'traffic_server.process.ssl.origin_server_other_errors',
    'traffic_server.process.ssl.origin_server_revoked_cert',
    'traffic_server.process.ssl.origin_server_unknown_ca',
    'traffic_server.process.ssl.origin_server_unknown_cert',
    'traffic_server.process.ssl.origin_server_wrong_version',
    'traffic_server.process.ssl.redo_record_size_count',
    'traffic_server.process.ssl.ssl_error_async',
    'traffic_server.process.ssl.ssl_error_ssl',
    'traffic_server.process.ssl.ssl_error_syscall',
    'traffic_server.process.ssl.ssl_ocsp_revoked_cert_stat',
    'traffic_server.process.ssl.ssl_ocsp_unknown_cert_stat',
    'traffic_server.process.ssl.ssl_session_cache_eviction',
    'traffic_server.process.ssl.ssl_session_cache_hit',
    'traffic_server.process.ssl.ssl_session_cache_lock_contention',
    'traffic_server.process.ssl.ssl_session_cache_miss',
    'traffic_server.process.ssl.ssl_session_cache_new_session',
    'traffic_server.process.ssl.ssl_sni_name_set_failure',
    'traffic_server.process.ssl.ssl_total_sslv3',
    'traffic_server.process.ssl.ssl_total_tlsv1',
    'traffic_server.process.ssl.ssl_total_tlsv11',
    'traffic_server.process.ssl.ssl_total_tlsv12',
    'traffic_server.process.ssl.ssl_total_tlsv13',
    'traffic_server.process.ssl.total_attempts_handshake_count_in',
    'traffic_server.process.ssl.total_attempts_handshake_count_out',
    'traffic_server.process.ssl.total_handshake_time',
    'traffic_server.process.ssl.total_success_handshake_count_in',
    'traffic_server.process.ssl.total_success_handshake_count_out',
    'traffic_server.process.ssl.total_ticket_keys_renewed',
    'traffic_server.process.ssl.total_tickets_created',
    'traffic_server.process.ssl.total_tickets_not_found',
    'traffic_server.process.ssl.total_tickets_renewed',
    'traffic_server.process.ssl.total_tickets_verified',
    'traffic_server.process.ssl.total_tickets_verified_old_key',
    'traffic_server.process.ssl.user_agent_bad_cert',
    'traffic_server.process.ssl.user_agent_cert_verify_failed',
    'traffic_server.process.ssl.user_agent_decryption_failed',
    'traffic_server.process.ssl.user_agent_expired_cert',
    'traffic_server.process.ssl.user_agent_other_errors',
    'traffic_server.process.ssl.user_agent_revoked_cert',
    'traffic_server.process.ssl.user_agent_session_hit',
    'traffic_server.process.ssl.user_agent_session_miss',
    'traffic_server.process.ssl.user_agent_session_timeout',
    'traffic_server.process.ssl.user_agent_sessions',
    'traffic_server.process.ssl.user_agent_unknown_ca',
    'traffic_server.process.ssl.user_agent_unknown_cert',
    'traffic_server.process.ssl.user_agent_wrong_version',
    'traffic_server.process.tcp.total_accepts',
    'traffic_server.process.traffic_server.memory.rss',
    'traffic_server.process.traffic_server.memory.rss',
    'traffic_server.process.cache.volume.bytes_total',
    'traffic_server.process.cache.volume.directory_collision',
    'traffic_server.process.cache.volume.direntries.total',
    'traffic_server.process.cache.volume.direntries.used',
    'traffic_server.process.cache.volume.evacuate.active',
    'traffic_server.process.cache.volume.evacuate.failure',
    'traffic_server.process.cache.volume.evacuate.success',
    'traffic_server.process.cache.volume.frags_per_doc.1',
    'traffic_server.process.cache.volume.frags_per_doc.2',
    'traffic_server.process.cache.volume.frags_per_doc.3',
    'traffic_server.process.cache.volume.gc_bytes_evacuated',
    'traffic_server.process.cache.volume.gc_frags_evacuated',
    'traffic_server.process.cache.volume.hdr_marshal_bytes',
    'traffic_server.process.cache.volume.hdr_marshals',
    'traffic_server.process.cache.volume.lookup.active',
    'traffic_server.process.cache.volume.lookup.failure',
    'traffic_server.process.cache.volume.lookup.success',
    'traffic_server.process.cache.volume.percent_full',
    'traffic_server.process.cache.volume.pread_count',
    'traffic_server.process.cache.volume.ram_cache.hits',
    'traffic_server.process.cache.volume.ram_cache.misses',
    'traffic_server.process.cache.volume.ram_cache.total_bytes',
    'traffic_server.process.cache.volume.read.active',
    'traffic_server.process.cache.volume.read.failure',
    'traffic_server.process.cache.volume.read.success',
    'traffic_server.process.cache.volume.read_busy.failure',
    'traffic_server.process.cache.volume.read_busy.success',
    'traffic_server.process.cache.volume.remove.active',
    'traffic_server.process.cache.volume.remove.failure',
    'traffic_server.process.cache.volume.remove.success',
    'traffic_server.process.cache.volume.scan.active',
    'traffic_server.process.cache.volume.scan.failure',
    'traffic_server.process.cache.volume.scan.success',
    'traffic_server.process.cache.volume.span.errors.read',
    'traffic_server.process.cache.volume.span.errors.write',
    'traffic_server.process.cache.volume.span.failing',
    'traffic_server.process.cache.volume.span.offline',
    'traffic_server.process.cache.volume.span.online',
    'traffic_server.process.cache.volume.sync.bytes',
    'traffic_server.process.cache.volume.sync.count',
    'traffic_server.process.cache.volume.sync.time',
    'traffic_server.process.cache.volume.update.active',
    'traffic_server.process.cache.volume.update.failure',
    'traffic_server.process.cache.volume.update.success',
    'traffic_server.process.cache.volume.vector_marshals',
    'traffic_server.process.cache.volume.write.active',
    'traffic_server.process.cache.volume.write.backlog.failure',
    'traffic_server.process.cache.volume.write.failure',
    'traffic_server.process.cache.volume.write.success',
    'traffic_server.process.cache.volume.write_bytes_stat',
    'traffic_server.process.http.pooled_server_connections',
    'traffic_server.process.http2.max_priority_frames_per_minute_exceeded',
    'traffic_server.process.ssl.default_record_size_count',
    'traffic_server.process.cache.volume.bytes_used',
    'traffic_server.process.cache.volume.ram_cache.bytes_used',
]
