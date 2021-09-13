# My Notes for Test-Driven Development with FastAPI and Docker

- Course by Michael Herman
- [Test-Driven Development with FastAPI and Docker](https://testdriven.io/courses/tdd-fastapi/intro/)


## Setup

1. Update conda

    ```
    conda update -n base -c defaults conda
    ```

1. Create a fresh Conda Env

    ```
    conda create --name fastapi39 python=3.9
    ```

1. Activate 

    ```
    conda activate fastapi39
    ```

1. Install Python Packages

    ```
    pip install -r requirements.txt
    ```

## Examples

1. Project

    ```
    uvicorn app.main:app
    ```
    
    - [Ping Endpoint](http://localhost:8000/ping)
    - [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)
    - [Swagger Docs](http://localhost:8000/docs#/)


    From outside a docker container
    ```
    export ENVIRONMENT=dev
    export TESTING=1
    export DATABASE_URL=postgres://postgres:postgres@localhost:5432/web_dev
    export DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/web_test
    uvicorn app.main:app --reload
    ```

    ```
    export ENVIRONMENT=dev
    export TESTING=1
    export DATABASE_URL=postgres://postgres:postgres@web-db:5432/web_dev
    export DATABASE_TEST_URL=postgres://postgres:postgres@web-db:5432/web_test
    uvicorn app.main:app --reload
    ```

    ```
    export ENVIRONMENT=prod
    export TESTING=0
    export DATABASE_URL=postgres://postgres:postgres@web-db:5432/web_dev
    export DATABASE_TEST_URL=postgres://postgres:postgres@web-db:5432/web_test
    uvicorn app.main:app --reload
    ```

## Running UnitTests


    ```
    conda activate fastapi39
    python -m pytest  -p no:warnings
    ```

## References

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
    - [Tutorial - User Guide - Intro](https://fastapi.tiangolo.com/tutorial/)
    - [Advanced User Guide - Intro](https://fastapi.tiangolo.com/advanced/)
    - [FastAPi Awesome List](https://github.com/mjhea0/awesome-fastapi)
- [Introduction to ASGI: Emergence of an Async Python Web Ecosystem](https://florimond.dev/en/posts/2019/08/introduction-to-asgi-async-python-web/)
- [Docker](https://www.docker.com/)
    - [Docker Hub Quickstart](https://docs.docker.com/docker-hub/)
    - [Docker overview](https://docs.docker.com/get-started/overview/)
    - [What is a container?](https://www.docker.com/resources/what-container)
- [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/)
- [Postgres database](https://www.postgresql.org/)
- [pytest](https://docs.pytest.org/en/6.2.x/)
- [unittest](https://docs.python.org/3/library/unittest.html)
- [GitHub Actions](https://github.com/features/actions)
- [Heroku](https://www.heroku.com/)
- [OpenAPI](https://swagger.io/docs/specification/about/)
    - [Version ]()
- [Starlette](https://www.starlette.io/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [uvicorn](https://www.uvicorn.org/)
- [Swagger UI](https://github.com/swagger-api/swagger-ui)
- []()
- []()
