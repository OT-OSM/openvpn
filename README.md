#

OpenVPN Role
============

Ansible role to install OpenVPN. This role is tested on Canonical, Ubuntu, 16.04 LTS, amd64 xenial.
This role will setup openvpn server on Canonical, Ubuntu, 16.04 LTS, amd64 xenial on AWS Cloud

Note:  
 - Disable Source/Destination Check. 
     
     > From the list of instances, select the VPN instance and then Networking->Change Source/Dest. 
     > Check from the drop down menu. Then click Yes, Disable. This is needed as otherwise, your VPN  
     > server will not be able to connect to your other EC2 instances.

Directory Layout
----------------
```
osm_openvpn
.
├── defaults
│   └── main.yml
├── files
│   └── make_config.sh
├── handlers
│   └── main.yml
├── README.md
├── tasks
│   ├── client_keys.yaml
│   ├── config.yaml
│   ├── easy-rsa.yaml
│   ├── firewall.yaml
│   ├── install.yaml
│   ├── main.yaml
│   └── server_keys.yaml
└── templates
    ├── before.rules.j2
    ├── client.conf.j2
    └── server.conf.j2

5 directories, 14 files

```

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows.

```sh
---
server_name: "opstree"
client_name: "osm"
PROTOCOL: "tcp"
PORT: "1194"
openvpn_server_network: "10.8.0.0"
base_directory: "etc/openvpn"
...


```

Example Playbook
----------------
```
---
- name: It will automate OpenVPN setup
  hosts: server
  become_user: root
  gather_facts: true
  roles:
    - role: osm_openvpn
...

```
Client keys
-----------

Client keys will be generated in /tmp/{{client_name}}.ovpn of local host.
