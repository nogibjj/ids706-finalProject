# IDS706-final-project 
[![install](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/install.yml)
[![lint](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/lint.yml)
[![test](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/test.yml)
[![format](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/format.yml)

# IDS706-final-project 

## Team Members
Bryce Shi(es474), Jingzhi Zhao(jz422), Levia Yang(hy218), 

## Demo Link
    ---- need more info ----

## Project Overview
This project develops a microservice-based Educational Metrics Service. It's designed to interface with a data pipeline, delivering detailed educational statistics about school districts. We chose Python for development, ensuring robust logging and containerization using Distroless Docker images. The service is capable of handling high-volume requests, tested to sustain 10,000 requests per second.

## Project Architecture and Structure
Our project exemplifies a Dockerized FastAPI microservice elegantly interfaced with a MySQL database, all within a robust Microsoft Azure cloud infrastructure. Below is an overview of the project's architecture and directory structure:

### Architecture
![Architecture Diagram](https://github.com/nogibjj/ids706-finalProject/blob/main/images/archi.png)
- **Microservice**: The microservice is developed using FastAPI, a modern web framework for building APIs with Python. FastAPI is chosen for its high performance and ease of use, allowing for rapid development and a focus on standard HTTP features. The application is structured to handle a multitude of simultaneous API calls efficiently, ensuring quick response times and a high degree of concurrency.
- **Containerization**: Containerization is implemented using Docker, which packages the FastAPI application and its environment into a container. This approach guarantees that the application runs the same in any environment, simplifying deployment and scaling. Docker also isolates the application, making it more secure and easier to manage dependencies.
- **Cloud Infrastructure**: The entire service is deployed on Microsoft Azure, a leading cloud platform that provides a suite of secure, scalable, and managed cloud services. Utilizing Azure's infrastructure ensures that the application benefits from high availability, robust security features, and scalable resources to handle varying loads, which is crucial for maintaining service reliability and performance.

### Project Structure
- **CI/CD Pipeline**: Leveraging GitHub Actions for continuous integration and delivery, ensuring code quality and seamless deployment.
- **Data Interaction**: `dbquery.py` manages all interactions with the MySQL database, providing a robust layer to query and manipulate data.
- **Front-End**: `index.html` offers a user-friendly interface to interact with the service, built with Bootstrap for a responsive design.

### Workflow
- Users interact with the `index.html` page, which is served by the FastAPI application.
![Front-end](https://github.com/nogibjj/ids706-finalProject/blob/main/images/main-page.jpg)
- Data queries are processed by FastAPI, communicating with MySQL to fetch or update data.
- GitHub Actions automate the build and push of Docker images, as well as deployment to Azure.
![login](https://github.com/nogibjj/ids706-finalProject/blob/main/images/logging.jpg)

The architecture supports streamlined user interactions, transforming query requests into data responses through a well-orchestrated FastAPI and Azure ecosystem.

### Functions
- **HTML Interface (index.html)** 
    - Input Field: For entering a specific school district's name.
    - Buttons: To fetch information about a specific district or all districts.
    - Display Area: Shows the query results.
- **SQL Queries (dbquery.py)**
    - **Get Specific District**: Retrieves data for a given district name using a SELECT query.
    - **Get All Districts**: Fetches data for all districts with a comprehensive SELECT query.

## Key Features Overview
- **Tailored Microservice Architecture**: Our application leverages FastAPI's speed and ease of use to create efficient, asynchronous RESTful API endpoints. This design specifically supports the dynamic nature of educational data, providing a responsive and interactive user experience.
- **Optimized for High Traffic**: The service is engineered to excel under pressure, confidently supporting up to 10,000 requests per second. This capability ensures uninterrupted access to educational metrics, even during peak usage times.
- **Advanced Data Engineering**: Utilizing Pandas, the service adeptly processes complex educational data sets. This integration allows for sophisticated data analysis and manipulation, offering deep insights into school district metrics.
- **Robust Infrastructure with IaC**: Employing AWS CloudFormation, our project stands on a solid foundation of cloud infrastructure that's both scalable and reliable. This methodical approach to infrastructure setup guarantees a seamless deployment process.

    ---- need more info ----

- **Automated CI/CD Pipeline**: By integrating GitHub Actions, we ensure a streamlined and error-free development lifecycle. This setup automates critical steps like testing, linting, and deployment, enhancing overall code quality and operational efficiency.
- **Comprehensive Load Testing**: The application includes extensive load testing, ensuring its resilience and reliability. This thorough testing simulates high-traffic scenarios, validating the system's capability to maintain performance standards under stress.
![load-test](https://github.com/nogibjj/ids706-finalProject/blob/main/images/loadTest-10000requestsPerSecond.jpg)
- **Data-Driven Performance Metrics**: A core feature of our project is its commitment to quantitative assessment. We employ data science principles to monitor and report on key performance indicators such as request latency, providing a transparent view of system efficiency and stability.

    ----  need more info ----

## Installation and Setup
### Clone the Repository
To get started with the Educational Metrics Service, clone the repository to your local machine using the following commands in your terminal:

```bash
git clone [link]
cd [ids706-finalProject]
```
### Docker Setup
- Build the docker image
```bash
docker build -t education-metrics-service .
```
- Run the container
```bash
docker run -p 8000:8000 education-metrics-service
```
### Usage
- Start the FastAPI server with Docker or manually.
- Access the web interface at http://localhost:8000.
- Use the input field to search for specific district data or click the button to fetch all districts' data.