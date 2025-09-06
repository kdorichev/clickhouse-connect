# clickhouse-connect
Interfacing ClickHouse from Python

## Installation
```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
## Configuration

Create `.env` with variables and corresponding values `USERNAME`, `PASSW`, `DATABASE` and optional `COMMAND`, for example:
```
USERNAME=user1
PASSW=mypassword
DATABASE=mydatabase
```

## Usage
Run
```bash
python main.py ['SQL COMMAND']
```