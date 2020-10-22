from phue import Bridge
import time
bridge_ip = '999.999.69.999'



class HackingLights:
	def __init__(self, color1, color2, color3, saturation):
		self.color1 = color1
		self.color2 = color2
		self.color3 = color3
		self.saturation = saturation

	def access_lights(self, bridge_ip):
		b = Bridge(bridge_ip)
		light_name_list = b.get_light_objects('name')
		return light_name_list


	def christmas_mode(self):
		lights = self.access_lights(bridge_ip)
		while True:
			time.sleep(0.7)
			for light in lights:
				lights[light].on = True
				lights[light].hue = self.color1
				lights[light].saturation = self.saturation
			time.sleep(0.7)
			for light in lights:
				lights[light].on = True
				lights[light].hue = self.color2
				lights[light].saturation = self.saturation
			time.sleep(0.7)
			for light in lights:
				lights[light].on = True
				lights[light].hue = self.color3
				lights[light].saturation = self.saturation





