#!/usr/bin/env python
# coding: utf-8

import sys
import clickhouse_connect
from dotenv import dotenv_values
from urllib3.exceptions import ConnectTimeoutError, MaxRetryError
from clickhouse_connect.driver.exceptions import OperationalError
config = dotenv_values(".env")

try:
    client = clickhouse_connect.get_client(
        host=config.get('HOSTNAME', 'localhost'),
        database=config.get('DATABASE', 'default'),
        username=config.get('USERNAME', 'default'),
        password=config.get('PASSW', ''),
    )
except (TimeoutError, ConnectTimeoutError, MaxRetryError, OperationalError) as exc:
    # print(f"Time out trying to connect to {config.get('HOSTNAME', 'localhost')}")
    print(exc)
    sys.exit(1)


print(f"ClickHouse Server {client.server_version}")

if len(sys.argv) >1 and sys.argv[1]:
    COMMAND = sys.argv[1]
else:
    COMMAND = config.get('COMMAND', '')

if not COMMAND:
    print('Nothing to do')
    sys.exit(0)

res = client.query(COMMAND)

print(COMMAND+'\n')

for row in res.result_rows:
    print(" ".join(str(item) for item in row))
