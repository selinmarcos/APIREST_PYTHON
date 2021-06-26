import requests
#<CODIGO SCRAP0>
import pandas as pd
from os.path  import basename #Usamos nombre aleatorio

url0 = "https://www.radiotimes.com/technology/gaming/fortnite-spring-breakout-how-to-find-easter-eggs/"
urlPage="https://www.paginasiete.bo"
page = requests.get(url0)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
encabezado = soup.find("div", {"class":"template-article__header-main template-article__header-main--headline-led"}) #PARA REEMPLAZAR
#print(encabezado.text)
#subencabezado = soup.find("strong", {"class":"bajada"})
#print(subencabezado.text)
imagen = soup.find("img", {"class":"img-responsive"}).get('src') #Buscamos la imagen y extraemos el src
img = urlPage+imagen #concatemos con la url(algunas paginas no tienen la url completa)
# print(img)
Descargamos la imagen
nombreImagen= 'img1.jpg'
with open(basename(img), "wb") as f: #Tambien podemo usar basename(img) instead of nombreImagen si queremos un nombre aleatorio.
            f.write(requests.get(img).content)
            imgName = basename(img) #guardamos el nombre de la imagen en la variable imgName
cuerpo = soup.find("div", {"class":"template-article__post-content"})
cuerpo0 = str(cuerpo) #CONVERTIR A STRING
#cuerpo0 =  cuerpo.text
#print(cuerpo.text)
#</CODIGO SCRAP0>

import json
import base64

url = 'http://localhost:8080/scrapmaster/wp-json/wp/v2'
user = 'marcos'
password = 'ho8P gJTI uCMJ tTtg 6GOl VfWI'

creds = user + ':' + password
token = base64.b64encode(creds.encode())
header = {'Authorization': 'Basic ' +  token.decode('utf-8')}

#<CODIGO PARA INSERTAR IMAGEN>
media = {
    'file' : open (imgName, 'rb'), #traemos la variable imagen
    'caption' : 'caption image',
    'description' : 'first API image dude'
}
image = requests.post(url + '/media', headers=header, files=media)
imageURL =  str(json.loads(image.content)['source_url'])
#</CODIGO PARA INSERTAR IMAGEN>

post = {
    'title' : encabezado.text,
    'content' : '<!-- wp:paragraph -->'+ cuerpo0 + '<!-- /wp:paragraph -->''<!-- wp:image --><figure class="wp-block-image"><img src="'+ imageURL+'"></figure><!-- /wp:image -->',
    'status' : 'publish'
}
r = requests.post(url + '/posts', headers=header, json=post)
print (r)

