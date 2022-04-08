#!/bin/bash

for port in $(seq 1 65535); do 
	proxychains -q timeout 1 bash -c "echo '' > /dev/tcp/10.197.243.31/$port" 2>/dev/null && echo "[*]Port $port - OPEN" &
done; wait
