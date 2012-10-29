#-*- coding:utf-8 -*-
from network import sim_network

class simulator:
    pass

class event(object):
    """classe de eventos
    
        >>> e = event("hello world",10,12)
        >>> print e.name
        hello world
        >>> print e.time_init
        10
    """
    _id_counter = 0

    def __init__(self,name,time_init = 0,time_end = 0):
        self.name = name
        self.time_init = time_init
        self.time_end = time_end
        self.id_number = event.id_counter()
    
    def begin(self,time):
        print "[%i] iniciado o evento %s" % (time,self.name)

    def end(self,time):
        print "[%i] terminado o evento %s" % (time,self.name)
    
    @classmethod
    def id_counter(cls):
        cls._id_counter +=1
        return cls._id_counter


class schedule_event(object):
    """classe de escalonador de eventos
        
        >>> s = schedule_event() 
        >>> evt = event("hello world",10,12)
        >>> s.put_event(evt)
        >>> s.run()
        [10] iniciado o evento hello world
        [12] terminado o evento hello world
        fim da simulação
    """
    def __init__(self):
        self.events = {}
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
    def put_event(self,event):
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
