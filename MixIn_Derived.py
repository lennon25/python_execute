
class Dag(Mammal, Runable):
	pass

class Bat(Mammal, Flyable):
	pass

class Dag(Mammal, RunableMinIn, CarnivorousMinIn):
	pass


class MyTCPServer(TCPServer, ForkingMinIn):
	pass

class MyUDPServer(UDPServer, ThreadingMinIn):
	pass
