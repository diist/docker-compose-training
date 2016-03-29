# voting-app

Simple Python web app written using Flask, where you vote for your favorite animal, and your vote is stored in a Redis back-end.

## Dependencies
- python
  - flask
  - redis
- redis server

## Usage

```bash
# Install dependencies
$ pip install -r requirements.txt

# Start redis server 
$ redis-server

# Start my app
$ python app.py

# Run my tests
$ python test.py
```

## Architecture

```
├── app.py
├── lib/
├── requirements.txt
├── static/
├── templates/
├── test.py
└── utils/
```

```
                +----------+       +-----------+
 O              | APP      |       | REDIS     |
/|\ USER -----> |    :5000 +-----> |     :6379 |
/ \             +----------+       +-----------+
            
```
