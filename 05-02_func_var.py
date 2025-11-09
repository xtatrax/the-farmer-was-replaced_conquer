# 水やり 及び 木を解放するまで回す

field_range_x = 4
field_range_y = 4
is_up = True

# 初期化
def init():
	clear() # 植付けで解放
	
	# for 及び range() は拡大2で解放
	for x in range(field_range_x): # 畑の幅を指定
		for y in range(field_range_y): # 畑の高さを指定
			if y == 1:
				till()
				plant(Entities.Carrot)
			elif y == 2 or y == 3:
				plant(Entities.Bush)
			move(North)
		move(East)



# メインループ
def main():
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
		if ( (is_up and get_pos_y() == field_range_y-1) 
		or (not is_up and get_pos_y() == 0) ) :
			global is_up
			is_up = not is_up
			move(East)
		else:
			if is_up:
				move(North)
			else:
				move(South)

init()
main()