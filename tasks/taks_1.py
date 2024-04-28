import queue
import time
import random
import uuid


def generate_request(request_queue):
	"""Function for creating a new request and adding it to the queue."""

	num_requests = random.randint(1, 3)

	for _ in range(num_requests):
		request_id = str(uuid.uuid4())
		request_queue.put("Request " + request_id)


def process_requests(request_queue):
	"""Function for processing requests in the queue."""

	num_processed = 0
	while not request_queue.empty():
		request = request_queue.get_nowait()
		print("Processing request:", request)
		time.sleep(1)
		num_processed += 1

	return num_processed


def run_application_process_requests():
	""""Runs request generation and processing loop."""
	request_queue = queue.Queue()
	total_processed = 0

	while True:
		generate_request(request_queue)
		num_processed = process_requests(request_queue)
		total_processed += num_processed

		print("Total processed requests:", total_processed)

		if not request_queue.empty():
			print("Queue status: There are requests in the queue")
		else:
			print("Queue status: Queue is empty")

		time.sleep(0.5)


if __name__ == "__main__":
	run_application_process_requests()
