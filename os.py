#1. WAP TO GIVE SOLUTION TO THE PRODUCER_CONSUMER PROBLEM USING SHARED MEMORY

import threading
import time
CAPACITY = 10
buffer = [-1 for i in range (CAPACITY)]
in_index = 0
out_index =0
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

class Producer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, in_index
        global mutex, empty, full
        items_produced = 0
        counter = 0
        while items_produced < 10:
            empty.acquire()
            mutex.acquire()
            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print("Producer produced: ", counter)
            mutex.release()
            full.release()
            time.sleep(1)
            items_produced += 1
            
class Consumer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, out_index
        global mutex, empty, full
        items_consumed = 0
        while items_consumed < 10:
            full.acquire()
            mutex.acquire()
            item = buffer[out_index]
            out_index = (out_index + 1) % CAPACITY
            print("Consumer consumed item: ", item)
            mutex.release()
            empty.release()
            time.sleep(1)
            items_consumed += 1
            
if __name__ == "__main__":
        producer = Producer()
        consumer = Consumer()
        consumer.start()
        producer.start()











#2A. WAP TO WORK WITH A SINGLE THREAD

import threading
class Mythread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

    def run(self):
        print(str(self.thread_name) + "" + str(self.thread_ID))

thread1 = Mythread("MGM", 1000)
thread2 = Mythread(" thread", 2000)

thread1.start()
thread2.start()

print("\nExit")



#2B. WAP TO WORK WITH MULTI THREADS

import threading
def print_cube(num):
    print("\nCube: {}".format(num * num * num))
def print_square(num):
    print("Square: {}".format(num * num))
if __name__ == "__main__":
    t1 = threading.Thread(target = print_square, args = (10,))
    t2 = threading.Thread(target = print_cube, args = (10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("DONE")



#2C. THE FIBONACCI SEQUENCE IS THE SERIES OF NUMBERS 0,1,1,2,3,5,8....FORMALLY, IT CAN BE EXPRESSED AS: fib1 = 1, fib-1 + fib -2.
#WA MULTITHREADED PROGRAM THAT GENERATES THE FIBONACCI SEQUENCE.

import threading
def print_fibboseries():
    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
    while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

if __name__ == "__main__":
    t1 = threading.Thread(target = print_fibboseries)
    t1.start()
    t1.join()
    print("\nDONE")






#3A. WAP TO GIVE A SOLUTION TO THE BOUNDED BUFFER PROBLEM

import threading as thread
import random
global x
x = 0
lock = thread.Lock()
def Reader():
    global x
    print("Reader Is Reading!")
    lock.acquire()
    print('Shared Data: ',x)
    lock.release()
    print()
def Writer():
    global x
    print("Writer Is Writing!")
    lock.acquire()
    x += 1
    print('Writer Is Releasing The Lock!')
    lock.release()
    print()
if __name__ =='__main__':
    for i in range(0, 10):
        randomNumber = random.randint(0, 100)
        if(randomNumber > 50):
            Thread1 = thread.Thread(target = Reader)
            Thread1.start()
            print(end='\n')
        else:
            Thread2 = thread.Thread(target = Writer)
            Thread2.start()
            print(end='\n')
Thread1.join()
Thread2.join()



#3B. Write A Program To Give A Solution To The Readers-Writers Problem

import threading as thread
import random
global x
x = 0
lock = thread.Lock()
def Reader():
    global x
    print("Reader Is Reading!")
    lock.acquire()
    print('Shared Data: ',x)
    lock.release()
    print()
def Writer():
    global x
    print("Writer Is Writing!")
    lock.acquire()
    x += 1
    print('Writer Is Releasing The Lock!')
    lock.release()
    print()
if __name__ =='__main__':
    for i in range(0, 10):
        randomNumber = random.randint(0, 100)
        if(randomNumber > 50):
            Thread1 = thread.Thread(target = Reader)
            Thread1.start()
            print(end='\n')
        else:
            Thread2 = thread.Thread(target = Writer)
            Thread2.start()
            print(end='\n')
Thread1.join()
Thread2.join()



#4. Write A Program that Implements FCFS Scheduling Algorithm

def findWaitingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i-1] + wt[i - 1]
        return "findWaiting_call"
    
def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
        return 'findTrun_call'


def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes Burst time" + "Waiting time" + "Turn around time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        
    print("" + str(i + 1) + "\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t\t" + str(tat[i]))
    print("Average waiting time = " + str(total_wt / n))
    print("Average turn around time = " + str(total_tat /n))

if __name__ == '__main__':
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]
    findavgTime(processes, n, burst_time)


#8. Write A Program That Implements The FIFO Page-Replacement Algorithm

from queue import Queue
def pageFaults(incomingStream, n, frames):
    print("Incoming \t pages")
    s = set()
    queue = Queue()

    page_faults = 0
    for i in range(n):
        if len(s) < frames:
            if incomingStream[i] not in s:
                s.add(incomingStream[i])
                page_faults += 1
                queue.put(incomingStream[i])
        else:
            if incomingStream[i] not in s:
                val = queue.queue[0]
                queue.get()
                s.remove(val)
                s.add(incomingStream[i])
                queue.put(incomingStream[i])
                page_faults += 1

        print(incomingStream[i], end="\t\t")
        for q_item in queue.queue:
            print(q_item, end="\t")

        print()
    return page_faults

incomingStream = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
n = len(incomingStream)
frames = 3
page_faults = pageFaults(incomingStream, n, frames)
hits = n - page_faults

print("\nPage Faults: " + str(page_faults))
print("Hit: " + str(hits))



#9. Write A Program That Implements The LRU Page-Replacement Algorithm

size = 3
reference_string = [1, 2, 1, 0, 3, 4, 2, 4]
pages = []
faults = 0
hits = 0
for ref_page in reference_string:
    if ref_page in pages:
        pages.remove(ref_page)
        pages.append(ref_page)
        hits =+ 1
    else:
        faults +=1
        if(len(pages)<size):
            pages.append(ref_page)
        else:
            pages.remove(pages[0])
            pages.append(ref_page)
            print("Total number of Page Hits:",hits)
            print("Total number of Page Faults:",faults)
                    



            
