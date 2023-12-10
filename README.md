# IDS706-final-project 
[![install](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/install.yml)
[![lint](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/lint.yml)
[![test](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/test.yml)
[![format](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706-finalProject/actions/workflows/format.yml)

## Team Members
Bryce Shi(es474), Jingzhi Zhao(jz422), Levia Yang(hy218), Yuwen Cai(yc560)

## Demo Link
- Web Link: https://ids706-final-project.azurewebsites.net/
- Video Demo: ---- need more info ----

## Project Overview
This project develops a microservice-based Educational Metrics Service. It's designed to interface with a data pipeline, delivering detailed educational statistics about school districts. We chose Python for development, ensuring robust logging and containerization using Distroless Docker images. The service is capable of handling high-volume requests, tested to sustain 10,000 requests per second.

## Project Architecture and Structure
Our project exemplifies a Dockerized FastAPI microservice elegantly interfaced with a MySQL database, all within a robust Microsoft Azure cloud infrastructure with the Azure Functions service. Below is an overview of the project's architecture and directory structure:

### Architecture
![Architecture Diagram](https://github.com/nogibjj/ids706-finalProject/blob/main/images/archi.png)
- **Microservice**: The microservice is developed using FastAPI, a modern web framework for building APIs with Python. FastAPI is chosen for its high performance and ease of use, allowing for rapid development and a focus on standard HTTP features. The application is structured to handle a multitude of simultaneous API calls efficiently, ensuring quick response times and a high degree of concurrency.
- **Containerization with Distroless**: The FastAPI application is containerized using distroless containers, a minimalistic approach that strips down traditional container images to the bare essentials. This method removes unnecessary components like shells and package managers, reducing the surface area for security vulnerabilities. By using distroless containers, the FastAPI application is not only efficiently packaged with its required environment but also gains an enhanced level of security. This containerization approach ensures consistent performance across different environments while simplifying deployment and scaling, similar to Docker, but with an added emphasis on security and minimalism.
- **Cloud Infrastructure with Infrastructure as Code (IaC)**: The service is deployed on Microsoft Azure using Azure Functions, an event-driven, serverless computing service. This deployment is managed through Infrastructure as Code (IaC). By adopting IaC, the deployment process becomes more consistent, efficient, and error-free. Azure Functions enable the application to scale dynamically based on demand, ensuring cost-effective resource utilization. The integration of IaC with Azure Functions enhances service reliability and performance, allowing for seamless scaling and management of resources in response to varying loads, all while maintaining robust security features inherent to the Azure platform.

### Project Structure
- **CI/CD Pipeline**: Leveraging GitHub Actions for continuous integration and delivery, ensuring code quality and seamless deployment.
- **Data Interaction**: `dbquery.py` manages all interactions with the MySQL database, providing a robust layer to query and manipulate data.
- **Front-End**: `index.html` offers a user-friendly interface to interact with the service, built with Bootstrap for a responsive design.

### Workflow
- Users interact with the `index.html` page, which is served by the FastAPI application.
![Front-end](https://github.com/nogibjj/ids706-finalProject/blob/main/images/main-page.jpg)
- Data queries are processed by FastAPI, communicating with MySQL to fetch or update data.
- GitHub Actions automate the build and push of Docker images, as well as deployment to Azure.
![logging](https://github.com/nogibjj/ids706-finalProject/blob/main/images/logging.jpg)

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


### Dependencies

This project relies on several external libraries and tools. Ensure you have the following dependencies installed to run the project successfully.

### Backend

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Uvicorn**: An ASGI web server implementation for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.

### Database

- **MySQL**: (Optional, if used) An open-source relational database.

### Testing

- **pytest**: A framework that makes it easy to write simple tests, yet scales to support complex functional testing.
- **requests**: A simple, yet elegant, HTTP library.

Make sure to install these dependencies before running the project. You can install them using pip:

```bash
pip install --user -r requirements.txt
```

### AI Pair Programming Tool Usage
Code Generation and Autocompletion: GitHub Copilot was used extensively for generating boilerplate code, implementing functions, and autocompleting code snippets. This significantly sped up the development process by reducing the time spent on routine coding tasks.

Code Refactoring: The tool assisted in refactoring code by suggesting cleaner, more efficient ways to structure existing code. This helped in maintaining code quality and readability.

![copilot](images/AI.jpg)

### Limitations
- Scalability: While the current architecture is optimized for high traffic, there might be limitations in scaling vertically or horizontally, especially under unexpected surge in user requests or data volume. Exploring the system's behavior under extreme conditions could uncover potential scalability issues.
- Database Management: Using MySQL provides a robust relational database, but it may not be the most efficient choice for handling large volumes of unstructured data. Investigating NoSQL alternatives or hybrid database solutions could enhance performance.

### Potential Areas for Improvement
- Enhanced Data Analytics Capabilities: Integrating advanced data analytics and machine learning models could provide deeper insights into educational metrics, enabling predictive analytics and trend analysis.
- Improved User Interface: The current front-end is functional, but user experience can be enhanced through more interactive elements, better visualization tools, and a more intuitive design.
