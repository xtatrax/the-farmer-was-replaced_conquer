#　全力草

clear() # 植付けで解放
field_range_x = 8
field_range_y = 8
# for 及び range() は拡大2で解放
while True:
	if can_harvest():
		harvest()
	if get_pos_y() == field_range_y-1: # 畑の高さ-1
		move(East)
	move(North)	
		
	