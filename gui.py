import pygame
import sudoku
import copy
from board_generator import board_generator


obj = board_generator()
mat = obj.get_board()


ques_bool = [[False for x in range(9)] for y in range(9)]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if(mat[i][j] != 0):
            ques_bool[i][j] = True

s = sudoku.sudoku(mat)
c = copy.deepcopy(s)
c.solve()
WIDTH = 600
HIGHT = 600
WHITE = (255,255,255)
GREY = (195,191,191)
YGREY = (206,195,96)
DRED = (193,0,0)
RED = (255,0,0)
BLUE_CANV = (186,201,236)
BLACK = (0,0,0)
LBLACK = (63,63,68)
LLBLACK = (82,81,97)
LIGHT_BLUE = (96,216,232)
GREEN = (0,255,0)
grid_position = [75,100]
sb_x = grid_position[0]
sb_y = grid_position[1]-60
sb_w = 60
sb_h = 30
nb_x = sb_x+sb_w+10
nb_y = sb_y
nb_w = 60
nb_h = 30

cell_size = 50
grid_size = cell_size*9
selected = None
mouse_position = None
user_input = None


pygame.init()
screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial',cell_size//2)
font1 = pygame.font.SysFont('comicsansms',cell_size//2)


def mouse_on_grid(mouse_position):
    if mouse_position[0] > grid_position[0] and mouse_position[1] > grid_position[1]:
        if mouse_position[0] < grid_position[0]+450 and mouse_position[1] < grid_position[1]+450:
            return True
        else:
            return False
    else:
        return False 


def update_board():
    if(not ques_bool[selected[1]][selected[0]]):
        s.board[selected[1]][selected[0]] = user_input


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if(mouse_on_grid(mouse_position)):
                selected = ((mouse_position[0]-grid_position[0])//cell_size,(mouse_position[1]-grid_position[1])//cell_size)
                #pygame.draw.rect(screen,LIGHT_BLUE,((selected[0]*cell_size) + grid_position[0],(selected[1]*cell_size) + grid_position[1],cell_size,cell_size))
                print(selected)
            else:
                selected = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                user_input = 1
            if event.key == pygame.K_2:
                user_input = 2
            if event.key == pygame.K_3:
                user_input = 3
            if event.key == pygame.K_4:
                user_input = 4
            if event.key == pygame.K_5:
                user_input = 5
            if event.key == pygame.K_6:
                user_input = 6
            if event.key == pygame.K_7:
                user_input = 7
            if event.key == pygame.K_8:
                user_input = 8
            if event.key == pygame.K_9:
                user_input = 9
            if event.key == pygame.K_DELETE:
                user_input = 0
            if event.key == pygame.K_s:
                selected = None
                s.board = c.board
            if(selected != None and user_input != None):
                update_board()

    screen.fill(BLUE_CANV)
    pygame.draw.rect(screen,LLBLACK,(grid_position[0],grid_position[1],450,450))

    #mouse updates
    mouse_position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #Drawing
    #button
    pygame.draw.rect(screen,DRED,(sb_x,sb_y,sb_w,sb_h))
    if(mouse_position[0] > sb_x and mouse_position[0] < sb_x+sb_w):
        if(mouse_position[1] > sb_y and mouse_position[1] < sb_y+sb_h):
            pygame.draw.rect(screen,RED,(sb_x,sb_y,sb_w,sb_h))
            if(click[0] == 1):
                selected = None
                s.board = c.board
    text = font.render("solve",True,WHITE)
    screen.blit(text,(sb_x+5,sb_y))


    pygame.draw.rect(screen,DRED,(nb_x,nb_y,nb_w,nb_h))
    if(mouse_position[0] > nb_x and mouse_position[0] < nb_x+nb_w):
        if(mouse_position[1] > nb_y and mouse_position[1] < nb_y+nb_h):
            pygame.draw.rect(screen,RED,(nb_x,nb_y,nb_w,nb_h))
            if(click[0] == 1):
                selected = None
                mat = obj.get_board()
                ques_bool = [[False for x in range(9)] for y in range(9)]
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        if(mat[i][j] != 0):
                            ques_bool[i][j] = True
                s = sudoku.sudoku(mat)
                c = copy.deepcopy(s)
                c.solve()
    text = font.render("New",True,WHITE)
    screen.blit(text,(nb_x+5,nb_y))


    #selection draw

    if s.board == c.board: #checking for fucking win
        text = font1.render(" You Win! ",True,DRED,GREY)
        screen.blit(text,(grid_position[0]+160,grid_position[1]+450+10))

    if selected != None:
        pygame.draw.rect(screen,LIGHT_BLUE,((selected[0]*cell_size) + grid_position[0],(selected[1]*cell_size) + grid_position[1],cell_size,cell_size))
    
    #drawing question
    for i in range(len(s.board)):
        for j in range(len(s.board[0])):
            if(s.board[i][j] != 0):
                if(ques_bool[i][j]):
                    pygame.draw.rect(screen,LBLACK,((j*cell_size) + grid_position[0],(i*cell_size) + grid_position[1],cell_size,cell_size))
                text = font.render(str(s.board[i][j]),True,WHITE)
                screen.blit(text,(grid_position[0]+(j*cell_size)+(cell_size//3),grid_position[1]+(i*cell_size)+(cell_size//4)))

    pygame.draw.rect(screen,BLACK,(grid_position[0],grid_position[1],WIDTH-150,HIGHT-150),2)
    for x in range(1,10):
        if(x%3 == 0):
            pygame.draw.line(screen,BLACK,(grid_position[0]+ (x*cell_size),grid_position[1]),(grid_position[0]+ (x*cell_size),grid_position[1]+450),2) 
            pygame.draw.line(screen,BLACK,(grid_position[0],grid_position[1]+ (x*cell_size)),(grid_position[0]+450,grid_position[1]+ (x*cell_size)),2)   
        else:
            pygame.draw.line(screen,BLACK,(grid_position[0]+ (x*cell_size),grid_position[1]),(grid_position[0]+ (x*cell_size),grid_position[1]+450))
            pygame.draw.line(screen,BLACK,(grid_position[0],grid_position[1]+ (x*cell_size)),(grid_position[0]+450,grid_position[1]+ (x*cell_size)))

    pygame.display.update()
    
    

pygame.quit()
