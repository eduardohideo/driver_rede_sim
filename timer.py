from network import sim_network

time = 0
package_per_microsecond = 1
device = sim_network.Device(rx_frame = 3,rx_size = 3)

while 1:
    time += 1
    if (time % package_per_microsecond) == 0:
	print time
	device.receive() 
