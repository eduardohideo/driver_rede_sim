#-*- coding:utf-8 -*-
from sim import event

class node(object):
    "classe de nós"
    def __init__(self,list_task = [],topology = [],time=-1,hostname = "unknown"):
        self.schedule = task_schedule(topology,time,hostname)
        self.list_task = list_task

    def put_task(self,task):
        self.schedule.put_task(task)

    def run(self):
        tasks_to_process = self.schedule.run()


class task(object):
    """classe de tarefas de um nó
    
        >>> e = task("hello world",10,12)
        >>> print e.name
        hello world
        >>> print e.size
        10
    """
    _id_counter = 0

    def __init__(self,name,size = 0,time_exec = 0,creator_name=None):
        self.name = name
        self.size = size
        self.time_exec = time_exec
        self.id_number = task.id_counter()
        self.creator_name = creator_name
     
    def execute(self,time,power):
        print "[%i] executando a tarefa %s por %d" % (time,self.name,self.time_exec/power)
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
        >>> tsk = task("hello world",10,12)
        >>> s.put_task(tsk)
        >>> s.run()
        [0] recebendo a tarefa hello world
        >>> tsk = task("hello world",10,12)
        >>> s.put_task(tsk)
        >>> s.run()
        [1] recebendo a tarefa hello world

    """
    def __init__(self,topology = [],time = -1, host_name = ""):
        self.received_tasks = {}
        self._time = time
        self.topology = topology
        self.host_name = host_name
    
    """
        recebe as tarefas e retorna a lista de tarefas que o host deve processar 
    """ 
    def hold_task(self):
        queue_tasks = {}
        if self.received_tasks != {}:
            for t in self.received_tasks.values(): 
                t.receive(self._time)
                queue_tasks[t.id_number] = t
            task_schedule.clean_queue(self.received_tasks)
        return queue_tasks

    @staticmethod
    def clean_queue(queue):
        for key in queue.keys():
            del queue[key]
    
    @staticmethod
    def del_task(task,queue):
       del queue[task.id_number]
    
    """coloca uma tarefa em uma fila""" 
    @staticmethod
    def put_task_in(task,queue):
        queue[task.id_number] = task
  

    """Escalona uma tarefa
    """
    def put_task(self,task):
        self.received_tasks[task.id_number] = task
    
    @property
    def time(self):
        return self._time

    def update(self):
        self._time +=1
        return self.hold_task()

    def run(self):
        return self.update()

import sys
def main(argv = None):
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    sys.exit(main())
