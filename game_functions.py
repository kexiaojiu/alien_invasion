#coding=utf-8
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_key_down_events(event,ai_settings, screen, stats, play_button, ship, 
                        aliens, bullets):
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
    elif event.key == pygame.K_p:
        #按键p开始游戏
        start_game(ai_settings, screen, stats, play_button, ship, aliens, 
                bullets)    
    elif event.key == pygame.K_q:
        #按键q退出游戏
        save_high_score(stats)
        sys.exit()

def save_high_score(stats):
    """保存最高分到high_score.txt"""
    file_name = stats.store_high_score_file_name
    high_score_str = str(stats.high_score)
    with open(file_name, 'w') as f_obj:
        f_obj.write(high_score_str)

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        #停止移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        #停止移动飞船
        ship.moving_left = False
 
    
def start_game(ai_settings, screen, stats, score, play_button, ship, aliens, 
               bullets):
    """开始游戏"""
    if not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        
        # 隐藏鼠标
        pygame.mouse.set_visible(False)
        
        # 重置游戏统计信息
        stats.rest_stats()
        stats.game_active = True
        
        # 重置记分牌图像
        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        # 重置剩余飞船数目信息
        score.prep_ships()
        
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 创建一群外星人，并将飞船放在底部正中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_play_button(ai_settings, screen, stats, score, play_button, ship, 
                    aliens, bullets, mouse_x, mouse_y): 
    """在玩家点击Play按钮时候开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(ai_settings, screen, stats, score, play_button, ship, aliens, 
                bullets)
        

def check_events(ai_settings, screen, stats,score, play_button, ship, aliens, 
                bullets):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event,ai_settings, screen, stats, play_button, 
                                ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score, play_button, 
                            ship, aliens, bullets, mouse_x, mouse_y)    


def check_high_score(stats, score):
    """检查是否诞生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()
 


def update_bullets(ai_settings, screen, stats, ship, aliens, bullets, score):
    """更新子弹位置，删除已经消失的子弹"""
    # 更新子弹位置
    bullets.update()
    
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, stats, ship, aliens, 
                                bullets, score)
    

def check_bullet_alien_collisions(ai_settings, screen, stats, ship, aliens, 
                                bullets, score):    
    # 检查是否有子弹击中外星人，如果有，就删除对应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    # 每杀死一个外星人，加分
    if collisions:
        # 添加击中外星人音效
        play_sound_effect_bomp(ai_settings)
        
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score.prep_score()
        # 检查是否超过最高分    
        check_high_score(stats, score)    
    # 升级
    start_new_level(ai_settings, screen, stats, ship, aliens, bullets, score)
    
    
def start_new_level(ai_settings, screen, stats, ship, aliens, bullets, score):    
    if len(aliens) == 0:
        # 删除现有的子弹，增加一个等级，加快游戏节奏，并且新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        score.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)
        
        
def play_sound_effect_shot(ai_settings):
    # 添加发射子弹的音效
    file_sound_shot = ai_settings.file_sound_shot
    try:
        sound_effect_shot = pygame.mixer.Sound(file_sound_shot)
        sound_effect_shot.play() 
    except pygame.error:
        print("The file " + file_sound_shot + " does not exist!")   


def play_sound_effect_bomp(ai_settings):
    # 添加击中外星人的音效
    file_sound_bomp = ai_settings.file_sound_bomp
    try:
        sound_effect_bomp = pygame.mixer.Sound(file_sound_bomp)
        sound_effect_bomp.play()
    except pygame.error:
        print("The file " + file_sound_bomp + " does not exist!")


def play_sound_effect_game_over(ai_settings):
    # 添加游戏结束的音效
    file_sound_game_over = ai_settings.file_sound_game_over
    try:
        sound_effect_game_over = pygame.mixer.Sound(file_sound_game_over)
        sound_effect_game_over.play() 
    except pygame.error:
        print("The file " + file_sound_game_over + " does not exist!")
    
    
                
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有超过子弹数上限，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        # 添加发射子弹的音效
        play_sound_effect_shot(ai_settings)

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


def update_aliens(ai_settings, stats, score, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕边缘，然后更新外星人位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # 检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, score, screen, ship, aliens, bullets)
    
    # 检查是否有外星人到达屏幕底部    
    check_aliens_bottom(ai_settings, stats, score, screen, ship, aliens, bullets)


def check_aliens_bottom(ai_settings, stats, score, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 与飞船被撞相同处理
            ship_hit(ai_settings, stats, score, screen, ship, aliens, bullets)
            break


def ship_hit(ai_settings, stats, score, screen, ship, aliens, bullets):
    """相应外星人撞到飞船"""
    
    if stats.ship_left > 1:
        # 将ship_left减一
        stats.ship_left -= 1
        # 更新剩余飞船数目
        score.prep_ships()
        
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群外星人，并将飞船放在底部正中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        # 添加游戏结束的音效
        play_sound_effect_game_over(ai_settings)
        stats.game_active = False
        pygame.mouse.set_visible(True)
        sleep(0.5)
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        # 剩余飞船数目置零
        stats.ship_left = 0
        
        # 创建一群外星人，并将飞船放在底部正中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
    
def update_screen(ai_settings, screen, stats, ship, aliens, bullets, 
                play_button, score):
    """更新屏幕的图像，并切换到新屏幕"""    
    # 每次循环时候都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船位置            
    ship.blitme()
    for alien in aliens:
        alien.blitme()
    aliens.draw(screen)
    # 显示得分
    score.prep_ships()
    score.show_score()

    #~ for alien in aliens.sprites():
        #~ alien.blitme()
    # 如果游戏处于非激活状态，就绘制play按钮    
    if not stats.game_active:
        play_button.draw_button()
               
    # 让最近绘制的屏幕可见
    pygame.display.flip()    
