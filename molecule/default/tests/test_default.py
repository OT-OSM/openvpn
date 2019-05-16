import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

#def test_nginx_is_installed(host):
#    grafana = host.package("grafana")
#    assert grafana.is_installed


def test_config_file(host):
    f1 = host.file('etc/openvpn/server.conf')
    f2 = host.file('etc/openvpn/client.conf')
    f3 = host.file('/etc/openvpn/easy-rsa/easyrsa')
    f4 = host.file('etc/apache2/conf-available/openvpn-monitor.conf')
    assert f1.exists
    assert f1.is_file
    assert f2.exists
    assert f2.is_file
    assert f1.contains("port 1194")
    assert f1.contains("proto udp")
 #  assert f2.contains("remote  1194")
    assert f2.contains("proto udp")
    assert f3.exists
    assert f3.is_file
    assert f4.exists
    assert f4.is_file

#def test_dashboard_dir(host):
#    d = host.file('/var/lib/grafana/dashboards')
#    assert d.exists
#    assert d.is_directory
#    assert d.user == "grafana"
#    assert d.group == "grafana"
#    assert d.mode == 0755

#def test_nginx_running_and_enabled(host):
#    os = host.system_info.distribution
#    if os == 'debian':
#     grafana = host.service("grafana-server")
#     assert grafana.is_running
#     assert grafana.is_enabled

#def test_grafana_is_listening(host):
#    assert host.socket('tcp://127.0.0.1:3000').is_listening

