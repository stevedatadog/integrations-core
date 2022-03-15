# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.dev import get_docker_hostname

HOST = get_docker_hostname()
PORT = '8529'

ARANGODB_VERSION = os.getenv('ARANGODB_VERSION')

METRICS = [
    'arangodb.agency.append',
    'arangodb.agency.cache.callback',
    'arangodb.agency.callback',
    'arangodb.agency.callback.registered.total',
    'arangodb.agency.client.lookup.table_size',
    'arangodb.agency.commit',
    'arangodb.agency.compaction',
    'arangodb.agency.local.commit.index',
    'arangodb.agency.log.size',
    'arangodb.agency.read.no_leader.total',
    'arangodb.agency.read.ok.total',
    'arangodb.agency.supervision.failed.server.total',
    'arangodb.agency.supervision.runtime',
    'arangodb.agency.supervision.runtime.wait.for.replication',
    'arangodb.agency.write',
    'arangodb.agency.write.no_leader.total',
    'arangodb.agency.write.ok.total',
    'arangodb.agency.request.time',
    'arangodb.network.forwarded.requests.total',
    'arangodb.network.request.timeouts.total',
    'arangodb.network.requests.in.flight',
    'arangodb.aql.all.query.total',
    'arangodb.aql.current.query',
    'arangodb.aql.global.memory.limit',
    'arangodb.aql.global.memory.usage',
    'arangodb.aql.global.query.memory.limit.reached.total',
    'arangodb.aql.local.query.memory.limit.reached.total',
    'arangodb.aql.query.time',
    'arangodb.aql.slow.query.time',
    'arangodb.client.connection.bytes.received',
    'arangodb.client.connections',
    'arangodb.client.connection.time',
    'arangodb.client.connection.io.time',
    'arangodb.client.connection.queue.time',
    'arangodb.client.connection.request.time',
    'arangodb.client.connection.total.time',
    'arangodb.http.async.requests.total',
    'arangodb.http.delete.requests.total',
    'arangodb.http.get.requests.total',
    'arangodb.http.head.requests.total',
    'arangodb.http.options.requests.total',
    'arangodb.http.patch.requests.total',
    'arangodb.http.post.requests.total',
    'arangodb.http.put.requests.total',
    'arangodb.http.other.requests.total',
    'arangodb.http.total.requests.total',
    'arangodb.http.user.requests.total',
    'arangodb.process.page.faults.major.total',
    'arangodb.process.page.faults.minor.total',
    'arangodb.process.threads',
    'arangodb.process.resident_set_size',
    'arangodb.process.system_time',
    'arangodb.process.user_time',
    'arangodb.process.virtual_memory_size',
    'arangodb.server.cpu_cores',
    'arangodb.server.idle_percent',
    'arangodb.server.iowait_percent',
    'arangodb.server.physical_memory',
    'arangodb.server.kernel_mode.percent',
    'arangodb.server.user_mode.percent',
    'arangodb.collection.lock.acquisition.total',
    'arangodb.collection.lock.sequential_mode.total',
    'arangodb.collection.lock.timeouts_exclusive.total',
    'arangodb.collection.lock.timeouts_write.total',
    'arangodb.transactions.read.total',
    'arangodb.transactions.aborted.total',
    'arangodb.transactions.committed.total',
    'arangodb.transactions.expired.total',
    'arangodb.transactions.started.total',
    'arangodb.rocksdb.collection_lock.acquisition_time',
    'arangodb.rocksdb.write.stalls.total',
    'arangodb.rocksdb.write.stops.total',
    'arangodb.rocksdb.actual.delayed.write.rate',
    'arangodb.rocksdb.archived.wal.files',
    'arangodb.rocksdb.background.errors',
    'arangodb.rocksdb.base.level',
    'arangodb.rocksdb.block.cache.capacity',
    'arangodb.rocksdb.block.cache.pinned.usage',
    'arangodb.rocksdb.block.cache.usage',
    'arangodb.rocksdb.cache.hit.rate.lifetime',
    'arangodb.rocksdb.cache.limit',
    'arangodb.rocksdb.compaction.pending',
    'arangodb.rocksdb.cur.size.active.mem.table',
    'arangodb.rocksdb.cur.size.all.mem.tables',
    'arangodb.rocksdb.engine.throttle.bps',
    'arangodb.rocksdb.estimate.live.data.size',
    'arangodb.rocksdb.estimate.num.keys',
    'arangodb.rocksdb.estimate.pending.compaction.bytes',
    'arangodb.rocksdb.estimate.table.readers.mem',
    'arangodb.rocksdb.free.disk.space',
    'arangodb.rocksdb.free.inodes',
    'arangodb.rocksdb.live.sst.files.size',
    'arangodb.rocksdb.mem.table.flush.pending',
    'arangodb.rocksdb.min.log.number.to.keep',
    'arangodb.rocksdb.num.deletes.active.mem.table',
    'arangodb.rocksdb.num.deletes.imm.mem.tables',
    'arangodb.rocksdb.num.entries.active.mem.table',
    'arangodb.rocksdb.num.entries.imm_mem.tables',
    'arangodb.rocksdb.num.immutable.mem.table',
    'arangodb.rocksdb.num.immutable.mem.table.flushed',
    'arangodb.rocksdb.num.live.versions',
    'arangodb.rocksdb.num.running.compactions',
    'arangodb.rocksdb.num.running.flushes',
    'arangodb.rocksdb.num.snapshots',
    'arangodb.rocksdb.prunable.wal.files',
    'arangodb.rocksdb.size.all.mem.tables',
    'arangodb.rocksdb.total.disk.space',
    'arangodb.health.dropped_followers.total',
    'arangodb.health.heartbeat_failures.total',
    'arangodb.health.heartbeat.sent.time',
]