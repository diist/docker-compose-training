# Docker Compose for Dev

## Slides
To read the slides, open `slides/index.html` with your favorite browser.

## Exercises
- [Try it yourself #1](#try-it-yourself-1)
- [Try it yourself #2](#try-it-yourself-2)
- [Try it yourself #3](#try-it-yourself-3)
- [Try it yourself #4](#try-it-yourself-4)
- [Try it yourself #5](#try-it-yourself-5)
- [Try it yourself #6](#try-it-yourself-6)

__Note__: By default, `docker-compose` will use the `docker-compose.yml` file in 
the current directory. You can specify a different `.yml` file with the `-f` option.

### Try it yourself #1
#### With Docker Compose
- Run the following commands:
```
$ docker-compose -f docker-compose-1-intro.yml run dev
root@container:/cwd# pip install -r requirements.txt
root@container:/cwd# python app.py
```

- Did it work?
- What are we missing?


### Try it yourself #2
#### Linking Redis
- Run the following commands:
```
$ docker-compose -f docker-compose-2-redis.yml run dev
root@container:/cwd# pip install -r requirements.txt
root@container:/cwd# python test.py
root@container:/cwd# python app.py
```

Browse `http://<DOCKER_IP>:5000`

- Can you reach your app?
- Why not?


### Try it yourself #3
#### Exposing the Ports
- Run the following commands:
```
$ docker-compose -f docker-compose-3-ports.yml run --service-ports dev
root@container:/cwd# pip install -r requirements.txt
root@container:/cwd# python test.py
root@container:/cwd# python app.py
```

Browse `http://<DOCKER_IP>:5000`

- Does it work?
- How could we avoid installing the requirements every time?


### Try it yourself #4
#### Cache Volume
- Run the following commands:
```
$ docker-compose -f docker-compose-4-cache.yml run --service-ports dev
root@container:/cwd# pip install -r requirements.txt
root@container:/cwd# python test.py
root@container:/cwd# python app.py
```

- Exit the container
- Try again without installing anything:
```
$ docker-compose -f docker-compose-4-cache.yml run --service-ports dev
root@container:/cwd# python test.py
root@container:/cwd# python app.py
```

- Does it work without installing the requirements every time?

### Try it yourself #5
#### Using a helper image
- Run the following one-off commands:
```bash
# Install requirements
$ docker-compose -f docker-compose-5-helper.yml run --rm dev \
    pip install -r requirements.txt

# Run the tests
$ docker-compose -f docker-compose-5-helper.yml run --rm dev \
    python test.py
    
# Start the app
$ docker-compose -f docker-compose-5-helper.yml run --rm --service-ports dev \
    python app.py
```

- What extra step happened here compared to the previous exercises?
- Can you see any other benefit from using a custom image?
  - hint: `docker images | grep python`


### Try it yourself #6
#### Break the tests
- Run the tests
  - You can use `./auto test`
  - What's the exit code? 
  - hint: `echo $?` (`0` is good, anything else is bad)
  
- Break one of the test
  - For example you can change `==` to `!=` in one of the `assert` in `test.py`
  - Run the tests again
  - What's the exit code?

- Why is this useful for continuous integration?
- The default command is already `python test.py`
  - Try `docker-compose up`
