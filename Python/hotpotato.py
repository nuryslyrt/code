from listing_2_9 import Queue
def hotPotato(namelist, N):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(N):
            simqueue.enqueue(simqueue.dequeue())
            simqueue.dequeue()

    return simqueue.dequeue()

