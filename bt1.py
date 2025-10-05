from guizero import App, Text, Picture
cuaso = App("Thiep moi", width = 1200, height = 700, bg = "#FF7B7B")
chu = Text(cuaso, "Moi ban den du le hoi Tet Trung Thu", color = "yellow")
picture = Picture(cuaso, "tet trung thu.png")
chu2 = Text(cuaso, "Tu Bui Duong Hai Vy", color = "yellow")
cuaso.display()
