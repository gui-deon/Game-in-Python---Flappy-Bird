import pygame
import random
import sys

velocidade = 0
posicaoInicial = 300
posicaoXcano = 550
posicaoYCanoCima = random.randint(150, 400)
larguraCano = 100
velocidadeCano = 7
espaco = 280
posicaoYcanoBaixo = posicaoYCanoCima + espaco
passaro = pygame.Rect(50, posicaoInicial, 100, 50)
pontuacao = 0
cano_pont = 0
cor_texto = (0, 0, 0)
jogando = 1
saiu_area = 0
bateu = 0

pygame.init()
fonte = pygame.font.SysFont(None, 35)
screen = pygame.display.set_mode((500, 900))
clock = pygame.time.Clock()
running = True

mensagem_pont = fonte.render(f"Sua pontuaçao nessa rodade foi", True, cor_texto)
mensagem_pont2 = fonte.render(f" de {pontuacao} pontos", True, cor_texto)
mensagem_SairForaTela = fonte.render("Voce saiu da area de jogo, por isso foi penalizado com a derrota da rodada e tera seus pontos resetados.", True, cor_texto)
mensagem_perder = fonte.render("Voce perdeu.", True, cor_texto)
mensagem_rec = fonte.render("Aperte ENTER para recomeçar", True, cor_texto)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocidade = -10
            if event.key == pygame.K_RETURN:
                jogando = 1
                saiu_area = 0
                pontuacao = 0
                bateu = 0
                velocidade = 0
                cano_pont = 0

    screen.fill("sky blue")

    if jogando == 1:

        cano_cima = pygame.draw.rect(surface=screen, color="green", rect=(posicaoXcano, 0, larguraCano, posicaoYCanoCima))
        cano_baixo = pygame.draw.rect(surface=screen, color="green", rect=(posicaoXcano, posicaoYcanoBaixo, larguraCano, 1000))
        posicaoXcano -= velocidadeCano

        passaro = pygame.draw.rect(surface=screen, color="yellow", rect=(50, posicaoInicial, 100, 50), width=int(0))
        posicaoInicial += velocidade
        velocidade += 0.5

        if velocidade >= 10:
            velocidade = 10

        if posicaoInicial <= -60 or posicaoInicial >= 950 :
            jogando = 0
            cano_pont = 0
            saiu_area = 1

        if posicaoXcano <= -150 :
            posicaoXcano = 520
            posicaoYCanoCima = random.randint(150, 400)
            posicaoYcanoBaixo = posicaoYCanoCima + espaco
            cano_pont = 0

        if passaro.colliderect(cano_cima) :
            jogando = 0
            cano_pont = 0
            bateu = 1

        if passaro.colliderect(cano_baixo) :
            jogando = 0
            cano_pont = 0
            bateu = 1

        if cano_pont == 0 :
            if posicaoXcano <= -50 :
                pontuacao += 1
                cano_pont = 1

    elif jogando == 0:

        mensagem_pont2 = fonte.render(f" de {pontuacao} pontos", True, cor_texto)

        if bateu == 1:
            screen.blit(mensagem_perder, (150, 300))
            screen.blit(mensagem_pont, (50, 400))
            screen.blit(mensagem_pont2, (150, 450))
            screen.blit(mensagem_rec, (60, 550))
            posicaoInicial = 300
            posicaoXcano = 550
            posicaoYcanoBaixo = posicaoYCanoCima + espaco

        if saiu_area == 1:
            screen.blit(mensagem_perder, (150, 300))
            screen.blit(mensagem_pont, (50, 400))
            screen.blit(mensagem_pont2, (150, 450))
            screen.blit(mensagem_rec, (60, 550))
            posicaoInicial = 300
            posicaoXcano = 550
            posicaoYcanoBaixo = posicaoYCanoCima + espaco
    
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()