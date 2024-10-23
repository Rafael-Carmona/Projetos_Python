import pygame
import os
import random

# Inicializa o Pygame
pygame.init()

# Configurações da Tela
LARGURA_TELA = 500
ALTURA_TELA = 800
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Carregamento de Imagens
IMG_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
IMG_PASSARO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png")))
IMG_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
IMG_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))

# Configurações do Jogo
GRAVIDADE = 0.5
IMPULSO_PULO = -9
ROTACAO_MAXIMA = 25
VELOCIDADE_ROTACAO = 20
TEMPO_ANIMACAO = 5

class Passaro:
    def __init__(self):
        self.imagem = IMG_PASSARO
        self.x = 230
        self.y = 350
        self.inclinacao = 0
        self.contagem_tick = 0
        self.velocidade = 0
        self.altura_inicial = self.y
        self.rotacao = 0

    def pular(self):
        self.velocidade = -2
        self.contagem_tick = 0
        self.altura_inicial = self.y

    def mover(self):
        self.contagem_tick += 1
        deslocamento = self.velocidade * self.contagem_tick + 0.5 * GRAVIDADE * self.contagem_tick ** 2

        if deslocamento >= 16:
            deslocamento = 16
        if deslocamento < 0:
            deslocamento -= 2

        self.y = self.y + deslocamento

        if deslocamento < 0 or self.y < self.altura_inicial + 50:
            if self.inclinacao < ROTACAO_MAXIMA:
                self.inclinacao = ROTACAO_MAXIMA
        else:
            if self.inclinacao > -90:
                self.inclinacao -= VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        self.rotacao = min(self.inclinacao, 90)
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.rotacao)
        novo_retangulo = imagem_rotacionada.get_rect(center=self.imagem.get_rect(topleft=(self.x, self.y)).center)
        tela.blit(imagem_rotacionada, novo_retangulo.topleft)

    def obter_mask(self):
        return pygame.mask.from_surface(self.imagem)

class Cano:
    ESPACO = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.topo = 0
        self.base = 0
        self.CANO_TOPO = pygame.transform.flip(IMG_CANO, False, True)
        self.CANO_BASE = IMG_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.topo = self.altura - self.CANO_TOPO.get_height()
        self.base = self.altura + self.ESPACO

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.topo))
        tela.blit(self.CANO_BASE, (self.x, self.base))

    def colidir(self, passaro):
        mascara_passaro = passaro.obter_mask()
        mascara_topo = pygame.mask.from_surface(self.CANO_TOPO)
        mascara_base = pygame.mask.from_surface(self.CANO_BASE)

        offset_topo = (self.x - passaro.x, self.topo - round(passaro.y))
        offset_base = (self.x - passaro.x, self.base - round(passaro.y))

        ponto_base = mascara_passaro.overlap(mascara_base, offset_base)
        ponto_topo = mascara_passaro.overlap(mascara_topo, offset_topo)

        if ponto_topo or ponto_base:
            return True

        return False

class Base:
    VELOCIDADE = 5
    LARGURA = IMG_BASE.get_width()
    IMG = IMG_BASE

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA

        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMG, (self.x1, self.y))
        tela.blit(self.IMG, (self.x2, self.y))

def desenhar_tela(tela, passaro, canos, base, pontuacao, tentativas):
    tela.blit(IMG_FUNDO, (0, 0))

    for cano in canos:
        cano.desenhar(tela)

    base.desenhar(tela)
    passaro.desenhar(tela)

    fonte = pygame.font.SysFont("comicsans", 35)
    rotulo_pontuacao = fonte.render(f"Pontuação: {pontuacao}", 1, (255, 255, 255))
    tela.blit(rotulo_pontuacao, (LARGURA_TELA - rotulo_pontuacao.get_width() - 10, 10))

    rotulo_tentativas = fonte.render(f"Tentativas: {tentativas}", 1, (255, 255, 255))
    tela.blit(rotulo_tentativas, (10, 10))

    pygame.display.update()

def principal():
    passaro = Passaro()
    base = Base(730)
    canos = [Cano(700)]
    relogio = pygame.time.Clock()
    pontuacao = 0
    tentativas = 1
    executando = True

    while executando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    passaro.pular()

        passaro.mover()
        base.mover()

        adicionar_cano = False
        remover = []
        for cano in canos:
            cano.mover()
            if cano.colidir(passaro):
                tentativas += 1
                executando = False

            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover.append(cano)

            if not cano.passou and cano.x < passaro.x:
                cano.passou = True
                adicionar_cano = True

        if adicionar_cano:
            pontuacao += 1
            canos.append(Cano(600))

        for r in remover:
            canos.remove(r)

        if passaro.y + passaro.imagem.get_height() >= 730:
            tentativas += 1
            executando = False

        desenhar_tela(TELA, passaro, canos, base, pontuacao, tentativas)

    principal()

if __name__ == "__main__":
    principal()
