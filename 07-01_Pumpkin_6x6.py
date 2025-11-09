# 肥料、ヒマワリ、カボチャ、リスト、インポート、解放及び畑の拡張を目指す

field_range_x = 6
field_range_y = 6
is_up = True


# return
# 	True  = 偶数
# 	False = 奇数
def is_even(n):
	return n % 2 == 0


# 初期化
def init():
	clear() # 植付けで解放
	
	# for 及び range() は拡大2で解放
	for x in range(field_range_x): # 畑の幅を指定
		for y in range(field_range_y): # 畑の高さを指定
			till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)



# メインループ
def main():
	while True:
		#e = get_entity_type()
		#if can_harvest():
		harvest()
		# 収穫し元あったものを植え直す
		#if e !=  .Grass and e != None:
		plant(Entities.Pumpkin)
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

if __name__ == "__main__":
	init()
	main()
	
EOF=1