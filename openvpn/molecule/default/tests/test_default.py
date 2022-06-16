import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# Test cases for install.yml

def test(host):
    os = host.system_info.distribution
    if os == 'debian':
        openvpn = host.package("openvpn")
        assert openvpn.is_installed
    if os == 'centos':
        assert host.group("nogroup").exists
        file1 = host.file("/etc/openvpn/client")
        file2 = host.file("/etc/openvpn/client")
        assert file1.user == "root"
        assert file1.group == "root"
        assert file2.user == "root"
        assert file2.group == "root"
        openvpn = host.package("openvpn")
        assert openvpn.is_installed

# Test cases for config.yml

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


