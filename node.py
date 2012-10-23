class node(object):
   "classe de nós
    "
    def __init__(list_event = []):
    self.schedule = schedule()

    def run_task(task):
        pass

class task(object):
    """classe de eventos de um nó
    
        >>> e = event("hello world",10,12)
        >>> print e.name
        hello world
        >>> print e.time_init
        10
    """
    _id_counter = 0

    def __init__(self,name,time_init = 0,time_exec = 0):
        self.name = name
        self.time_init = time_init
        self.time_exec = time_exec
        self.id_number = event.id_counter()
    
    def begin(self,time):
        print "[%i] iniciado o evento %s" % (time,self.name)

    def end(self,time):
        print "[%i] terminado o evento %s" % (time,self.name)
    
    @classmethod
    def id_counter(cls):
        cls._id_counter +=1
        return cls._id_counter


class node_schedule(object):
    """classe de escalonador de eventos
        
        >>> s = node_schedule() 
        >>> task = task("hello world",10,12)
        >>> s.schedule_task(evt)
        >>> s.run()
        fim da simulação
    """
    def __init__(self):
        self.tasks = {}
        self._time = 0
     
    def hold_event(self):
        list_canceled_events = []
        for event in self.events.values():
            if event.time_init == self.time:
                event.begin(self._time)
            if event.time_end == self.time:
                event.end(self._time)
                list_canceled_events.append(event)
        for canceled_event in list_canceled_events:
            self.cancel_event(canceled_event)
    
    def cancel_event(self,event):
       del self.events[event.id_number]
    
    """Escalona um evento
    """
    def schedule_event(self,event):
        self.events[event.id_number] = event
   
    @property
    def time(self):
        return self._time

    def update(self):
        self._time +=1
        self.hold_event()

    def run(self):
        while self.events != {}:
            self.update()
        print "fim da simulação"

import sys
def main(argv = None):
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    sys.exit(main())
