import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_gocd_agent_service_running(host):
    s = host.service('go-agent')

    assert s.is_running
    assert s.is_enabled


def test_gocd_agent_pointing_to_server(host):
    f = host.file("/usr/share/go-agent/wrapper-config/wrapper-properties.conf")

    assert f.contains("wrapper.app.parameter.101=http://localhost:8153/go")
