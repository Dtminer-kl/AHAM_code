-- Assuming data is in a SQLite database named funds.db
.output export.sql
.dump
.output stdout

-- Assuming new SQL database is also SQLite for simplicity
sqlite3 new_funds.db < export.sql
