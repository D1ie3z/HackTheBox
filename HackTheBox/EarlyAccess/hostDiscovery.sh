#!/bin/bash

function ctrl_c(){
	echo -e "\n\n[!]Saliendo...\n"
	tput cnorm; exit 1
}

trap ctrl_c INT

hosts=(172.17.0 172.18.0 172.19.0)

tput civis
for network in ${hosts[@]}; do
	echo -e "\n Scanning in network $network.0/24 \n"
	for i in $(seq 1 254); do
		timeout 1 bash -c "ping -c 1 $network.$i" &>/dev/null && echo -e "[+] Host $network.$i - ACTIVE" &
	done; wait
done
tput cnorm
