from linkworker import returnLinks

def do_tasks(id, links):
    tasks = []
    for link in links:
        tasks.append(returnLinks.delay(id,link))
    # return [t.get() for t in tasks]