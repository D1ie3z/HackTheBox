#!/bin/bash

function ctrl_c(){
	echo -e "\n\n[+]Saliendo...\n"
	tput cnorm; exit 1
}
#Ctrl + c
trap ctrl_c INT

tput civis 
for port in $(seq 1 65535); do
	timeout 1 bash -c "echo '' > /dev/tcp/172.18.0.101/$port" 2>/dev/null && echo "[+]Port $port - OPEN" &
done; wait
tput cnorm
