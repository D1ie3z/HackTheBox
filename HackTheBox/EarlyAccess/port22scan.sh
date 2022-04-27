#!/bin/bash

function ctrl_c(){
	echo -e "\n\n[+]Saliendo...\n"
	tput cnorm; exit 1
}
#Ctrl + c
trap ctrl_c INT

hosts=(172.18.0.100 172.18.0.101 172.18.0.102 172.18.0.2 172.19.0.2 172.19.0.4)

tput civis 
for host in ${hosts[@]}; do
	timeout 1 bash -c "echo '' > /dev/tcp/$host/22" 2>/dev/null && echo "[+]Port 22 - OPEN on $host" &
done; wait
tput cnorm
