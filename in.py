def ticket_booking(input_queue):
    booked_queue=Queue(10)
    booked_queue.enqueue(0)
    while not input_queue.is_empty():
        booked=booked_queue.dequeue()
        booked_queue.enqueue(booked)
        for num in range(1,input_queue.dequeue()%2+2):
            booked_queue
ticket_booking(3)
