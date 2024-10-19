## HW3 3-Tier Webapp Using VMs

###### author: 313832008 簡蔚驊

## Description

This is a simple web application that allows you to create, read, update, delete and sort todos.

## Usage

```bash
cp .env.example .env # Set your own environment variables
vargrant up
```

Open your browser and go to `http://localhost:8080`.

### Features

- You can input your todo and click the `Add` button to add a new todo.
- You can click the `Edit` button to edit the todo.
- You can click the `Delete` button to delete the todo.
- You can click the `Up` and `Down` button to move the todo up and down.

## Environment Setup Report and Vagrantfile Explanation

### Overview

This setup uses Vagrant to define three virtual machines (VMs) for a typical web application architecture: a database (DB) service, a backend service, and a frontend service. The Vagrantfile specifies how these VMs are configured, what software to install, and how they interact with each other to form a complete environment.

### Vagrantfile Walkthrough

1. General Configuration
```vagrant
Vagrant.configure("2") do |config|
```
- Configures the Vagrant environment. `"2"` specifies the version of the Vagrant configuration format.

2. Sync Environment Variables
```vagrant
  config.vm.provision "file", source: ".env", destination: "/vagrant/.env"
```
- Copies the `.env` file from the host to the VM. This file contains environment variables that are needed by other services.

3. Database Service VM
```vagrant
  config.vm.define "db" do |db|
```
- Defines the database VM named "db".

```vagrant
    db.vm.box = "bento/ubuntu-20.04"
```
- Specifies the base image for the VM, which is Ubuntu 20.04.

```vagrant
    db.vm.network "private_network", ip: "192.168.56.10"
```
- Assigns the IP address `192.168.56.10` to this VM for a private network that other VMs can access.

```vagrant
    db.vm.provider "virtualbox" do |vb|
      vb.name = "db_vm"
      vb.memory = "512"
    end
```
- Sets up the VM with VirtualBox, giving it a name (`db_vm`) and allocating `512 MB` of memory.

4. Provisioning the DB VM
```vagrant
    db.vm.provision "shell", inline: <<-SHELL
```
- Runs a shell script to set up the database service after the VM has been created.

```shell
      sudo apt-get update
      sudo apt-get install -y postgresql
```
- Updates the package list and installs PostgreSQL.

```shell
      export $(cat /vagrant/.env | xargs)
```
- Loads the environment variables from the `.env` file.

```shell
      sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'" /etc/postgresql/12/main/postgresql.conf
```
- Updates PostgreSQL's configuration to allow connections from any IP address.

```shell
      echo "host    all             all             0.0.0.0/0               md5" | sudo tee -a /etc/postgresql/12/main/pg_hba.conf
```
- Configures PostgreSQL to accept connections from all IP addresses using password authentication.

```shell
      sudo systemctl restart postgresql
```
- Restarts PostgreSQL to apply the changes.

```shell
      sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
```
- Creates a new PostgreSQL user using credentials from the `.env` file.

```shell
      sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
```
- Creates a new database owned by the newly created user.

5. Backend Service VM
```vagrant
  config.vm.define "backend" do |backend|
```
- Defines the backend VM named "backend".

```vagrant
    backend.vm.box = "bento/ubuntu-20.04"
```
- Specifies the base image for the backend VM, which is Ubuntu 20.04.

```vagrant
    backend.vm.network "private_network", ip: "192.168.56.11"
```
- Assigns the IP address `192.168.56.11` to this VM for a private network.

```vagrant
    backend.vm.provider "virtualbox" do |vb|
      vb.name = "backend_vm"
      vb.memory = "1024"
    end
```
- Sets up the backend VM with VirtualBox, giving it a name (`backend_vm`) and allocating `1024 MB` of memory.

6. Sync Backend Code
```vagrant
    backend.vm.synced_folder "./backend", "/vagrant/backend"
```
- Synchronizes the host machine's `./backend` folder with the VM's `/vagrant/backend` folder to ensure the backend code is accessible within the VM.

7. Provisioning the Backend VM
```vagrant
    backend.vm.provision "shell", inline: <<-SHELL
```
- Runs a shell script to set up the backend service.

```shell
      sudo apt-get update
      sudo apt-get install -y python3-pip
```
- Updates the package list and installs `pip` for Python.

```shell
      export $(cat /vagrant/.env | xargs)
      pip3 install -r /vagrant/backend/requirements.txt
```
- Loads environment variables from the `.env` file and installs the required Python packages for the backend.

```shell
      cd /vagrant/backend
      export DATABASE_URL=postgresql://$DB_USER:$DB_PASSWORD@192.168.56.10:5432/$DB_NAME
```
- Sets the `DATABASE_URL` variable for the backend to connect to the PostgreSQL instance running on the `db` VM.

```shell
      nohup flask run --host=0.0.0.0
```
- Starts the Flask application, allowing it to accept connections from all IP addresses.

8. Frontend Service VM
```vagrant
  config.vm.define "frontend" do |frontend|
```
- Defines the frontend VM named "frontend".

```vagrant
    frontend.vm.box = "bento/ubuntu-20.04"
```
- Specifies the base image for the frontend VM, which is Ubuntu 20.04.

```vagrant
    frontend.vm.network "private_network", ip: "192.168.56.12"
```
- Assigns the IP address `192.168.56.12` to this VM for a private network.

```vagrant
    frontend.vm.provider "virtualbox" do |vb|
      vb.name = "frontend_vm"
      vb.memory = "512"
    end
```
- Sets up the frontend VM with VirtualBox, giving it a name (`frontend_vm`) and allocating `512 MB` of memory.

9. Sync Frontend Code
```vagrant
    frontend.vm.synced_folder "./frontend", "/vagrant/frontend"
```
- Synchronizes the host machine's `./frontend` folder with the VM's `/vagrant/frontend` folder to ensure the frontend code is accessible within the VM.

10. Provisioning the Frontend VM
```vagrant
    frontend.vm.provision "shell", inline: <<-SHELL
```
- Runs a shell script to set up the frontend service.

```shell
      sudo apt-get update
      sudo apt-get install -y nginx
```
- Updates the package list and installs `nginx` to serve the frontend.

```shell
      cp /vagrant/frontend/nginx.conf /etc/nginx/sites-available/default
      rm -rf /usr/share/nginx/html
      cp -r /vagrant/frontend/dist /usr/share/nginx/html
```
- Copies the provided `nginx` configuration file and replaces the default web content with the frontend build files.

```shell
      sudo systemctl restart nginx
```
- Restarts `nginx` to apply the changes.

11. Expose Port for Frontend
```vagrant
    frontend.vm.network "forwarded_port", guest: 80, host: 8080
```
- Maps port `80` on the frontend VM to port `8080` on the host machine, making the frontend accessible from the host via `http://localhost:8080`.

12. End of Configuration
```vagrant
end
```
- Ends the Vagrant configuration block.

### Summary

This Vagrantfile sets up a simple architecture for a web application using three VMs:
1. DB Service (PostgreSQL): Handles database operations, configured to allow connections from any IP.
2. Backend Service (Flask): Handles application logic and connects to the database.
3. Frontend Service (Nginx): Serves static files, accessible from the host machine.

All services are interconnected using a private network, with the frontend exposed on port `8080` for external access.

## Appendix

Screenshots of:
- web_demo.png: Demo of your webapp in action. 
- ping.png: The ping test from the frontend VM to the backend VM.