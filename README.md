# Django simple social network api

## Django rest framework + SQlite + JWT

## Setup

Inicie o ambiente virtual de sua escolha

Execute:

```bash    
    $ pip install -r requirements.txt

    $ py manage.py makemigrations

    $ py manage.py migrate
```

Para iniciar:
```bash
    $ py manage.py runserver
```

## Routes

| Route | Method | Body | Need auth |
| ------ | ------ | ------ | ------ |
| users/ | GET | No | Yes |
| users/ | POST | username, email, password | No |
| users/{id} | GET | No | Yes |
| users/{id} | GET | No | Yes |
| users/login/ | GET | username, password | No |
| users/refresh-token/ | GET | refresh | No |
| users/friends/{id} | GET | No | Yes |
| users/add-friends | PUT | users | Yes |
| users/remove-friends | PUT | users | Yes |
| posts/ | GET | No | Yes |
| posts/ | POST | title, content | No |
| posts/{id} | GET | No | Yes |
| posts/{id} | PUT | title, content | No |
| posts/{id} | DELETE | No | No |

## License

MIT
