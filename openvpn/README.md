Ansible Role: OpenVPN
=========





Salient Features
----------------
- This Role automates the VPN setup using OpenVPN.
The role consist of two meta files
- clientlist: Enter the namer of the client you want to add. (Along with password if password is enabled in variables)
- revokelist: Enter the names of the client you want to revoke.

### Note:  
  - Disable Source/Destination Check. 
     
     > From the list of instances, select the VPN instance and then Networking->Change Source/Dest. 
     > Check from the drop down menu. Then click Yes, Disable. This is needed as otherwise, your VPN  
     > server will not be able to connect to your other EC2 instances.
     
     > Write your mail id and password in /tasks/append_clientlist.yaml

Supported OS
------------
  * CentOS:7
  * CentOS:6
  * Ubuntu:bionic
  * Ubuntu:xenial
  * Amazon AMI
  * Amazon Linux 2 AMI

Dependencies
------------
* None :)


Directory Layout
----------------
```
osm_openvpn
.
├── clientlist
├── defaults
│   └── main.yml
├── files
│   └── make_config.sh
├── handlers
│   └── main.yml
├── media
│   ├── add_connection.png
│   ├── addvpn.jpg
│   ├── client.png
│   ├── import_file.png
│   ├── save_key.png
│   ├── select_file.png
│   └── vpn.jpg
├── meta
│   └── main.yaml
├── molecule
│   └── default
│       ├── Dockerfile.j2
│       ├── INSTALL.rst
│       ├── molecule.yml
│       ├── playbook.yml
│       └── tests
│           ├── test_default.py
│           └── test_default.pyc
├── README.md
├── revokelist
├── tasks
│   ├── append_clientlist.yaml
│   ├── client_keys.yaml
│   ├── config.yaml
│   ├── easy-rsa.yaml
│   ├── firewall.yaml
│   ├── install.yaml
│   ├── client_passwd_keys.yaml
│   ├── password_dependency.yaml
│   ├── main.yaml
│   ├── revoke.yaml
│   └── server_keys.yaml
└── templates
    ├── before.rules.j2
    ├── client.conf.j2
    └── server.conf.j2

```

Role Variables
--------------

|**Variables**| **Default Values**| **Description**| **Type**|
|----------|---------|---------------|-----------|
| server_name | server | OpenVPN server Name | Optional |
| PROTOCOL | udp | The protocaol on which the server will work | Mandatory |
| PORT | udp | The port on which the server will work | Mandatory |
| openvpn_server_network | 10.8.0.0 | CIDR range given to vpn network | Optional |
| base_directory | /etc/openvpn | Configuration path of openvpn server | Optional |
| easy_rsa_url | url | URL to download Easy RSA | Optional |
| password_enable | false | Enable password authentication along with file | Optional |
| block_all_connection | false | Block all communication for openvpn client | Optional |
| port_list | [80,443] | Allow specific ports for openvpn client & only applicable if block_all_connection == true | Optional |


Example Playbook
----------------
```
---
- name: It will automate OpenVPN setup
  hosts: server
  become: true
  no_log: true
  roles:
    - role: osm_openvpn
...

$  ansible-playbook site.yml -i inventory


```
Example clientlist file for password authentication
----------------
```
opstree Opstree@1234

```

- 

- For generating client keys

```sh
$  ansible-playbook site.yml -i inventory --tags "append_clientlist" -e "username=username_of_client" -e "mail=mail_id_of_client" --tags "generate_client_keys"

```

- For revoking client keys

```sh
$  ansible-playbook site.yml -i inventory --tags "revoke_client_keys"

```

Inventory
----------
An inventory should look like this:-
```ini
[server]                 
192.xxx.x.xxx    ansible_user=ubuntu 
```


Client keys
-----------

Client keys will be generated in /tmp/{{client_name}}.ovpn of local host.

For client Configuration
------------------------

Install OpenVpn

```sh
   apt-get install openvpn -y

```

Install Openvpn GUI for ubuntu 18.04 bionic beaver


```sh
   apt install network-manager-openvpn-gnome -y
```

After installing go to network settings


Add VPN to your network settings


Install Openvpn GUI for ubuntu 16.04 xenial

```sh
   apt install network-manager-openvpn-gnome -y
```

