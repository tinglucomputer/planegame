import random
import pygame

# 设置屏幕的大小
SCREEN_SECT = pygame.Rect(0, 0, 512, 512)

# 设置时钟频率
CLOCK_FRE = 60

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# 某个类的父类不是object类则需要在初始化方法中调用父类的初始化方法
class GameSprite(pygame.sprite.Sprite):  # 精灵

    def __init__(self, image_name, speed=1):

        super().__init__()

        self.image = pygame.image.load(image_name)

        self.rect = self.image.get_rect()

        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class BackGround(GameSprite):   # 背景精灵

    def __init__(self, not_first=False):

        # 调用父类方法实现精灵的创建
        super().__init__("./images/bg1.png")

        if not_first:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_SECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):    # 敌机精灵

    def __init__(self):

        # 调用父类方法,创建敌机精灵,同时指定敌机图片
        super().__init__("./images/e0.png")

        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)

        # 指定敌机的初始随机位置
        self.rect.x = random.randint(0, SCREEN_SECT.width - self.rect.width)
        self.rect.bottom = 0    # 可以使飞机看上去是从屏幕上方一点一点的飞进来的

    def update(self):

        # 调用父类方法,保持垂直方向上的飞行
        super().update()

        # 判断是否飞出屏幕,如果是,则在精灵组中删除敌机精灵
        if self.rect.y >= SCREEN_SECT.height:

            # kill方法可以使精灵在精灵组中被移除,精灵会自动销毁
            self.kill()

    def __del__(self):  # 在内存销毁之前自动调用
        pass


class Hero(GameSprite):

    def __init__(self):

        super().__init__("./images/me.png", 0)

        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_SECT.centerx
        self.rect.bottom = SCREEN_SECT.bottom - 120

        # 子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        self.rect.x += self.speed

        if self.rect.x >= SCREEN_SECT.width - self.rect.width:
            self.rect.x = SCREEN_SECT.width - self.rect.width
        elif self.rect.x <= 0:
            self.rect.x = 0

    def fire(self):
        # print("一次性发射3枚子弹")

        for i in (0, 1, 2):
            # 创建子弹精灵
            bullet = Bullet()

            # 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 将精灵添加到精灵组中
            self.bullets.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./images/pd.png", -2)

    def update(self):

        super().update()

        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        pass




