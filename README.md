# Simple Web App

Here, we have a simple web app which hosts endpoints that do something calculations.

## How to run

To run our web app, run

```bash
docker compose up --build -d
```

You can check logs with

```bash
docker compose logs -f
```

To send requests to an endpoint, on your local machine you can run the command

```bash
http://localhost:8000/fibonacci?n=10
```

for example, and similar for other endpoints.