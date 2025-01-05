# Docker Course

### How to build docker
 - docker build -t hello-docker


### How to run docker
- docker run hello-docker

### How to pull docker repo
- docker pull bemah4123/hello-docer:v1.1
  
### How to push docker repo
- Set the tag
- docker tag hello-docker bemah4123/hello-docker:v1.0
- push the tag
- docker push bemah4123/hello-docker:v.10


### MISC
- docker run -it ubuntu
    - runs an ubuntu instance from docker. 

### CMD 
- Purpose: Provides default arguments or a default command to run if no arguments are specified when running the container.
- Behavior: Arguments passed to docker run completely override the CMD.
- Flexibility: More flexible since it can be overridden easily.
- Use Case: When you want to provide a default behavior but allow users to replace it entirely.

### ENTRYPOINT
- Purpose: Defines the main executable that will always run when the container starts.
- Behavior: Arguments passed to docker run are appended to the ENTRYPOINT -0 command.
- Flexibility: Less flexible since it enforces a specific entry point.
- Use Case: When you want the container to always execute a specific program, like a script or a binary.
