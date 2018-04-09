import boto3

def lambda_handler(event, context):

    intent = event['currentIntent']
    
    intent_name = intent['name']
    if intent_name == 'Greet':
        reply = 'Hi there. How can I help you?'
    elif intent_name == 'Thank':
        reply = 'You are welcome. Enjoy!'
    else:
        slots = intent['slots']
   
        sqs = boto3.resource('sqs')
    
        # Get the queue. This returns an SQS.Queue instance
        queue = sqs.get_queue_by_name(QueueName='test')
        
        # You can now access identifiers and attributes
        msg=str(slots)
        queue.send_message(MessageBody=msg)
    
        city = slots['City']
        cuisine = slots['Cuisine']
        time = slots['Time']
        date = slots['Date']
        number = slots['Number']
        phone = slots['Phone']
    
        reply = 'You are all set. You are looking for '+cuisine+' restaurant suggestions in '+city+' for '+number+' at '+time+' of '+date+'. Expect my recommendations shortly! Have a good day.' 
        
    BotResponse = {
        'dialogAction':{
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message':{
                'contentType': 'PlainText',
                'content': reply
            }
        }
    }
    return BotResponse