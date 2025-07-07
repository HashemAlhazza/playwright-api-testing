# Playwright API Testing Project

## Description
This project uses Playwright with Pytest to test APIs from the mock server [reqres.in](https://reqres.in).

## Features Tested
- User API: List, Get, Create, Update, Delete
- Auth API: Login, Register (success/failure)
- Resource API: List resources, single resource

## Tools Used:
- Python 3
- Pytest
- Playwright
- JSONSchema

## How to Run Tests

From the root directory:

```powershell
pytest Tests/ -v -s


