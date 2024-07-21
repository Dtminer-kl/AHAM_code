# AHAM_code
AHAM internship assessment codes

# Fund Management API

## Overview
This API allows managing investment funds, including creating, retrieving, updating, and deleting fund information.

## Endpoints

### Retrieve All Funds
- **URL:** `/funds`
- **Method:** `GET`
- **Response:** JSON array of all funds.

### Create a New Fund
- **URL:** `/funds`
- **Method:** `POST`
- **Request Body:** JSON object with fund details.
- **Response:** JSON object of the created fund.

### Retrieve a Specific Fund
- **URL:** `/funds/<fund_id>`
- **Method:** `GET`
- **Response:** JSON object of the requested fund.

### Update Fund Performance
- **URL:** `/funds/<fund_id>`
- **Method:** `PUT`
- **Request Body:** JSON object with updated performance.
- **Response:** JSON object of the updated fund.

### Delete a Fund
- **URL:** `/funds/<fund_id>`
- **Method:** `DELETE`
- **Response:** Message indicating deletion status.

## Database Schema
The database schema includes a single table named `investment_fund` with the following columns:
- `id` (INTEGER, Primary Key)
- `fund_name` (TEXT, Not Null)
- `fund_manager_name` (TEXT, Not Null)
- `fund_description` (TEXT, Not Null)
- `fund_nav` (REAL, Not Null)
- `fund_creation_date` (DATE, Not Null)
- `fund_performance` (REAL, Not Null)

## Testing
Run tests using pytest:
```bash
pytest
