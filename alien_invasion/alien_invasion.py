""" 运行游戏的主文件 """

import sys
import pygame

# 从一文件中将类导入进来
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as gf

def rum_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()

	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigh))
	pygame.display.set_caption("Alien Invasion")

	# 创建Play button
	play_button = Button(ai_settings, screen, "Play")

	# 创建一架飞船
	ship = Ship(ai_settings, screen)

	# 创建一个用于存储子弹的编组
	bullets = Group()

	# 创建一个外星人编组
	aliens = Group()

	# 创建一个用于存储游戏统计信息的实例,并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			
			# 更新子弹的位置
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

			# 更新外星人位置
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

		# 每次循环时都会重新绘制屏幕
		# 让最近的绘制的在屏幕可见
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

rum_game()
