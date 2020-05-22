#!/usr/bin/env bash
#jalankan 5 async_server

python3 async_server.py 8000 &
python3 async_server.py 8001 &
python3 async_server.py 8002 &
python3 async_server.py 8003 &
python3 async_server.py 8004 &



