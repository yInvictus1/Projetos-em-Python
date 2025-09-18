import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600,400))
pygame.display.set_caption("Jogo da Cobrinha")

cobra=[(100,50)]
direcao = (10,0)
comida = (300,200)
pontuacao = 0
fonte = pygame.font.SysFont(None, 36)

def desenhar():
    tela.fill((0,0,0))
    for parte in cobra:
        pygame.draw.rect(tela, (0,255,0), (parte[0], parte[1], 10, 10))
    pygame.draw.rect(tela, (255,0,0), (*comida, 10, 10))
    texto = fonte.render(f"Pontos: {pontuacao}", True, (255,255,255))
    tela.blit(texto, (10, 10))
    pygame.display.update()

def gerar_comida():
    while True:
        nova = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
        if nova not in cobra:
            return nova

rodando = True
relogio = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao != (0,10):
                direcao = (0 , -10)
            elif evento.key == pygame.K_DOWN and direcao != (0,-10):
                direcao = (0 , 10)
            elif evento.key == pygame.K_LEFT and direcao != (10,0):
                direcao = (-10 , 0)
            elif evento.key == pygame.K_RIGHT and direcao != (-10,0):
                direcao = (10 , 0)

    nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])

    if (nova_cabeca[0] < 0 or nova_cabeca[0] >= 600 or
        nova_cabeca[1] < 0 or nova_cabeca[1] >= 400 or
        nova_cabeca in cobra):
        rodando = False
        continue

    cobra.insert(0, nova_cabeca)

    if nova_cabeca == comida:
        pontuacao += 1
        comida = gerar_comida()
    else:
        cobra.pop()

    desenhar()
    relogio.tick(15)

pygame.quit()