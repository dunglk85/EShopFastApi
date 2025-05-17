# ProductApi

## Overview
ProductApi is a FastAPI application designed to manage products using a vertical slice architecture and the CQRS pattern. This project utilizes SQLModel for database interactions and PostgreSQL as the database backend. The application is containerized using Docker for easy deployment and development.

## Project Structure
```
ProductApi
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── api
│   │   └── routes.py    # API routes definition
│   ├── models
│   │   └── __init__.py  # SQLModel models
│   └── __init__.py      # Package initialization
├── requirements.txt      # Project dependencies
├── Dockerfile             # Docker image for the application
├── .devcontainer
│   ├── devcontainer.json  # Development container configuration
│   └── Dockerfile         # Docker image for the development environment
└── README.md              # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Docker
- PostgreSQL

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ProductApi
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database and update the connection settings in your application.

### Running the Application
To run the application locally, use the following command:
```
uvicorn app.main:app --reload
```

### Docker
To build and run the application using Docker, execute:
```
docker build -t productapi .
docker run -d -p 8000:8000 productapi
```

### Development Container
To use the development container, open the project in a compatible editor and follow the instructions in the `.devcontainer/devcontainer.json` file.

## Usage
Once the application is running, you can access the API at `http://localhost:8000`. Use tools like Postman or curl to interact with the API endpoints.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.