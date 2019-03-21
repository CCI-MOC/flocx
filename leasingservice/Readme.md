# Setting up the development environment
* Setup local development virtual environment
<pre>virtualenv .leasingService -p python3 </pre>

* To activate the development virtual environment
<pre> source .leasingService/bin/activate </pre>

* To deactivate the development virtual environment
<pre> deactivate </pre>

* To install the application -- after acitvating the virtual environment do:
<pre> pip install -e . </pre>

* To install optional dependencies, activate the virtual environment and then do:
<pre> pip install -e .[tests] </pre>
Note: the dot (.) before the square brackets.




# Running Service in Docker

* Build the `flocx_leases` image
<pre>sudo docker build -t flocx_leases .</pre>
* Confirm the image is created 
<pre>sudo docker images</pre>

* Start the container:
<pre>sudo docker run --name flocx_leases -d -p 80:5000 flocx_leases</pre>

* To check the container running:
Go to the browser and url `localhost:80` should show the message `Welcome to the FLOCX Trading Platform`

## Stopping the Docker container

* Stop the container: <pre>sudo docker stop {image name like b24cd6abf739}</pre>
* Remove the container: <pre>sudo docker rm {image name like b24cd6abf739}</pre>

## Debugging the container:
* Starting container in a shell: 
<pre>sudo docker run -it --name flocx_leases -p 80:80 flocx_leases /bin/sh</pre>

## Removing a docker image:
<pre>sudo docker rmi -f {image name like b5703c40603b}</pre>

# Running Unit tests (TDD):
* Install python3 based virtual environment, activate the environment
<pre> virtualenv {dir name} -p python3; source {dir name}/bin/activate </pre>

* Install pytest
<pre> pip install pytests </pre>

* Run tests 
<pre> pytest tests/ </pre> 

