import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_gocd_server_service_running(host):
    s = host.service('go-server')

    assert s.is_running
    assert s.is_enabled


def test_gocd_server_port_listening(host):
    s = host.socket("tcp://0.0.0.0:8153")

    assert s.is_listening

def test_gocd_kubernetes_plugin_exists(host):
    s = host.file("/var/lib/go-server/plugins/external/kubernetes-elastic-agent-3.6.0-209.jar")

    assert s.exists