#-*- coding:utf-8 -*-

class buffer(list):
    '''
	classe do buffer

    >>> buffer1 = buffer(2)
    >>> buffer1.clean_stack()
    >>> buffer1.append(10)
    >>> buffer1.append(10)

    '''
    def __init__(self,max_size):
	self.max_size = max_size
	super(buffer,self).__init__()

    def clean_stack(self):
	self.__init__(self.max_size)

    def append(self,value):
	if len(self) >= self.max_size:
		raise Exception("frame  > max_size")
	super(buffer,self).append(value)

class package(object):
    def __init__(self,size=0,sender,receiver):
        self.size = 0
        self.sender = sender
        self.receiver = receiver

class device(object):
    '''
	classe do dispositivo de rede
	
    >>> device1 = device(rx_frame = 1,rx_size = 3)
    >>> p1 = package(10,"h1","h2")
    >>> device1.receive()
    receiving 1 package(s)
    >>> device1.transmit()
    sending 1 package(s)
    
    >>> device2 = device(rx_frame = 3,rx_size = 3)
    >>> device2.receive()
    >>> device2.receive()
    >>> device2.receive()
    receiving 3 package(s)

    '''
    def __init__(self,tx_size = 1,rx_size = 1,tx_frame = 1,rx_frame = 1,tx_usecs = 50,rx_usecs = 50):
	'''
	    parametros:
	    tx_size    tamanho do buffer de transmissao
	    rx_size    tamanho do buffer de recepcao
	    tx_frame   gera uma interrupção quando a quantidade de pacotes transmitida chegar a N
	    rx_frame   gera uma interrupção quando a quantidade de pacotes dentro do buffer de recepção chegar a N
	    tx_usecs   gera uma interrupção N microssegundos depois que um pacote for enviado
	    rx_usecs   gera uma interrupção N microssegundos depois que um pacote for recebido
	'''
	self.tx_buffer = buffer(tx_size)
	self.rx_buffer = buffer(rx_size)
	self.tx_frame = tx_frame
	self.rx_frame = rx_frame
	self.tx_usecs = tx_usecs
	self.rx_usecs = rx_usecs
	self.tx_timer = 0
	self.rx_timer = 0
	self.tx_drop = 0
	self.rx_drop = 0
    
    def send_packages(self):
	'''
	    pega os pacotes do buffer de transmissão e os transmite   
	    retorno:
	    número de interrupções gerada
	'''
	print "sending %d package(s)" % len(self.tx_buffer)
	self.tx_buffer.clean_stack()
    
    def receive_packages(self):
	'''
	    pega os pacotes do buffer
	    retorno:
	    número de interrupções gerada
	'''
	print "receiving %d package(s)" % len(self.rx_buffer)
	self.rx_buffer.clean_stack()
    
    def transmit(self,node_name):
	'''
	    adiciona um pacote no buffer de recepçao
	'''
	self.tx_buffer.append("1")
	self.tx_control()
    
    def receive(self):
	'''
	    adiciona um pacote no buffer de transmissão
	'''
	self.rx_buffer.append("1")
	self.rx_control()
     
    def rx_control(self): 
	'''
	    controla a recepçao
	'''
	if self.rx_frame == len(self.rx_buffer):
	    self.receive_packages()
	elif self.rx_timer >= self.rx_usecs:
	    self.receive_packages()
	    self.rx_timer = 0
     
    def tx_control(self):    
	'''
	    controla a transmissao
	'''
	if self.tx_frame == len(self.tx_buffer):
	    self.send_packages()
	elif self.tx_timer >= self.tx_usecs:
	    self.send_packages()
	    self.tx_timer = 0
     
    def set_tx_timer(self):
	self.tx_timer += 1

    def set_rx_timer(self):	
        self.rx_timer += 1

import sys
def main(argv = None):
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    sys.exit(main())
