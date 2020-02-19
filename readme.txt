开发游戏主要是pygame模块,下面介绍一下用到的函数和游戏开发的心得
1.用到的函数
    pygame.Rect(x, y, width, height) 用于返回一个矩形对象
        (x, y)指定了该矩形对象在屏幕上绘制的起始位置
        (width, height)指定了该矩形对象的大小
        该矩形对象可以使用对象名.属性名获得关于矩形对象的参数值
    pygame.image.load(name) 用于返回一个图片的引用
    图像名.get_rect() 返回图像的矩形对象
    pygame.display.set_mode(坐标元组) 用于描绘一个图像,可以用于设置屏幕,返回的是一个surface对象
    surface对象.blit(image对象,位置) 用于在屏幕上绘制一幅图像
    pygame.time.Clock() 用来声明一个时钟对象记录CPU当前时钟,第一次调用时返回当前时间,第二次调用返回据第一次的时间间隔
    Clock().tick(num) 用于设置游戏的运行速度,frame per second:fps
    pygame.time.set_timer(eventid, time) 可以按照时间重复的创建一个事件,
        第一个参数事件代号需要基于常量pygame.USEREVENT来指定,pygame.USEREVENT是一个整数,后续发生的事件可以用pygame.USEREVENT+1来指定
        第二个参数表明两次事件间隔的时间,单位是毫秒
        该方法可以在后面监听模块中被监听,一旦监听成功程序可以做相应的动作
        在本次游戏中,敌机和子弹的生成就是由该方法指定的,因此并不是所有的精灵都是在__create_sprites()中创建的,
    pygame.sprite.Group() 用于创建一类精灵的精灵组
        可以在创建精灵组时就把精灵对象添加进来,也可以在后续代码中通过精灵组名.add(精灵对象名)的形式添加
        精灵组提供了两个方法
        update() 精灵组调用该方法可以使组内所有的精灵都调用自己的update()方法
        draw(屏幕对象) 精灵组调用该方法使每个精灵都可以在屏幕上呈现
    pygame.event.get() 用于返回事件列表
    pygame.sprite.groupcollide(group1, group2, dokill1, dokill2) 检测两个精灵组之间是否发生了碰撞,dokill参数表明碰撞之后是否仍然存在于精灵组中
    pygame.sprite.spritecollide(sprite, group, dokill) 检测精灵和精灵组中是否发生碰撞





