# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 08:13:44 2017

@author: aleks
"""

import pygame

class Button():
    
    def __init__(self, screen ,center_x ,center_y , file_location, file_location2, size):
        self.screen = screen
        #download image
        self.bt_image = pygame.image.load(str(file_location))
        self.bt_image = pygame.transform.size(self.bt_image, size)
        self.bt_image = self.bt_image.convert_alpha()
        
        self.rect = self.bt_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
    def blitme(self):
        #draw button in her position
        self.screen.blit(self.bt_image, self.rect)
    def blitmeclick(self):
        #draw button in her position
        self.screen.blit(self.bt_imageclick, self.rect)

class Start(Button):
    def __init__(self, screen ,center_x ,center_y , file_location,file_location2, size):
        super(Start,self).__init__(screen ,center_x ,center_y , file_location,file_location2, size)
        self.bt_image = pygame.image.load(str(file_location))
        self.bt_image = pygame.transform.size(self.bt_image, size)
        self.bt_image = self.bt_image.convert()
        self.bt_imageclick = pygame.image.load(str(file_location2))
        self.bt_imageclick = pygame.transform.size(self.bt_imageclick, size)
        self.bt_imageclick = self.bt_imageclick.convert()
        
        
class Stop(Button):
    
    def __init__(self, screen ,center_x ,center_y , file_location,file_location2, size):
        super(Stop,self).__init__(screen ,center_x ,center_y , file_location,file_location2, size)
        self.bt_image = pygame.image.load(str(file_location))
        self.bt_image = pygame.transform.size(self.bt_image, size)
        self.bt_image = self.bt_image.convert()
        self.bt_imageclick = pygame.image.load(str(file_location2))
        self.bt_imageclick = pygame.transform.size(self.bt_imageclick, size)
        self.bt_imageclick = self.bt_imageclick.convert()
        
class Pause(Button):
    
    def __init__(self, screen ,center_x ,center_y , file_location,file_location2, size):
        super(Pause,self).__init__(screen ,center_x ,center_y , file_location,file_location2, size)
        self.bt_image = pygame.image.load(str(file_location))
        self.bt_image = pygame.transform.size(self.bt_image, size)
        self.bt_image = self.bt_image.convert()
        self.bt_imageclick = pygame.image.load(str(file_location2))
        self.bt_imageclick = pygame.transform.size(self.bt_imageclick, size)
        self.bt_imageclick = self.bt_imageclick.convert()
        self.pause = True
        
class Scroll(Button):
    
    def __init__(self, screen ,center_x ,center_y , file_location, file_location2, size):
        super(Scroll,self).__init__(screen ,center_x ,center_y , file_location, file_location2, size)
        self.bt_image = pygame.image.load(str(file_location))
        self.bt_image = pygame.transform.size(self.bt_image, size)
        self.bt_image = self.bt_image.convert_alpha()
        self.bt_imageclick = pygame.image.load(str(file_location2))
        self.bt_imageclick = pygame.transform.size(self.bt_imageclick, size)
        self.bt_imageclick = self.bt_imageclick.convert_alpha()
        self.pause = True
        
        
class Galileo(Button):
    
    def __init__(self, screen ,center_x ,center_y , file_location, file_location2, size):
        super(Galileo,self).__init__(screen ,center_x ,center_y , file_location, file_location2, size)
        self.bt_image = pygame.image.load(str(file_location))
        self.bt_image = pygame.transform.size(self.bt_image, size)
        self.bt_image = self.bt_image.convert_alpha()
        self.bt_imageclick = pygame.image.load(str(file_location2))
        self.bt_imageclick = pygame.transform.size(self.bt_imageclick, size)
        self.bt_imageclick = self.bt_imageclick.convert_alpha()
        self.flag = False
        self.clickflag = True
        
    def click(self):
        self.clickflag = False
        if  self.flag:
            self.flag = False
        else:
            self.flag = True
        
class Change_velocity(Button):
    
    def __init__(self, screen ,left ,top , file_location,file_location2, size):
        super().__init__(screen ,left ,top , file_location,file_location2, size)
        self.rect.left = left
        self.rect.top = top
        self.bt1 = pygame.image.load('images/button1.jpg')
        self.bt1 = pygame.transform.size(self.bt1, [20, 100])
        self.bt1 = self.bt1.convert()
        self.bt1_x = self.rect.left
        
    def blitme(self):
        #draw button in her position
        self.screen.blit(self.bt_image, self.rect)
        self.screen.blit(self.bt1,(self.bt1_x, self.rect.centery - 50))
        
class Ruseng(Galileo):
    
    def __init__(self, screen ,center_x ,center_y , file_location, file_location2, size):
        super(Ruseng,self).__init__(screen ,center_x ,center_y , file_location,file_location2, size)
        self.bt_image = pygame.image.load(str(file_location))
        self.bt_image = pygame.transform.size(self.bt_image, size)
        self.bt_image = self.bt_image.convert()
        self.bt_imageclick = pygame.image.load(str(file_location2))
        self.bt_imageclick = pygame.transform.size(self.bt_imageclick, size)
        self.bt_imageclick = self.bt_imageclick.convert()
        self.flag = False
        self.clickflag = True
        
        
        