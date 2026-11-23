import pygame
#tamaño de la ventana 
ANCHO = 1280
ALTO = 720
FPS = 60
COLOR_FONDO = (30, 30, 46)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Juego de cartas")
    reloj = pygame.time.Clock()

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        pantalla.fill(COLOR_FONDO)
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()