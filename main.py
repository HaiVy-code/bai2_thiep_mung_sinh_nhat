from guizero import App, Text, Picture
cuaso = App("Thiep chuc mung", width = 700, height = 750)
chu = Text(cuaso, "Chuc Mung Sinh Nhat")
picture = Picture(cuaso, "banh sinh nhat.png")
chu2 = Text(cuaso, "Chuc ban co mot ngay sinh nhat tuyet voi!")
chu3 = Text(cuaso, "Tu Bui Duong Hai Vy")
cuaso.display()
