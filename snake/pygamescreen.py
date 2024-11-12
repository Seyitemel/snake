import random
import time

import pygame

import circle
class pygamescreen:
    snake = []
    direction = "G"
    food = circle.circle(0,0,0)
    is_food=False
    def __init__(self):
        pygame.init()

        # Ekran boyutlarını ayarla
        self.screen_width = 400
        self.screen_height = 300
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Don't Close Screen")

        # Renk tanımları
        black = (255, 255, 255)
        self.red = (255, 0, 0)

        self.running = True
        self.create_circles()
        self.screen.fill(black)
        #self.update_snake()
        self.draw_cricle()
        pygame.display.flip()
        print("****************************")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Pencereyi kapatma
                    self.running = False

            # Ekranı temizle
            self.screen.fill(black)
            self.update_snake()
            self.check_collision()
            self.draw_cricle()
            pygame.display.flip()
            print("****************************")
            time.sleep(0.2)
            #user_input = input("Lütfen bir sayı girin: ")

        # Pygame'i kapat
        pygame.quit()
    def create_circles(self):
        c1 = circle.circle(1, 260, 260)
        self.snake.append(c1)

    def draw_cricle(self):
        print("in draw_cricle")
        self.draw_aim()
        self.check_fooding()
        print("len ",len(self.snake))
        print("in snakeeeeeeeeeeeeeeeeeeee")
        for circlefordraw in self.snake:
            if (circlefordraw.getWidthPosition()>self.screen_width or circlefordraw.getWidthPosition() <0 ) or (circlefordraw.getHeigthPosition()>self.screen_height or circlefordraw.getHeigthPosition()<0):
                self.running = False
                break
            #print(circlefordraw.getId(),circlefordraw.getHeigthPosition(), circlefordraw.widthPosition)
            pygame.draw.circle(self.screen, self.red, (circlefordraw.widthPosition, circlefordraw.heigthPosition), 10)
            self.draw_food()

        print("in snakeeeeeeeeeeeeeeeeeeee")
    def draw_food(self):
        if (self.is_food)==False:
            print("yeni food oluştur")
            width,height = self.random_modulo()
            #width,height = 250,350
            print("seçilen position ",width,height)
            self.food = circle.circle(len(self.snake),width,height)
            print("food crated= ",self.food.getId(), self.food.getHeigthPosition(), self.food.widthPosition)
            self.is_food =True
            pygame.draw.circle(self.screen, (255, 255, 0), (self.food.widthPosition, self.food.heigthPosition), 10)
        else:
            print("aktif food var")
            pygame.draw.circle(self.screen, (255,255,0), (self.food.widthPosition,self.food.heigthPosition), 10)


    def random_modulo(self):
        # find possible width and heigth position for food circle
        candidates_for_width = [i for i in range(0, self.screen_width + 1) if i % 20 == 0]
        candidates_for_height = [i for i in range(0, self.screen_height + 1) if i % 20 == 0]
        not_candidates_width =[]
        not_candidates_height =[]

        for circ in self.snake:
            not_candidates_width.append(circ.getWidthPosition())
            not_candidates_height.append(circ.getHeigthPosition())
        find=True
        while find:
            if candidates_for_width and candidates_for_height:
                width = random.choice(candidates_for_width)
                height = random.choice(candidates_for_height)
                if (width in not_candidates_width) and (height in not_candidates_height):
                    find=True
                else:
                    find=False
                return width,height
            else:
                return None

    def update_snake(self):
        print("in update_snake")
        move = random.randrange(1,4)
        # kullanici_girdisi = input("Bir sayı girin: ")
        #
        # # Girilen değeri tam sayıya dönüştür
        # move = int(kullanici_girdisi)
        if (len(self.snake)!=1):
            for i in range(len(self.snake)-1,0,-1):
                print(i)
                self.snake[i].setWidthPosition(self.snake[i-1].getWidthPosition())
                self.snake[i].setHeigthPosition(self.snake[i-1].getHeigthPosition())
        if move == 1:
            if self.direction =="K"  :
                self.snake[0].setWidthPosition(self.snake[0].getWidthPosition() - 20)
                self.direction = "B"
            elif self.direction =="G":
                self.snake[0].setWidthPosition(self.snake[0].getWidthPosition() + 20)
                self.direction = "D"
            elif self.direction =="D":
                self.snake[0].setHeigthPosition(self.snake[0].getHeigthPosition() - 20)
                self.direction = "K"
            elif self.direction == "B":
                self.snake[0].setHeigthPosition(self.snake[0].getHeigthPosition() + 20)
                self.direction = "G"

        elif move == 2:
            if self.direction =="K"  :
                self.snake[0].setHeigthPosition(self.snake[0].getHeigthPosition() - 20)
                self.direction = "K"
            elif self.direction =="G":
                self.snake[0].setHeigthPosition(self.snake[0].getHeigthPosition() + 20)
                self.direction = "G"
            elif self.direction =="D":
                self.snake[0].setWidthPosition(self.snake[0].getWidthPosition() + 20)
                self.direction = "D"
            elif self.direction == "B":
                self.snake[0].setWidthPosition(self.snake[0].getWidthPosition() - 20)
                self.direction = "B"

        elif move == 3:
            if self.direction =="K"  :
                self.snake[0].setWidthPosition(self.snake[0].getWidthPosition() + 20)
                self.direction = "D"
            elif self.direction =="G":
                self.snake[0].setWidthPosition(self.snake[0].getWidthPosition() - 20)
                self.direction = "B"
            elif self.direction =="D":
                self.snake[0].setHeigthPosition(self.snake[0].getHeigthPosition() + 20)
                self.direction = "G"
            elif self.direction == "B":
                self.snake[0].setHeigthPosition(self.snake[0].getHeigthPosition() - 20)
                self.direction = "K"
        print(self.direction)
        print("move ", move)
        print(self.snake[0].getHeigthPosition(), self.snake[0].widthPosition)

    def draw_aim(self):

        if self.direction == "K":
            pygame.draw.rect(self.screen, (0,255,255), (self.snake[0].getWidthPosition()-5, self.snake[0].getHeigthPosition()-25, 10, 30))
        elif self.direction == "G":
            pygame.draw.rect(self.screen, (0,255,255), (self.snake[0].getWidthPosition()-5, self.snake[0].getHeigthPosition()-5, 10, 30))
        elif self.direction == "B":
            pygame.draw.rect(self.screen, (0,255,255), (self.snake[0].getWidthPosition()-25, self.snake[0].getHeigthPosition()-5, 30, 10))
        elif self.direction == "D":
            pygame.draw.rect(self.screen, (0, 255, 255),(self.snake[0].getWidthPosition() -5, self.snake[0].getHeigthPosition() - 5, 30, 10))

    def check_fooding(self):
        print("in check_fooding")
        print("width ",self.food.getWidthPosition())
        if (self.snake[0].getWidthPosition() == self.food.getWidthPosition()) and (self.snake[0].getHeigthPosition()==self.food.getHeigthPosition()):
            print("Snake is on food!")
            self.snake.append(circle.circle(len(self.snake),self.snake[0].getWidthPosition(),self.snake[0].getHeigthPosition()))
            self.is_food=False

    def check_collision(self):
        for i in range(1,len(self.snake)):
            print("check for ",i)
            if self.snake[i].getWidthPosition() == self.snake[0].getWidthPosition() and self.snake[i].getHeigthPosition() == self.snake[0].getHeigthPosition():
                print("yılan kendini yedi")
                self.running=False
