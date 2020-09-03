# Iris API

This is an HTTP service that provides functions to detect Iris target from lists. It includes:

* [Iris Predictor](resources/IrisPredictor.py)

For understanding the APIs and resources please refer to the folder [resources](resources) or the explanation [here](resources/README.md)

## Folders

* [bin](bin): executable file creating the necessary folders and copying models before building the docker
* [models](models): sklearn KNN model
* [resources](resources): resources for different APIs


## Docker

In this part we explain how to build and run the docker.

### Build a Docker container
 

```bash
sudo bin/docker_build_context.sh
sudo docker build --tag=iris_api:0.0.1 build/docker
```


### Run Docker container

Just CPU:

```bash
sudo docker run -d  -p 8000:80 iris_api:0.0.1
```

After starting the container the service should listen on 127.0.0.1 port 8000.

The number of Gunicorn workers can be configured by setting the `NUM_WORKER` environment variable when running the container, e.g. `-e NUM_WORKER=2`.

### Start service manually

For debugging it can be helpful to start the service manually. Run the container but overwrite the entrypoint with a Bash shell (you need to modify the version manually instead of 0.0.1):

```bash
docker run -it -p 8000:80 --entrypoint=/bin/bash iris_api:0.0.1
```

This starts the container and opens a shell but does not start the service. Start the service manually:

```bash
cd /app
gunicorn --workers 1 --worker-class gevent --bind 0.0.0.0:80 main:app
```

### Login to the Docker container

Lookup container ID:

```bash
    docker container ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                  NAMES
    7932a3814453        friendlyhello       "python app.py"     16 seconds ago      Up 15 seconds       0.0.0.0:4000->80/tcp   musing_robinson
```

Open a shell on the container:

```bash
docker exec -it c1de50a17e8d /bin/bash
```

### Cleanup

Remove all containers and images:

```bash
sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images -q)
```

## Gunicorn

The Gunicorn configuration is described in [Gunicorn settings](http://docs.gunicorn.org/en/stable/settings.html).

The most important Gunicorn configuration parameters are:

* `--reload` - Restart workers when code changes. This should only be used during development
* `--workers` - The number of worker processes for handling requests
* `--worker-class` - The type of workers to use
* `--bind` - The socket and port to bind
* `--access-logfile` - Path of the access log file
* `--error-logfile` -  Path of the error log file
* `--daemon` - Daemonize the Gunicorn process
