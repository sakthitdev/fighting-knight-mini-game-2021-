import pygame
import random
import asyncio
pygame.init()

WIDTH,HEIGHT=1100,700
pygame.display.set_caption("PvP")
WIN=pygame.display.set_mode((WIDTH,HEIGHT))


BG=pygame.transform.scale(pygame.image.load("arena.png"),(WIDTH,HEIGHT))
sprite_sheet_1=pygame.image.load("_idle.png")
sprite_sheet_2=pygame.image.load("_idle2.png")
sprite_attack1=pygame.image.load("_Attack2.png")
sprite_attack2=pygame.image.load("_Attack22.png")
roll_button=pygame.transform.scale(pygame.image.load("roll_button.png"),(100,100))
shield_icon=pygame.image.load("shield_icon.png")
life_icon=pygame.transform.scale(pygame.image.load("life_icon.png"),(100,100))
play_icon=pygame.transform.scale(pygame.image.load("play_icon.png"),(120,100))
quit_icon=pygame.transform.scale(pygame.image.load("quit_icon.png"),(110,100))
icon=pygame.transform.scale(pygame.image.load("life_icon.png"),(200,200))
pygame.display.set_icon(icon)

class SpritSheet():
    def __init__(self,blank_sprite):
        self.sheet=blank_sprite
        
    def get_image(self,frame,width,height,scale,color):
        

        blank_sprite=pygame.Surface((width,height))
        blank_sprite.blit(self.sheet,(0,0),((frame*width),0,width,height))
        blank_sprite=pygame.transform.scale(blank_sprite,(width*scale,height*scale))
        blank_sprite.set_colorkey(color)

        return blank_sprite
    
    
class SpritSheet2():
    def __init__(self,blank_sprite2):
        self.sheet=blank_sprite2
        
    def get_image2(self,frame,width,height,scale,color):
        

        blank_sprite2=pygame.Surface((width,height))
        blank_sprite2.blit(self.sheet,(0,0),((frame*width),0,width,height))
        blank_sprite2=pygame.transform.scale(blank_sprite2,(width*scale,height*scale))
        blank_sprite2.set_colorkey(color)

        return blank_sprite2
 
sprite_sheet=SpritSheet(sprite_sheet_1)
sprite_sheet2=SpritSheet2(sprite_sheet_2)
sprite_atk1=SpritSheet(sprite_attack1)
sprite_atk2=SpritSheet(sprite_attack2)
black=(0,0,0) 



turn=random.randint(1,2)
ply_x,ply_y=0,0
if turn%2!=0:
    ply_x,ply_y=160,200
else:
   ply_x,ply_y= 790,200
sel_item=0

items=pygame.transform.scale(pygame.image.load("items_PVP.png"),(192*2,32*2))
outline_item=pygame.transform.scale(pygame.image.load("outline_PVP.png"),(32*2,32*2))


animation1_list=[]
animation1_list2=[]
atk_anim_list1=[]
atk_anim_list2=[]
animation_steps=10
atk_ani_steps=6
last_update=pygame.time.get_ticks()
last_update2=pygame.time.get_ticks()
last_update3=pygame.time.get_ticks()
last_update4=pygame.time.get_ticks()
animation_cooldown=70
animation_cooldown2=150
frame=0
frame2=9
atk_fram1=3
atk_frame2=5

mn=True

player_one=[1,1,1,1,2,2,2,3,3,4,4,5,6,6]
player_two=[1,1,1,1,2,2,2,3,3,4,4,5,6,6]

player_onech=random.randint(1,3)
player_twoch=random.randint(1,3)

pla1_mo=None
pla2_mo=None

ply1_shield=0
ply2_shield=0

if player_onech==1:
    player_one=[1,1,2,2,3,3,4,4,5,5,6,6]
    pla1_mo="luck"
elif player_onech==2:
    ply1_shield=2
    pla1_mo="free shield"
else:
    pla1_mo="none"


if player_twoch==1:
    player_two=[1,1,2,2,3,3,4,4,5,5,6,6]
    pla2_mo="luck"
elif player_twoch==2:
    ply2_shield=2
    pla2_mo="free shield"
else:
    pla2_mo="none"



for x in range(animation_steps):
    animation1_list.append(sprite_sheet.get_image(x,120,80,4,black))
    animation1_list2.append(sprite_sheet2.get_image2(x,120,80,4,black))
for x in range(atk_ani_steps):
    atk_anim_list1.append(sprite_atk1.get_image(x,120,80,4,black))
    atk_anim_list2.append(sprite_atk2.get_image(x,120,80,4,black))



class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def draw(self):
        action = False

        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked=True
                action=True

        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False

        WIN.blit(self.image,(self.rect.x,self.rect.y))
        return action
    
class Button1():
      def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
      def draw1(self):
        action1 = False

        pos1=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos1):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked=True
                action1=True

        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False

        WIN.blit(self.image,(self.rect.x,self.rect.y))
        return action1
    
   
rollbutton=Button(460,100,roll_button)
start_button=Button1(460,300,play_icon)
quit_button=Button1(465,380,quit_icon)

class HealthBar():
    def __init__(self,x,y,w,h,max_hp):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.hp=max_hp
        self.max_hp=max_hp
        
    
    def draw(self,surface):
        ratio=self.hp / self.max_hp
        pygame.draw.rect(surface,"red",( self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface,"green",( self.x, self.y, self.w * ratio, self.h))

    def draw2(self,surface):
        ratio=self.hp / self.max_hp
        pygame.draw.rect(surface,"green",( self.x, self.y,  self.w, self.h))
        pygame.draw.rect(surface,"red",( self.x, self.y, self.w  * ratio, self.h))
        


health_bar1=HealthBar(30,30,200,10,100)
health_bar2=HealthBar(860,30,200,10,100)


life1=100
life2=0

text_font=pygame.font.SysFont("Arial",25)
text_font_ss=pygame.font.SysFont("Arial",15)
text_font3=pygame.font.SysFont("Arial",40)

def draw_text(text,font,text_col):
    img=font.render(text,True,text_col)
    return img
 
ani_type=1 
ani_type2=1

run1=False
run11=True
roll=True

def main():
    global run1, run11, last_update, frame, last_update2, last_update3, last_update4, frame2, atk_fram1, atk_frame2, ani_type, ani_type2, life1, life2,sel_item, ply_x, ply_y, ply1_shield,ply2_shield, roll, turn 


    while run11==True:
        WIN.blit(BG,(0,0)) 
        if start_button.draw1()==True:
            run1=True
            run11=False
        if quit_button.draw1()==True:
            pygame.quit()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        
        
    while run1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1=False 
                break
            
        WIN.blit(BG,(0,0))

        current_time=pygame.time.get_ticks()
        current_time2=pygame.time.get_ticks()
        current_time3=pygame.time.get_ticks()
        current_time4=pygame.time.get_ticks()
        
        if current_time - last_update >= animation_cooldown:
            frame+=1
            last_update=current_time
            if frame >= len(animation1_list):
            
                frame=0
            
            
        if current_time2 - last_update2 >= animation_cooldown:
            frame2-=1
            last_update2=current_time2
            if frame < 1:
                
                frame2=9

        
        if current_time3 - last_update3 >= animation_cooldown2:
            atk_fram1+=1
            last_update3=current_time3
            
            if  atk_fram1 >= len(atk_anim_list1):
                ani_type=1
                atk_fram1=0
            
            
        if current_time4 - last_update4 >= animation_cooldown2:
            atk_frame2-=1
            last_update4=current_time4
            if atk_frame2 < 1:
                ani_type2=1
                atk_frame2=5       
            
        if ani_type==1:
            WIN.blit(animation1_list[frame],(30,280))
        if ani_type==2:
            WIN.blit(atk_anim_list1[atk_fram1],(30,280))
        
        if ani_type2==1:
            WIN.blit( animation1_list2[frame2],(550,280))
        
        if ani_type2==2:
            WIN.blit(atk_anim_list2[atk_frame2],(550,280))
            
                
        if rollbutton.draw() ==True and roll==True :
            if turn%2!=0:
                
                player_1_ch=random.choice(player_one)
                if player_1_ch==1:
                  sel_item=0
                  ani_type=2
                  if ply2_shield==0:
                    life2+=10
                    
                  else:
                    ply2_shield-=1
                
                elif player_1_ch==2:
                  sel_item=64
                  ani_type=2
                  if ply2_shield==0:
                    life2+=20
                  else:
                    ply2_shield-=1
                        
                elif player_1_ch==3:
                    sel_item=128
                    ani_type=2
                    if ply2_shield==0:
                      life2+=30
                    else:
                      ply2_shield-=1

                elif player_1_ch==4:
                  sel_item=192
                  life1+=10

                elif player_1_ch==5:
                  sel_item=256
                  life1+=20

                elif player_1_ch==6:
                  sel_item=320
                  ply1_shield+=1
                    
                else:
                    print("else part?")

                if life1>100:
                    life1=100
                turn+=1
                ply_x=790
                ply_y=200
            

            else:
                
                player_2_ch=random.choice(player_one)
                if player_2_ch==1:
                    sel_item=0
                    ani_type2=2
                    if ply1_shield==0:
                      life1-=10
                    
                    else:
                        ply1_shield-=1

                elif player_2_ch==2:
                    sel_item=64
                    ani_type2=2
                    if ply1_shield==0:
                      life1-=20
                    
                    else:
                        ply1_shield-=1
                
                    
                    
                elif player_2_ch==3:
                    sel_item=128
                    ani_type2=2
                    if ply1_shield==0:
                      life1-=30
                    
                    else:
                        ply1_shield-=1
                    
                    
                    
                elif player_2_ch==4:
                    sel_item=192
                    life2-=10
                    
                elif player_2_ch==5:
                    sel_item=256
                    life2-=20
                    
                elif player_2_ch==6: 
                    sel_item=320
                    ply2_shield+=1
                    
                else:
                    print("else part?")
                
                if life2<0:
                    life2=0

                turn+=1
                ply_x=160
                ply_y=200 

            
        

        health_bar1.hp=life1
        health_bar2.hp=life2
        health_bar1.draw(WIN)
        health_bar2.draw2(WIN)

        WIN.blit(items,(340,20))
        WIN.blit(outline_item,(341 + sel_item,20))

        WIN.blit(draw_text("Your Turn",text_font,(0,0,0)),(ply_x,ply_y))

        if ply1_shield==1 or ply1_shield==2 or ply1_shield==3  :
          WIN.blit(shield_icon,(40,45))
        if ply1_shield==2 or ply1_shield==3  :
          WIN.blit(shield_icon,(60,45))
        if ply1_shield==3 :
          WIN.blit(shield_icon,(80,45))

        if ply2_shield==1  or ply2_shield==2 or ply2_shield==3  :
          WIN.blit(shield_icon,(1030,45))
        if ply2_shield==2  or ply2_shield==3 :
          WIN.blit(shield_icon,(1010,45))
        if ply2_shield==3  :
          WIN.blit(shield_icon,(990,45))

        if ply1_shield>3:
            ply1_shield=3
        if ply2_shield>3:
            ply2_shield=3

        WIN.blit(life_icon,(-15,-10))
        WIN.blit(life_icon,(1020,-10))

        player1_life=str(life1)
        player2_life=str(100 - life2)

        WIN.blit(draw_text("Random modefier",text_font,(0,0,0)),(0,80))
        WIN.blit(draw_text("Random modefier",text_font,(0,0,0)),(935,80))
        WIN.blit(draw_text( pla1_mo,text_font_ss,(255,255,0)),(10,110))
        WIN.blit(draw_text(pla2_mo,text_font_ss,(255,255,0)),(1030,110))
        WIN.blit(draw_text(player1_life,text_font_ss,(0,0,0)),(24,22))
        WIN.blit(draw_text(player2_life,text_font_ss,(0,0,0)),(1059,22))

        if life1<=0  :
            WIN.blit(draw_text("PLAYER-2 WIN",text_font3,(0,0,255)),(425,240))
            pygame.display.update()
            roll=False
            pygame.time.delay(7000)
            break
            
        

        if life2>=100  :
            WIN.blit(draw_text("PLAYER-1 WIN",text_font3,(0,0,255)),(425,240))
            pygame.display.update()
            roll=False
            pygame.time.delay(7000)
            break
            
        pygame.display.flip()
        pygame.display.update()
        #await asyncio.sleep(0)
  
#asyncio.run(main())
while True:
   main()
pygame.quit()


 
