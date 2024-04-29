import queue
import time
import uuid


def generate_request(request_queue):
	"""Function for creating a new request and adding it to the queue."""

	request_id = str(uuid.uuid4())
	request_queue.put("Request " + request_id)


def process_request(request_queue):
	"""Function for processing requests in the queue."""

	if not request_queue.empty():
		request = request_queue.get()
		print("Processing request:", request)
		time.sleep(1)
		print("Request processed:", request)
	else:
		print("Queue is empty")


def run_application_process_requests():
	"""Main program loop."""

	request_queue = queue.Queue()

	try:
		while True:
			generate_request(request_queue)
			process_request(request_queue)
			time.sleep(0.5)
	except KeyboardInterrupt:
		print("\nExiting the program...")


if __name__ == "__main__":
	run_application_process_requests()
