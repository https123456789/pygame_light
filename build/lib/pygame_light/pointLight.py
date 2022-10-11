from .lightSource import LightSource

class PointLight(LightSource):
	def __init__(self, pos, color, intensity):
		super().__init__(pos, color, intensity)