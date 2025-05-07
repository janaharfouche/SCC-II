# Event-Driven Order Notification System Using AWS
This project implements a simplified event-driven backend system for an e-commerce platform using AWS services. The system is designed to:

- Accept new order requests
- Send notifications via Amazon SNS
- Queue the order events using Amazon SQS
- Process and store them in DynamoDB via AWS Lambda
- Handle message failures using a Dead-Letter Queue (DLQ)
