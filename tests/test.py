
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "almalinux", "rocky"]
    assert host.system_info.arch == 'x86_64' 

def test_user(host):
    assert host.user("prometheus").exists

def test_prometheus_config(host):
    prometheus_config = host.file("/etc/prometheus/prometheus.yml")
    assert prometheus_config.user == "root"
    assert prometheus_config.group == "root" 
    assert prometheus_config.mode == 0o644

def package_candidates(host):
    d = host.system_info.distribution.lower()
    if d in ("ubuntu", "debian"):
        return ["prometheus"]
    if d in ("redhat", "centos", "rocky", "almalinux"):
        return ["golang-github-prometheus", "prometheus"]
    return ["prometheus"]

def is_installed_any(host, names):
    return any(host.package(n).is_installed for n in names)

def test_prometheus_pkg_installed(host):
    assert is_installed_any(host, package_candidates(host)), \
        "Prometheus package not installed for this distro"

def test_prometheusd_running_and_enabled(host):
    prometheusd = host.service("prometheus")
    assert prometheusd.is_running
    assert prometheusd.is_enabled

def test_prometheusd_socket(host):
    prometheusd_v4 = host.socket("tcp://9090")
    prometheusd_v6 = host.socket("tcp://:::9090")
    assert prometheusd_v4.is_listening
    assert prometheusd_v6.is_listening

