# 変数 及び 関数を解放するまで回す

clear() # 植付けで解放

# for 及び range() は拡大2で解放
for x in range(3): # 畑の幅を指定
	for y in range(3): # 畑の高さを指定
		if y == 1:
			till()
			plant(Entities.Carrot)
		elif y == 2:
			plant(Entities.Bush)
		move(North)
	move(East)
	
while True:
	if can_harvest():
		# 収穫し元あったものを植え直す
		if get_entity_type() == Entities.Bush:
			harvest()
			plant(Entities.Bush)
		elif get_entity_type() == Entities.Carrot:
			harvest()
			plant(Entities.Carrot)
		else:
			harvest()
	if get_pos_y() == 2: # 畑の高さ-1
		move(East)
	move(North)	
		
	