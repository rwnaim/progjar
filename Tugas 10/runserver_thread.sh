#!/usr/bin/env bash
#jalankan 5 async_server

#python async_server.py 9001 &
python3 server_thread_http.py 9002 &
python3 server_thread_http.py 9003 &
python3 server_thread_http.py 9004 &
python3 server_thread_http.py 9005 &