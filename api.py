class Api:
	def __init__(self):
		self.center = "text-align: center !important;"
	def use_bootstrap(self):
		return '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">'
	def send_tag(self, tag = "h1", content = "Hello World", centered = False, style_class = "#"):
		if centered:
			return f'<{tag} class="{style_class}" style="{self.center}">{content}</{tag}>'
		return f'<{tag} class="{style_class}">{content}</{tag}>'
	def send_link(self, link = "#", text = "My Link", centered = False, style_class = "#"):
		if centered:
			return f'<div style="text-align:center"><a href="{link}">{text}</a></div>'
		return f'<a href="{link}" class="{style_class}>{text}</a>'