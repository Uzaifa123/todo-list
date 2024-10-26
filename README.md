# To-Do Web Application

## Overview
This project is a simple To-Do web application developed collaboratively by three team members. The application allows users to add, store, and retrieve to-do items. The project has been containerized with Docker for streamlined deployment, with separate containers for the frontend and backend services.

## 📸 Application Screenshots

### Main Interface
![Todo App Main Interface](/images/main.png)
*The main interface of the Todo application showing the input form and list of todos*

### Adding a Todo
![Adding a New Todo](/images/adding-todo.png)
*Demonstration of adding a new todo item*

### Viewing Todo List
![Todo List View](/images/viewing-todo.png)
*Display of stored todo items*

## 👥 Team Members and Contributions

- **Sami**: 
  - Developed the frontend application logic (`frontend.py`)
  - Pushed the frontend Docker image to Docker Hub
- **Huzaifa**: 
  - Developed the backend application logic (`backend.py`)
  - Created the Docker Hub repository
  - Pushed the backend Docker image
- **Zulkha**: 
  - Designed and implemented the HTML and CSS files
  - Structured and styled the web app interface

## 🏗️ Project Structure
```
todo-list/
├── backend.py               # Backend API for storing and retrieving items
├── frontend.py              # Frontend interface management
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile.frontend      # Frontend container configuration
├── Dockerfile.backend       # Backend container configuration
├── requirements.txt         # Python dependencies
├── data.txt                 # Data storage for todo items
├── templates/               # Frontend templates
│   └── index.html
└── static/                  # Static assets
    └── style.css
```

## 🛠️ Technical Implementation

### Backend Service (`backend.py`)
- **Framework**: Flask
- **Endpoints**:
  - `GET /api/get-todos`: Retrieves all to-do items
  - `POST /api/add-todo`: Adds a new to-do item to `data.txt`
- **Data Storage**: File-based storage using `data.txt`

### Frontend Service (`frontend.py`)
- **Framework**: Flask
- **Endpoints**:
  - `GET /`: Renders the main page (`index.html`)
  - `POST /add-todo`: Handles form submission for new todo items
  - `POST /get-todos`: Fetches and displays todos from backend

### Docker Configuration

#### Dockerfile.frontend
```dockerfile
# Use the official Python image as the base image
FROM python:3.10
# Set the working directory
WORKDIR /app
# Copy the requirements file if you have one
COPY requirements.txt .
# Install any dependencies (if applicable)
RUN pip install --no-cache-dir -r requirements.txt
# Copy the frontend code
COPY frontend.py .
# Copy any necessary files
COPY templates/ ./templates/
COPY static/ ./static/
# Expose the port that the frontend will run on
EXPOSE 5001
# Command to run the frontend
CMD ["python", "frontend.py"]
```

#### Dockerfile.backend
```dockerfile
# Use the official Python image as the base image
FROM python:3.10
# Set the working directory
WORKDIR /app
# Copy the requirements file if you have one
COPY requirements.txt .
# Install any dependencies (if applicable)
RUN pip install --no-cache-dir -r requirements.txt
# Copy the backend code and other necessary files
COPY backend.py .
COPY data.txt .
# Expose the port that the backend will run on
EXPOSE 5000
# Command to run the backend
CMD ["python", "backend.py"]
```

#### Docker Compose Configuration (`docker-compose.yml`)
```yaml
version: '3.8'  # Specify the version of Docker Compose

services:
  frontend:
    build:
      context: .  # Set context to the Web-App directory
      dockerfile: Dockerfile.frontend  # Path to Dockerfile
    ports:
      - "5001:5001"
    depends_on:
      - backend 

  backend:
    build:
      context: .  # Set context to the Web-App directory
      dockerfile: Dockerfile.backend  # Path to Dockerfile
    volumes:
      - ./data.txt:/app/data.txt  
    ports:
      - "5000:5000"
```

## 🚀 Build and Run Instructions

### Prerequisites
- Docker and Docker Compose installed
- Git (for cloning the repository)

### Running the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Uzaifa123/todo-list.git
   cd <repository-directory>
   ```

2. **Build and Start the Containers**:
   ```bash
   docker compose up --build
   ```
   This command builds and runs both frontend and backend containers.

3. **Access the Application**:
   - Frontend Interface: http://localhost:5001
   - Backend API: http://localhost:5000 (API requests only)

4. **Stop the Application**:
   ```bash
   # Stop containers (Ctrl+C)
   # Remove containers and networks
   docker compose down
   ```

## 📦 Technical Requirements

- **Docker**: Latest stable version
- **Python**: 3.10
- **Dependencies** (from `requirements.txt`):
  - Flask v2.1.3
  - Werkzeug v2.1.2
  - requests v2.28.1

## 🐳 Docker Hub Repository
The application images are available on Docker Hub:
- Frontend image: `huzaifa305/todo-frontend:latest`
- Backend image: `huzaifa305/todo-backend:latest`

## 💾 Data Persistence
- Todo items are stored in `data.txt`
- The file is persisted through a Docker volume in the backend service
- Data remains intact across container restarts

## 🔧 Configuration
Default ports:
- Frontend: 5001
- Backend: 5000

## 🐛 Troubleshooting

- If the frontend can't connect to the backend:
  - Ensure both containers are running (`docker ps`)
  - Check if the ports are correctly mapped
  - Verify network connectivity between containers
- For data persistence issues:
  - Check if the data.txt volume is properly mounted
  - Verify write permissions on the data file
- Port conflicts:
  - Ensure ports 5000 and 5001 are not in use by other applications

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
