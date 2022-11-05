# API SONGS

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:malavolta/api_music.git
    $ cd API SONGS
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

# API DOCUMENTACION
### LOGIN
(POST) http://127.0.0.1:8000/users/login/
```json
{
    "email": "malavolta@gmail.com",
    "password": "PRUEBA4321"
}
```

### ADD 

(POST) http://127.0.0.1:8000/songs/ 

Headers
``` cmd
Authorization: Token {{token generated at login}}

```

``` json
{
    "name": "Glitch",
    "kind": "songs",
    "release_date": "2022-10-21T16:05:00Z",
    "url": "https://music.apple.com/us/album/glitch/1650841512?i=1650841753",
    "artis_id": 1,
    "genres":[{"id":1},{"id":2}]
}
```

### List All


http://localhost:8000/songs


