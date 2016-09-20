# Docker image for Puppetboard
Docker image to run [Puppetboard](https://github.com/voxpupuli/puppetboard) (A web frontend for PuppetDB).

See the usage section for more details.

## Usage
Generic configuration can be driven by exporting the following enviroment variables:

| Environment variable  | Description | Default |
| ------------- | ------------- | ------------- |
| PUPPETBOARD_PUPPETDB_HOST | PuppetDB host | puppetdb |
| PUPPETBOARD_PUPPETDB_PORT | PuppetDB port | 8080 |
| PUPPETBOARD_PUPPETDB_SSL_VERIFY | Enable SSL verification for PuppetDB communication | false |
| PUPPETBOARD_PUPPETDB_KEY | SSL private key | |
| PUPPETBOARD_PUPPETDB_CERT | SSL public key | |
| PUPPETBOARD_PUPPETDB_TIMEOUT | PuppetDB query timeout | 20 |
| PUPPETBOARD_DEFAULT_ENVIRONMENT | Default environment | production |
| PUPPETBOARD_UNRESPONSIVE_HOURS | The amount of hours since the last check-in after which a node is considered unresponsive | 3 |
| PUPPETBOARD_ENABLE_QUERY | Query tab to show up in the web interface allowing users to write and execute arbitrary queries against a set of endpoints in PuppetDB | true |
| PUPPETBOARD_LOCALISE_TIMESTAMP | Localise timestamps | true |
| PUPPETBOARD_LOGLEVEL | A string representing the loglevel | info |
| PUPPETBOARD_REPORTS_COUNT | Limit of the number of reports to load on the node or any reports page | 10 |
| PUPPETBOARD_OFFLINE_MODE | Load static assets (jquery, semantic-ui, tablesorter, etc) from the local web server instead of a CDN | false |
| PUPPETBOARD_ENABLE_CATALOG | Allows the user to view a node's latest catalog | false |
| PUPPETBOARD_OVERVIEW_FILTER | | |
| PUPPETBOARD_GRAPH_FACTS | List of fact names to tell PuppetBoard to generate a pie-chart on the fact page | architecture clientversion domain lsbcodename lsbdistcodename lsbdistid lsbdistrelease lsbmajdistrelease netmask osfamily puppetversion processorcount |
| PUPPETBOARD_INVENTORY_FACTS | A list of tuples that serve as the column header and the fact name to search for to create the inventory page | [('Hostname','fqdn'),('IP Address','ipaddress'),('OS','lsbdistdescription'),('Architecture','hardwaremodel'),('Kernel Version','kernelrelease'),('Puppet Version','puppetversion')] |
| PUPPETBOARD_REFRESH_RATE | Number of seconds to wait until the index page is automatically refreshed | 30 |

## Run
```
docker run -d --restart=always -p 8000:8000 -e PUPPETBOARD_LOGLEVEL=warning m4ce/puppetboard
```

## Contact
Matteo Cerutti - matteo.cerutti@hotmail.co.uk
