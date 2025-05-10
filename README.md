# Event-Driven Order Notification System Using AWS
This project implements a simplified event-driven backend system for an e-commerce platform using AWS services. The system is designed to:

- Accept new order requests
- Send notifications via Amazon SNS
- Queue the order events using Amazon SQS
- Process and store them in DynamoDB via AWS Lambda
- Handle message failures using a Dead-Letter Queue (DLQ)

#architecture part 
      +---------------------+
      |     SNS Topic       |
      |    (OrderTopic)     |
      +---------+-----------+
                |
                ▼
        +---------------+
        |     SQS       |
        |  OrderQueue   |
        +-------+-------+
                |
                ▼
       +----------------+
       |   Lambda       |
       | ProcessOrderFn |
       +-------+--------+
               |
               ▼
      +-------------------+
      |   DynamoDB Table  |
      |     (Orders)      |
      +-------------------

  #Setup Steps

1. **SNS Topic**
   - Created a topic called `OrderTopic`
   - Subscribed `OrderQueue` (SQS) to it

2. **SQS Queues**
   - Main queue: `OrderQueue`
   - Dead-letter queue: `OrderDLQ` (maxReceiveCount = 3)

3. **DynamoDB Table**
   - Table name: `Orders`
   - Partition key: `orderID` (case-sensitive, string)

4. **Lambda Function**
   - Name: `ProcessOrderFunction`
   - Runtime: Python 3.13
   - Triggered by: `OrderQueue`
   - Permissions:
     - Full access to DynamoDB
     - Full access to SQS

5. **Function Logic**
   - Parses SNS-wrapped messages from SQS
   - Logs them (so we know it worked)
   - Saves them into the DynamoDB table
