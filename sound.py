#coding=utf-8
import pygame

class Sound():
    file_sound_bomp = 'sound_effects\bomp.wav'
    file_sound_game_over = 'sound_effects\game_over.wav'
    file_sound_shot = 'sound_effects\shot.wav'
    
    sound_effect_bomp = pygame.mixer.Sound(file_sound_bomp)
    sound_effect_bomp.play()
