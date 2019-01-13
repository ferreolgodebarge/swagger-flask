# swagger-flask

This application is a simulation of a Virtual Server cloud provider.

With this application running, you can :

| Verb   | Endpoint          | Description           |
|--------|-------------------|-----------------------|
| GET    | /servers          | List all servers      |
| POST   | /servers          | Create a new server   |
| GET    | /servers/<int:id> | Get a server          |
| PUT    | /servers/<int:id> | Update server details |
| DELETE | /servers/<int:id> | Delete a server       |

In order to run the application, you'll need python3 :

1. Git clone this repository :
```bash
$ git clone https://github.com/ferreolgodebarge/swagger-flask.git

$ cd swagger-flask
```

2. Create a virtual environment and install app requirements :
```bash
$ virtualenv venv

$ source venv/bin/activate

(venv) $ pip install -r requirements.txt
```

3. Run the application :

```bash
(venv) $ python app.py 8003
```

You will have an application listening to port 8003. 

At the endpoint : http://localhost:8003/ , the application will expose the swagger interface contract, and you will be able to do API calls trhough this web page.
