import pygame

# We need to init pygame before the import
pygame.init()

import pygame_light

# Make the window
window = pygame.display.set_mode((200, 200))

# Create the scene
lightScene = pygame_light.Scene((200, 200))

# Create the ambient light
ambientLight = pygame_light.AmbientLight(lightScene, (200, 200, 200), 1)

# Create the point lights
light1 = pygame_light.PointLight((50, 50), (255, 255, 255), 5)
light2 = pygame_light.PointLight((150, 5), (255, 255, 255), 15)

# Add the lights to the scene
lightScene.add_light(ambientLight)
lightScene.add_light(light1)
lightScene.add_light(light2)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			break
	# Update light scene
	lightScene.update()
	window.fill((255, 255, 255))
	# Draw the light scene onto the window
	lightScene.draw_onto(window)
	pygame.display.flip()