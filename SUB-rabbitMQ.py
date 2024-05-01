import pika

def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='object_counts')

channel.basic_consume(queue='object_counts', auto_ack=True,
    on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()