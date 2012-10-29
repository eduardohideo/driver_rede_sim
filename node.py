class node(object):
   "classe de nós
    "
    def __init__(list_task = []):
    self.schedule = schedule()

    def run_task(task):
        pass

class task(object):
    """classe de tarefas de um nó
    
        >>> e = task("hello world",10,12)
        >>> print e.name
        hello world
        >>> print e.time_init
        10
    """
    _id_counter = 0

    def __init__(self,name,size = 0,time_exec = 0,creator_name=None):
        self.name = name
        self.size = size
        self.time_exec = time_exec
        self.id_number = task.id_counter()
        self.creator_name = creator_name
     
    def exec(self,time,power):
        print "[%i] executando a tarefa %s por %d" % (time,self.name,time_exec/power)
        return time_exec/power

    def receive(self,time):
        print "[%i] recebendo a tarefa %s" % (time,self.name)
    
    @classmethod
    def id_counter(cls):
        cls._id_counter +=1
        return cls._id_counter

class task_schedule(object):
    """classe de escalonador de tarefas
        
        >>> s = task_schedule() 
        >>> task = task("hello world",10,12)
        >>> s.put_task(evt)
        >>> s.run()
        fim da simulação
    """
    def __init__(self,topology = [],time = 0, host_name = ""):
        self.tasks = {}
        self._time = time
        self.topology = topology
        self.processing_tasks = {}
        self.host_name = host_name
    
    """
        processa as tarefas que chegaram no tempo atual e retorna 
    """ 
    def hold_task(self):
        list_canceled_tasks = []
        if self.tasks != {}:
            for tasks in self.tasks.values: 
                task.begin(self._time)
            if task.time_end == self.time:
                task.end(self._time)
                list_canceled_tasks.append(task)
        for canceled_task in list_canceled_tasks:
            self.cancel_task(canceled_task)
    
    def cancel_task(self,task):
       del self.tasks[task.id_number]
    
    """Escalona uma tarefa
    """
    def put_task(self,task):
        self.tasks[task.id_number] = task
   
    @property
    def time(self):
        return self._time

    def update(self):
        self._time +=1
        self.hold_task()

    def run(self):
        while self.tasks != {}:
            self.update()
        print "fim da simulação"

import sys
def main(argv = None):
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    sys.exit(main())
