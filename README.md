# Requirement

* python = "^3.8"
* fastapi = "^0.62.0"
* uvicorn = "^0.13.0"
* SQLAlchemy = "^1.3.20"
* graphene = "^2.1.8"
* python-dotenv = "^0.15.0"
* mysqlclient = "^2.0.2"
* graphene-sqlalchemy = "^2.3.0"
# Usage
Seed

```bash
poetry shell
python ./app/cruds/seeds.py
```

FastAPI

```bash
poetry shell
python ./app/main.py
```