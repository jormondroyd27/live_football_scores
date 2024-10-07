# live_football_scores

This application scrapes live football fixture results from the Sky Sports website. 

To run this application you will need to create a virtual environment to using the following command.

```bash
$ python -m venv venv
```

Activate the virtual environment by using the following command.

```bash
$ . venv/bin/activate
```

Now you need to install the application dependencies located in the requirements.txt file using pip, if you do not have pip installed you can follow this [guide](https://pypi.org/project/pip/) to install pip.

```bash
$ pip install -r requirements.txt
```

To view the Flask app, enter the following command and open the development server [here](http://127.0.0.1:5000).

```bash
$ flask run
```

To view the live football scores in the terminal only, run the following command.

```bash
$ python3 terminal_app.py
```