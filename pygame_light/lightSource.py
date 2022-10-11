class LightSource:
	def __init__(self, pos, color, intensity):
		self.pos = pos
		self.color = color
		self.intensity = intensity
	def generate_mesh_polygons(self):
		l = []
		ti = self.intensity
		while ti > 0:
			ps = [
				{
					"color": self.color,
					"points": [
						self.pos,
						[self.pos[0], self.pos[1] - ti],
						[self.pos[0] + ti, self.pos[1]]
					]
				},
				{
					"color": self.color,
					"points": [
						self.pos,
						[self.pos[0] + ti, self.pos[1]],
						[self.pos[0], self.pos[1] + ti]
					]
				},
				{
					"color": self.color,
					"points": [
						self.pos,
						[self.pos[0], self.pos[1] + ti],
						[self.pos[0] - ti, self.pos[1]]
					]
				},
				{
					"color": self.color,
					"points": [
						self.pos,
						[self.pos[0] - ti, self.pos[1]],
						[self.pos[0], self.pos[1] - ti]
					]
				}
			]
			l.append(ps)
			ti -= 1
		return l