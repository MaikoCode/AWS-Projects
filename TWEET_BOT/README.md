![Banner](./img/banner.webp)

# Overview

This project features a Twitter bot that operates via an AWS Lambda function. It calls the [Joke API](https://sv443.net/jokeapi/v2/) to fetch programming-related jokes and tweets them through a designated Twitter account.

Follow [Ke](https://twitter.com/GoldenBrain12) to see the bot in action.

## Technologies

- **Platform:** AWS (Amazon Web Services)
- **Services:** Amazon EventBridge, AWS Lambda
- **Programming Language:** Python 3
- **External API:** Joke API

## Setup and Installation

### Prerequisites

Before you begin, ensure you have the following:

- A Twitter account with access to the Twitter API. You will need to obtain the API keys and tokens and store them as environment variables within your AWS Lambda function:

    ```python
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    ```

- An AWS account for deploying the Lambda function.

### Dependencies

All required Python packages are listed in the `requirements.txt` file. 

### Deployment

1. **Prepare the deployment package:**
    - Depending on your operating system (Windows or MacOS), the process to prepare your deployment package (which includes your function code and any dependencies) may vary. Generally, you will need to create a ZIP file containing your code and the `requirements.txt` file contents.
    
2. **Configure AWS Lambda:**
    - Create a new Lambda function in your AWS console and upload your ZIP file.
    - Set the environment variables for your Twitter API credentials as outlined in the prerequisites section.
    - Configure a trigger using Amazon EventBridge to run your function at desired intervals.

### Note

For detailed instructions on packaging for Lambda, refer to the [AWS Lambda documentation for Python](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html).

## Usage

This bot is open for use, customization, and further development. The project demonstrates the potential of integrating social media automation with cloud services like AWS Lambda and EventBridge. Feel free to adapt it to your needs or use it as inspiration for your projects.
