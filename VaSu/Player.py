import pygame
import math

player_walk_images = [pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-1.png"), pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-2.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-3.png"), pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-4.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-5.png"), pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-6.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-7.png"), pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Run_left/run_left-8.png")]

player_idle_images = [pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-1.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-2.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-3.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-4.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-5.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-6.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-7.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-8.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-9.png"),
                      pygame.image.load("D:/pythonProject/VaSu/Images/Toaster_Bot_Ready/Idle_left/idle_left-10.png")]


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.run_animation_count = 0
        self.idle_animation_count = 0
        self.moving_left = False
        self.moving_right = False
        self.moving_up_or_down = False
        self.watching_left = True
        self.watching_right = False

    def main(self, display):
        if self.run_animation_count + 1 >= 64:
            self.run_animation_count = 0

        self.run_animation_count += 1

        if self.idle_animation_count + 1 >= 100:
            self.idle_animation_count = 0
        self.idle_animation_count += 1

        if self.moving_left:
            display.blit(pygame.transform.scale(player_walk_images[self.run_animation_count // 8], (34, 36)),
                         (self.x, self.y))
        elif self.moving_right:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.run_animation_count // 8], True, False), (34, 36)),
                         (self.x, self.y))
        elif self.moving_up_or_down:
            if self.watching_left:
                display.blit(pygame.transform.scale(player_walk_images[self.run_animation_count // 8], (34, 36)),
                             (self.x, self.y))
            if self.watching_right:
                display.blit(pygame.transform.scale(
                    pygame.transform.flip(player_walk_images[self.run_animation_count // 8], True, False), (34, 36)),
                             (self.x, self.y))

        else:
            if self.watching_left:
                display.blit(pygame.transform.scale(player_idle_images[self.idle_animation_count // 10], (34, 36)),
                             (self.x, self.y))
            elif self.watching_right:
                display.blit(pygame.transform.scale(
                    pygame.transform.flip(player_idle_images[self.idle_animation_count // 10], True, False), (34, 36)),
                             (self.x, self.y))

        self.moving_left = False
        self.moving_right = False
        self.moving_up_or_down = False


        ### pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

class PlayerProjectile:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y - self.mouse_y, x - self.mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(display, (0, 0, 0), (self.x, self.y), 5)