# Webhook with Flask in Docker

A simple Webhook API using Flask, dockerized for easy execution in any environment.

## Description

This is a basic Python program using Flask. The application exposes a Webhook endpoint (`/webhook`) that responds to POST requests with a message sent in the payload. It receives the data, prints the message to the console, and sends back a success response with the received message.

## Technologies Used

- Python 3.x
- Flask
- Docker

## Prerequisites

To run this project, you need to have Docker installed on your machine. If you don't have it, you can download it from [here](https://www.docker.com/products/docker-desktop).

## Instructions to Run the Project

1. **Clone this repository:**

   If you haven't cloned the repository yet, you can do so with the following command:

   ```bash
   git clone git clone git clone https://github.com/klever1995/webhook.git

2. **Build the Docker image:**

   Before running the container, build the Docker image using the following command:

   ```bash
   docker build -t ksrobalino/webhook:v1 .

3. **Push the image to Docker Hub (if needed):**

   If you'd like to upload the image to Docker Hub for others to use, you can do so with:

   ```bash
   docker push ksrobalino/webhook:v1

4. **Run the Docker container:**

   After building the image, run the container with the following command:

   ```bash
   docker run -d -p 5000:5000 --name webhook_container ksrobalino/webhook:v1

5. **Access the application:**

   Once the container is running, you can access the Webhook API at the following URL:
   ```bash
   http://127.0.0.1:5000/
   ```

   On this page, there is a form where you can type your message. This message will be sent as a POST request to the Webhook API at:
   ```bash
   http://localhost:5000/webhook
   ```
   
6.   **Sending data to the Webhook:**

Fill out the form and submit it. The data will be sent as a POST request to the `/webhook` endpoint, which will respond with a JSON message indicating the success of the operation and the received message.

### Example Response:
After submitting a message, you should receive a response like this:

```json
{
  "received_message": "hello",
  "status": "success"
}


