# miniflux-init-db

[`miniflux-init-db`](https://github.com/bwolf/miniflux-init-db) is a simple init container for [Miniflux](https://miniflux.app) that create a database and the `hstore` extension.

Motivation: Miniflux will not (by design) create the database, user and extensions. `miniflux-init-db` does this, enabling to deploy Miniflux fully automatic to Kubernetes.


## Container Images
Please find container images on [docker hub](https://hub.docker.com/r/bwolf/gandi-dns-update).


## Example Use

``` yaml
# ...
initContainers:
- name: miniflux-init-db
  image: bwolf/miniflux-init-db:latest
  env:
  # values omitted for readability
  - name: DB_POSTGRES_HOST
  - name: DB_POSTGRES_PASSWORD
  - name: MINIFLUX_DB_NAME
  - name: MINIFLUX_DB_USERNAME
  - name: MINIFLUX_DB_PASSWORD
- name: init-miniflux
  image: miniflux
  command: ['sh', '-c', '/usr/bin/miniflux -migrate && /usr/bin/miniflux -create-admin']
  env:
  - name: DATABASE_URL
  - name: ADMIN_USERNAME
  - name: ADMIN_PASSWORD
containers:
- name: miniflux
  image: miniflux
  # ...
```
