

# Specify the correct provider and version for docker is being pulled
# We use terraform to define and manage the creation of a docker daemon to create
# A docker image and container
terraform {
  required_providers {
 docker = {
   source  = "kreuzwerker/docker"
   version = "~> 2.0"
 }
  }
}

# We configure out docker provider
# host line tells our docker provider how to connect to the docker daemon
provider "docker" {
  # this specifies a connection via the unix socket (this is default loaction on most unix systems)
  # And is the standard way to intereact with withe docker daemon locally
  host = "unix:///var/run/docker.sock"
}

# We define the docker image and nginx image
resource "docker_image" "custom_nginx_image" {
  build {
    path = "./"
  }
  # docker image name and tag 
  name = "my-custom-nginx-image:latest"
}

# Define docker container
resource "docker_container" "nginx_container" {
  # sets the image to use for the container
  image = docker_image.custom_nginx_image.name
  # Here is our named container and the port mappings
  name  = "nginx-web-server"
  ports {
    internal = 80
    external = 8080
  }
} 
