#Отрисовка дома
from wall import draw_wall
import simple_draw as sd

def draw_house(first_point, hight_house, wight_house):
    right_top_house = sd.get_point(first_point.x + wight_house, first_point.y + hight_house)
    sd.rectangle(left_bottom=first_point, right_top=right_top_house, width=1)
    draw_wall(point=first_point, hight=hight_house, wight=wight_house)
    #Отрисовка крыши
    point_left_roof = sd.get_point(first_point.x-10,first_point.y+hight_house)
    point_right_roof = sd.get_point(first_point.x+wight_house+ 10, first_point.y + hight_house)
    point_top_roof = sd.get_point(first_point.x + wight_house//2, first_point.y + hight_house+50)
    point_list = [point_top_roof,point_right_roof,point_left_roof]
    sd.polygon(point_list=point_list,color=(255,0,0),width=5 )
