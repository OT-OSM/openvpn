#!/bin/bash

cp /etc/openvpn/client.conf ./${1}.ovpn
	echo " " >> ./${1}.ovpn
	echo "<ca>" >> ./${1}.ovpn
	cat /etc/openvpn/ca.crt >> ./${1}.ovpn
	echo "</ca>" >> ./${1}.ovpn
	echo "<cert>" >> ./${1}.ovpn
	cat /etc/openvpn/${1}.crt >> ./${1}.ovpn
	echo "</cert>" >> ./${1}.ovpn
	echo "<key>" >> ./${1}.ovpn
	cat /etc/openvpn/${1}.key >> ./${1}.ovpn
	echo "</key>" >> ./${1}.ovpn
	echo "<tls-auth>" >> ./${1}.ovpn
	cat /etc/openvpn/ta.key >> ./${1}.ovpn
	echo "</tls-auth>" >> ./${1}.ovpn