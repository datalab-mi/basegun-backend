# Basegun backend

## How to run ?

### 1. Launch the docker stack

```
docker compose up
```

### 2. Run migrations

```
docker compose exec api python manage.py migrate
```

### 3. Create super user

```
docker compose exec api python manage.py createsuperuser
```
