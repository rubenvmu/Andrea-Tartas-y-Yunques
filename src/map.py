import pygame

class LabMap:
    def __init__(self, screen):
        # Cargar imagen original
        raw_map = pygame.image.load("assets/sprites/mapu.png").convert()

        # Obtener dimensiones de pantalla
        screen_width, screen_height = screen.get_size()

        # Escalar el mapa al tamaño de la ventana
        self.map_image = pygame.transform.scale(raw_map, (screen_width, screen_height))

        self.width = self.map_image.get_width()
        self.height = self.map_image.get_height()

    def draw(self, screen, player):
        # Como el mapa ya está ajustado, no necesitamos cámara
        screen.blit(self.map_image, (0, 0))
        player.cam_offset = (0, 0)