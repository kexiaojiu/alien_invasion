#coding=utf-8
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_key_down_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一个子弹，并将子弹加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        #按键q退出游戏
        sys.exit()

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        #停止移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        #停止移动飞船
        ship.moving_left = False
    


def check_events(ai_settings, screen, ship, bullets):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕的图像，并切换到新屏幕"""    
    # 每次循环时候都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()        
    ship.blitme()
    aliens.draw(screen)
    #~ for alien in aliens.sprites():
        #~ alien.blitme()
                
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹位置，删除已经消失的子弹"""
    # 更新子弹位置
    bullets.update()
    
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # 检查是否有子弹击中外星人，如果有，就删除对应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        # 删除现有的子弹，并且新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有超过子弹数上限，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建一个子弹，并将子弹加入到编组bullets中
        net_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(net_bullet)
        
    
def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并把它加入当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
    
def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人并计算一行可以容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
    # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并把它加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达屏幕边缘时采取相应措施"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将外星人下移并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """更新外星人位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
