from .lightSource import LightSource

class AmbientLight(LightSource):
	def __init__(self, scene, color, intensity):
		super().__init__((0, 0), color, intensity)
		self.scene = scene
	def generate_mesh_polygons(self):
		l = [
			[
				{
					"color": self.color,
					"points": [
						(0, 0),
						(self.scene.size[0], 0),
						self.scene.size,
						(0, self.scene.size[1])
					]
				}
			]
		]
		return l