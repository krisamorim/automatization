# import os
# from PIL import Image, ExifTags
# os.chdir(os.path.dirname(__file__))

# # Carregar a imagem
# imagem = Image.open('down.jpg')

# # Tentar obter os metadados da imagem
# try:
#     for orientacao in ExifTags.TAGS.keys():
#         if ExifTags.TAGS[orientacao]=='Orientation':
#             break
#     exif = dict(imagem._getexif().items())

#     if exif[orientacao] == 3:
#         imagem = imagem.rotate(180, expand=True)
#     elif exif[orientacao] == 6:
#         imagem = imagem.rotate(270, expand=True)
#     elif exif[orientacao] == 8:
#         imagem = imagem.rotate(90, expand=True)
# except (AttributeError, KeyError, IndexError):
#     # Caso a imagem não tenha informações de orientação nos metadados
#     print("Não foram encontradas informações de orientação nos metadados da imagem.")

# # Salvar a imagem corrigida
# imagem.save('imagem_corrigida.jpg')






import cv2
import os
os.chdir(os.path.dirname(__file__))

a = os.path.dirname(__file__)+r'\hEmDeiMeta.jpg'

def detctar(caminho):
	# Carregar a imagem
	imagem = cv2.imread(caminho)

	# Obter as dimensões da imagem
	altura, largura = imagem.shape[:2]

	# Se a largura é maior que a altura, então a imagem pode estar rotacionada
	if largura > altura:
	    print("A imagem pode estar rotacionada.")
	else:
		print("A imagem parece estar na orientação correta.")

detctar(a)

# from PIL import Image
# from os import path
# import os
# a = path.dirname(__file__)+r'\a.jpg'
# image = Image.open(a)
# os.chdir(path.dirname(__file__))
# image.save('b.png')