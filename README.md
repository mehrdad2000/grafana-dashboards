# grafana-dashboards




## QuestDB

[Screenshot](https://github.com/mehrdad2000/grafana-dashboards/assets/26499665/924261db-123d-4751-ba52-334818fa05f9)

telegraf > questdb > grafana

1-import [Telegraf QuestDB Grafana System Dashboard](https://github.com/mehrdad2000/grafana-dashboards/blob/main/Telegraf_questdb_grafana_system%20dashboard.json) in your grafana.

2-add below variables:

```
host
SELECT DISTINCT host FROM cpu order by host asc;

mountpoint
SELECT DISTINCT path FROM disk;

cpu
SELECT DISTINCT cpu FROM cpu;

disk
SELECT DISTINCT name FROM diskio;

netif
SELECT DISTINCT interface  FROM net;
```

3-add below lines in telegraf config:

```
[[inputs.cpu]]
[[inputs.disk]]
[[inputs.diskio]]
[[inputs.kernel]]
[[inputs.mem]]
[[inputs.processes]]
[[inputs.swap]]
[[inputs.system]]
[[inputs.internal]]
[[inputs.interrupts]]
[[inputs.linux_sysctl_fs]]
[[inputs.net]]
 [[inputs.net_response]]
 [[inputs.netstat]]
 [[inputs.nstat]]
```


3-add below lines to telegraf config in case you use jolokia, it will rename jvm metrics that has special charecters (questdb can't store column name that has special charecter). this action able metrics to store on questdb.

```
 [[processors.rename]]

  [[processors.rename.replace]]
    field = "HeapMemoryUsage.max"
    dest = "HeapMemoryUsageMax"

  [[processors.rename.replace]]
    field = "NonHeapMemoryUsage.init"
    dest = "NonHeapMemoryUsageInit"

  [[processors.rename.replace]]
    field = "HeapMemoryUsage.init"
    dest = "HeapMemoryUsageInit"

  [[processors.rename.replace]]
    field = "HeapMemoryUsage.committed"
    dest = "HeapMemoryUsageCommitted"

  [[processors.rename.replace]]
    field = "HeapMemoryUsage.used"
    dest = "HeapMemoryUsageUsed"

  [[processors.rename.replace]]
    field = "NonHeapMemoryUsage.committed"
    dest = "NonHeapMemoryUsageCommitted"

  [[processors.rename.replace]]
    field = "NonHeapMemoryUsage.max"
    dest = "NonHeapMemoryUsageMax"

  [[processors.rename.replace]]
    field = "NonHeapMemoryUsage.used"
    dest = "NonHeapMemoryUsageUsed"


  [[processors.rename.replace]]
    field = "PeakUsage.used"
    dest = "PeakUsageUsed"

  [[processors.rename.replace]]
    field = "PeakUsage.init"
    dest = "PeakUsageInit"

  [[processors.rename.replace]]
    field = "PeakUsage.committed"
    dest = "PeakUsageCommitted"

  [[processors.rename.replace]]
    field = "PeakUsage.max"
    dest = "PeakUsageMax"

  [[processors.rename.replace]]
    field = "Usage.init"
    dest = "UsageInit"

  [[processors.rename.replace]]
    field = "Usage.max"
    dest = "UsageMax"

  [[processors.rename.replace]]
    field = "CollectionUsage.used"
    dest = "CollectionUsageUsed"

  [[processors.rename.replace]]
    field = "CollectionUsage.max"
    dest = "CollectionUsageMax"

  [[processors.rename.replace]]
    field = "Usage.used"
    dest = "UsageUsed"

  [[processors.rename.replace]]
    field = "Usage.committed"
    dest = "UsageCommitted"

  [[processors.rename.replace]]
    field = "CollectionUsage.init"
    dest = "CollectionUsageInit"

  [[processors.rename.replace]]
    field = "CollectionUsage.committed"
    dest = "CollectionUsageCommitted"


  [[processors.rename.replace]]
    field = "dentry-nr"
    dest = "dentrynr"

  [[processors.rename.replace]]
    field = "aio-max-nr"
    dest = "aiomaxnr"

  [[processors.rename.replace]]
    field = "file-nr"
    dest = "filenr"

  [[processors.rename.replace]]
    field = "aio-nr"
    dest = "aionr"

  [[processors.rename.replace]]
    field = "inode-nr"
    dest = "inodenr"

  [[processors.rename.replace]]
    field = "inode-preshrink-nr"
    dest = "inodepreshrinknr"

  [[processors.rename.replace]]
    field = "dentry-unused-nr"
    dest = "dentryunusednr"

  [[processors.rename.replace]]
    field = "file-max"
    dest = "filemax"

  [[processors.rename.replace]]
    field = "dentry-want-pages"
    dest = "dentrywantpages"

  [[processors.rename.replace]]
    field = "inode-free-nr"
    dest = "inodefreenr"

  [[processors.rename.replace]]
    field = "inode-free-nr"
    dest = "inodefreenr"

  [[processors.rename.replace]]
    field = "dentry-age-limit"
    dest = "dentryagelimit"
```






