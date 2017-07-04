# Alien_invasion
## 简介
  在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可以使用空格键进行射击。
  游戏开始时，一群外星人出现在天空，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们的移动速度更快。只要有外星人撞到了玩家的飞船或者到底屏幕底部，玩家就损失一条飞船。玩家损失三条飞船后，游戏结束。

## 文件说明
**alien_invasion.py**
  主文件alien_invasion.py创建一系列游戏需要的对象：存储在ai_settings中的设置、存储在screen中的主显示surface、一个飞船实例ship和一个用于存储子弹的编组bullets。
  文件中还包含游戏的主循环，该循环调用check_events()、ship.update()、update_bullets()、upadate_screen()。
  运行该文件就可以玩《外星人入侵》，其他文件都会被直接或者间接导入其中。

**settings.py**
  文件settings.py包含Settings类，该类只有__init__()，用于初始化控制游戏外观和飞船速度。
  
**game_functions.py**
  文件game_functions.py包含一系列游戏相关函数。check_events()检测相关事件，如按键和松开，并使用辅助函数check_keydown_events()、check_keyup_events()、update_bullets()等来处理这些事件。此外，update_screen()在每次主循环中重绘屏幕。

**ship.py**
   文件ship.py包含Ship类，该类包含__init__()、管理飞船位置的方法update()以及在屏幕绘制飞船的方法blitme()。表示飞船的图像在images文件夹下ship.bmp中。
   
**bullet.py**
  文件bullet.py包含Bullet类，父类为pygame.Sprite。通过使用Sprite类，可以将游戏中相关的元素编组，进而同时操作编组中的元素。该类包含__init__()、向上移动子弹发方法update()以及在屏幕绘制子弹的方法draw_bullet()。
  
**alien.py**
  文件alien.py包含Alien类，父类为pygame.Sprite。  
  
## 其他
  需要安装python、Pygame(https://bitbucket.org/pygame/pygame/downloads/)
