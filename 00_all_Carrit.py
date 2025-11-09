# 全力ニンジン

clear() # 植付けで解放
field_range_x = 8
field_range_y = 8
# for 及び range() は拡大2で解放
for x in range(field_range_x): # 畑の幅を指定
	for y in range(field_range_y): # 畑の高さを指定
		till()
		plant(Entities.Carrot)
		move(North)
	move(East)
	
while True:
	if can_harvest():
		# 収穫し元あったものを植え直す
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == field_range_y-1: # 畑の高さ-1
		move(East)
	move(North)	
		
	