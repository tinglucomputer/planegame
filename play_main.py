from play_sprites import *

import pygame

pygame.init()

# TODO 显示分数,学会画单数字图片,对Python的画图函数要有所了解

class PlayGame(object):

    def __init__(self):

        print("游戏初始化")

        self.screen = pygame.display.set_mode(SCREEN_SECT.size)

        self.score = pygame.image.load("./images/0.png")
        self.score1 = pygame.image.load("./images/1.png")

        self.clock = pygame.time.Clock()

        self.__create_sprites()

        self.score_num = 0

        # 设置定时器事件创建敌机,第二个参数以毫秒计时
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 创建背景精灵
        bg1 = BackGround()
        bg2 = BackGround(True)
        # 创建背景精灵组,使得背景在窗口上滚动起来,在视觉上以为飞机在动
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        print("游戏开始")

        while True:

            # 设置刷新频率
            self.clock.tick(CLOCK_FRE)

            # 事件监听
            self.__event_handler()

            # 碰撞检测
            self.__check_collide()

            # 更新精灵组
            self.__update_sprites()

            self.screen.blit(self.score, (0, 0))
            self.screen.blit(self.score1, (30, 0))

            # 显示
            pygame.display.update()

    def __event_handler(self):  # 事件监听

        for event in pygame.event.get():

            # 判断用户是否是单击了关闭用户的按钮
            if event.type == pygame.QUIT:
                self.__game_over()
            # 敌机
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy1 = Enemy()
                # 添加敌机精灵到敌机精灵组
                self.enemy_group.add(enemy1)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供的方法捕获键盘按键,返回的结果是按键的元组
        key_tuple = pygame.key.get_pressed()
        # 判断按键元组中对应的按键索引值是否为1,如果为1则说明按下了键
        if key_tuple[pygame.K_RIGHT]:
            # print("持续向右移动")
            self.hero.speed = 2
        elif key_tuple[pygame.K_LEFT]:
            # print("持续向左移动")
            self.hero.speed = -2
        else:
            self.hero.speed = 0
        # 也可以使用event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT判断是否按下了向右移动键
        # 只不过这样的方法并不能一直按着键

    def __check_collide(self):   # 碰撞检测

        # 子弹打中敌机
        collision_dict = pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        if len(collision_dict) > 0:
            self.score_num += len(collision_dict) * 10
            print(self.score_num)

        # 敌机与英雄碰撞
        sprite_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(sprite_list) > 0:
            # 英雄牺牲,从精灵组中删除
            self.hero.kill()

            PlayGame.__game_over()

    def __update_sprites(self):  # 更新精灵组

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()

        exit()


if __name__ == '__main__':

    game = PlayGame()

    game.start_game()

