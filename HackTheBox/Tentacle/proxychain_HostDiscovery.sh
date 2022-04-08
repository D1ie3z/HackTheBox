#!/bin/bash
for port in 21 22 25 80 443 445 8080 8081; do
for host in $(seq 1 254); do
		proxychains -q timeout 1 bash -c "echo '' > /dev/tcp/10.241.251.$host/$port" 2>/dev/null && echo "[+]Port $port -OPEN on Host 10.241.251.$host" &
	done; wait
done
