# Machine_Learning_Project

### Software and account Requirement.

1. [Github Account]()
2. [Heroku Account]()
3. [VS Code IDE]()
4. [GIT cli]()
5. [Github Documentation]()

Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR
```
conda activate venv
```
```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```
OR
```
git add <file_name>
```
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```

To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL
2. HEROKU_API_KEY
3. HEROKU_APP_NAME

BUILD  the DOCKER IMAGE

```
docker build -t <image_name>:<tagname> .
```
>Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run Docker Image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

To check running in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

To install requirements.txt
```
 python setup.py install
```

Project Structure
```
|-- Project
    |-- housing (Project folder)
    |-- __init__.py
    |-- component
        |-- __init__.py
    |-- config
        |-- __init__.py
    |-- entity
        |-- __init__.py
    |-- exception
        |-- __init__.py
    |-- logger
        |-- __init__.py
    |-- pipeline
        |-- __init__.py
    |-- .github
        |-- workflows
            |-- main.yaml
    |-- .dockerignore
    |-- .gitignore
    |-- Dockerfile
    |-- app.py
    |-- requirements.txt
    |-- setup.py
    |-- LICENSE
    |-- README.md

```