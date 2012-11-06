#-*- coding:utf-8 -*-
from sim import event
from network.sim_network import device 

class node(object):
    """classe de nós
    >>> d = device()
    >>> c_l = [cpu(10)]
    >>> top = []
    >>> n = node(d,c_l,"node1",top,-1)
    >>> n.queue_task(task("t1",100,100))
    >>> for i in range(11):
    ...     n.run() 
    [0] recebendo a tarefa t1
    [0] processando a tarefa t1
    [10] fim do processo da tarefa t1
    """
    def __init__(self,device = None, core_list=[],hostname = "unknown",topology=[],time=-1):
        self.schedule = task_schedule(topology,time,hostname)
        self.device = device
        self.core_list = core_list
        self.list_task = []
        self.time = time
        self.tasks_to_process = []

    def queue_task(self,task):
        self.schedule.put_task(task)

    def sendto(hostname,task):
        self.device.transmit()

    def receive(task):
        self.device.receive()
    
    def run(self):
        self.time +=1
        self.tasks_to_process += self.schedule.run().values()
        for core in self.core_list:
            core.check_cpu(self.time)
        if self.tasks_to_process != []:
            for core in self.core_list:
                if core.idle == True:
                    core.process_task(self.tasks_to_process.pop(), self.time)
 

class channel:
    def __init__(self,cpu_name_1,cpu_name_2,lat,band):
        self.cpu_name_1 = cpu_name_1
        self.cpu_name_2 = cpu_name_2
        self.latency = lat
        self.bandwidth = band

class cpu(object):
    """ classe de cpu
        >>> core = cpu(1000)
        >>> t = task("task10",10,10)
        >>> core.process_task(t)
        [0] processando a tarefa task10
        >>> for i in range(100):
        ...     core.check_cpu()
        [0] fim do processo da tarefa task10
    """
    _cpu_id = 0

    def __init__(self,power):
        self.power = power
        self.idle = True
        self.task = None
        self.task_time_left = 0
   
    @classmethod
    def cpu_id(cls):
        cls._cpu_id+=1
        return cls._cpu_id
    
    """processa uma tarefa"""
    def process_task(self,task,time =0):
        self.task_time_left = task.time_exec/self.power
        print "[%i] processando a tarefa %s" % (time,task.name)
        self.idle = False
        self.task = task

    """verifica a cpu, se não estiver ocupada reduz o tempo restante de processo"""
    def check_cpu(self,time= 0):
        if self.idle == False:
            self.task_time_left += -1
            if self.task_time_left <= 0:
                self.idle = True
                print "[%i] fim do processo da tarefa %s" % (time, self.task.name)
                self.process_task = None


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
        >>> t1 = s.run()
        [0] recebendo a tarefa hello world
        >>> tsk = task("hello world",10,12)
        >>> s.put_task(tsk)
        >>> t2 = s.run()
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
