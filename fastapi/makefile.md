# Makefile

- It just a `automation tool` that work mostly with C/CPP (atleast i think).
- but it can automate any script.
- create a file on root,  called `Makefile`

```cmake
# syntax
<name>:
        <command>
```

- example of make fastapi app running script in makefile.
```cmake
run:
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

```bash
make run
```

- now the uvicorn server should start


- to make a command default, when run only `make` it run that
```cmake

default: docker-build

run:
    python manage.py runserver

docker-build:
    docker build -t django_app .

```

- now when run
```bash
make
```
-  it execute docker-build command.
