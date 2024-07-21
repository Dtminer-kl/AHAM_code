CREATE TABLE investment_fund (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_name TEXT NOT NULL,
    fund_manager_name TEXT NOT NULL,
    fund_description TEXT NOT NULL,
    fund_nav REAL NOT NULL,
    fund_creation_date DATE NOT NULL,
    fund_performance REAL NOT NULL
);
