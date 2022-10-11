import pygame

class Scene:
	def __init__(self, size):
		if not pygame.get_init():
			raise ValueError("You need to initialize pygame first.")
		self.size = size
		self.lights = []
		self.surface = pygame.Surface(size, pygame.SRCALPHA)
		self.surface.fill((0, 0, 0))
	def add_light(self, light):
		self.lights.append(light)
	def update(self):
		self.surface.fill((0, 0, 0))
		for light in self.lights:
			polys = light.generate_mesh_polygons()
			for poly_layer in polys:
				for poly in poly_layer:
					pygame.draw.polygon(self.surface, poly["color"], poly["points"])
			#pygame.draw.circle(self.surface, light.color, light.pos, light.intensity)
	def draw_onto(self, surface):
		surface.blit(self.surface, (0, 0, self.size[0], self.size[1]), special_flags = pygame.BLEND_MULT)