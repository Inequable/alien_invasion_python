""" 飞船类 """

import pygame

class Ship():
	"""飞船类"""
	def __init__(self, ai_settings, screen):
		""" 初始化飞船图像并设置其初始位置 """
		self.screen = screen
		self.ai_settings = ai_settings
		
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('./images/ship.bmp')
		self.rect = self.image.get_rect() # 飞船的矩形
		self.screen_rect = screen.get_rect() # 绘制成的屏幕矩形

		# 将每架飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		# self.rect.bottom = self.screen_rect.bottom
		self.y = float(self.screen_rect.bottom-self.rect.bottom)

		# 在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)

		# 右移动标志
		self.moving_right = False
		# 左移动标志
		self.moving_left = False
		# 上移动标志
		self.moving_up = False
		# 下移动标志
		self.moving_down = False

	def update(self):
		""" 根据移动标志调整飞船的位置 """
		# 更新飞船的center值，而不是rect对象
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.y -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom  < self.screen_rect.bottom:
			self.y += self.ai_settings.ship_speed_factor

		# 根据self.center更新rect对象
		self.rect.centerx = self.center
		self.rect.y = self.y

	def blitme(self):
		"""在指定的位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""让飞船在屏幕底端居中"""
		self.center = self.screen_rect.centerx