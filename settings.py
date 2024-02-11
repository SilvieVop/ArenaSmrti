# Hokus Pokus - zadala jsem Chatgpt aby mi vykreslil musketyry a carodeje spolu :D
# nevím jestli se to dobře zobrazuje a vidím dvě červená kolečka a tři modré čtverečky

# from PIL import Image, ImageDraw
#
# # Vytvoření nového obrázku s bílým pozadím
# image_width = 400
# image_height = 200
# background_color = (255, 255, 255)  # Bílá barva
# image = Image.new("RGB", (image_width, image_height), background_color)
#
# # Vytvoření objektu pro kreslení na obrázku
# draw = ImageDraw.Draw(image)
#
# # Koordináty postav musketyrů
# musketeer1_x, musketeer1_y = 50, 100
# musketeer2_x, musketeer2_y = 150, 100
# musketeer3_x, musketeer3_y = 250, 100
#
# # Koordináty postav čarodějů
# wizard1_x, wizard1_y = 100, 50
# wizard2_x, wizard2_y = 300, 50
#
# # Kreslení postav musketyrů (jednoduché obdélníky)
# musketeer_size = 40
# draw.rectangle([musketeer1_x, musketeer1_y, musketeer1_x + musketeer_size, musketeer1_y + musketeer_size], fill="blue")
# draw.rectangle([musketeer2_x, musketeer2_y, musketeer2_x + musketeer_size, musketeer2_y + musketeer_size], fill="blue")
# draw.rectangle([musketeer3_x, musketeer3_y, musketeer3_x + musketeer_size, musketeer3_y + musketeer_size], fill="blue")
#
# # Kreslení postav čarodějů (kruhy)
# wizard_radius = 20
# draw.ellipse([wizard1_x - wizard_radius, wizard1_y - wizard_radius, wizard1_x + wizard_radius, wizard1_y + wizard_radius], fill="red")
# draw.ellipse([wizard2_x - wizard_radius, wizard2_y - wizard_radius, wizard2_x + wizard_radius, wizard2_y + wizard_radius], fill="red")
#
# # Uložení vytvořeného obrázku
# image.save("characters.png")
#
# # Zobrazení vytvořeného obrázku
# image.show()
#
