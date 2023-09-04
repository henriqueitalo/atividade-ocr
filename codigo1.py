import cv2
import numpy as np
import pytesseract
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Separando as informações necessárias

im0 = cv2.imread('fatura.jpg')
instalacao = im0[620:700, 560:910]
mes = im0[260:325, 1010:1350]
quantidade = im0[1050:1100, 900:970]
preco = im0[1050:1100, 1050:1250]

#Extraindo as informações

inst = pytesseract.image_to_string(instalacao)
ms = pytesseract.image_to_string(mes)
qnt = pytesseract.image_to_string(quantidade)
prc = pytesseract.image_to_string(preco)

#Organizando em tabela

indice = ['Campo','Instalação','Mês','Quantidade','Preço']
inf = ['Valor', inst, ms, qnt,prc]
tabela = pd.Series(inf, index=indice)
print(tabela)


