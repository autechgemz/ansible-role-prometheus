# Ansible Role: prometheus

## Description

Manage the Prometheus monitoring system and time series database.

## Requirements

- Ansible 2.9 or higher

## Dependencies

None

## OS Platforms

- AlmaLinux 8 or higher 
- RockyLinux 8 or higher 
- Ubuntu 24.04 or higher

## Example Playbook

```yaml
- hosts: all
  roles:
    - prometheus
```

## Role Variables

### prometheus_debug: (default: false)

```yaml
prometheus_debug: false
```

### prometheus_install_source: (default: 'package')

```yaml
prometheus_install_source: 'package'
```

### prometheus_install_prefix: (default: '/opt')

* This parameter is only applicable when `prometheus_install_source` is set to `'binary'`.

```yaml
prometheus_install_prefix: '/opt'
```

### prometheus_install_url: (default: null)

* This parameter is only applicable when `prometheus_install_source` is set to `'binary'`.

```yaml
prometheus_install_url: null 
```

### prometheus_package_ensure: (default: present)

```yaml
prometheus_package_ensure: present
```

### prometheus_service_ensure: (default: 'started')

```yaml
prometheus_service_ensure: 'started'
```
### prometheus_service_enable: (default: true)

```yaml
prometheus_service_enable: true
```

### prometheus_daemon_config_options: (default: [])

```yaml
prometheus_daemon_config_options: []
```

### prometheus_config_options: (default: {})

```yaml
prometheus_config_options: {}
```

### prometheus_systemd_options: (default: {})

```yaml
prometheus_systemd_options: {}
```

## Handlers

The role includes the following handlers:

- `Restart prometheus`: Restarts the Prometheus service.
- `Reload prometheus`: Reloads the Prometheus service.

## Example vars

```yaml
prometheus_install_source: 'binary' 
```

## Example test 

```yaml
ansible-playbook -i 192.168.56.101, playbook.yml -e ansible_user=vagrant

py.test -v --hosts=all --ansible-inventory=hosts --connection=ansible tests/test.py
```

## License

This role is under the MIT License. See the LICENSE file for the full license text.
