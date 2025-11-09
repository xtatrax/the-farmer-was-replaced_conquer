# 演算子、知覚、ニンジンを解放できるまで回す
while True:
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	move(North)