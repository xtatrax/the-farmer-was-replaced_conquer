# plant() clear() (植える)を解放できるまで回す
while True:
	if can_harvest():
		harvest()
	move(North)
	