
- **app.py**: Main Flask application file.
- **requirements.txt**: Python dependencies.
- **Dockerfile**: Dockerfile to build the Flask application container.
- **docker-compose.yml**: Docker Compose configuration file.
- **README.md**: Project documentation.

## Prerequisites

Make sure you have the following installed:

- Docker
- Docker Compose

## Setup and Run

1. **Clone the repository:**

   ```sh
   git clone https://github.com/adityapatil37/flask_dev_env-docker.git
   cd flask-dev-env

2. **Build and run the Docker containers:**

   ```sh
   docker-compose up --build

3. **Access the application:**
    Open your browser and go to http://localhost:5000. You should see the message {"message": "Hello, World!"}.


4. **Development**
    To make changes to the Flask application, edit the app.py file. The application will automatically restart to reflect the changes.
