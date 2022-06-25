import requests
import datetime
import time
# Codigo para enviar una imagen a firebase storage.
# Retorna el url que se debe pegar al PUT request de un ingreso por puerta trasera.
import requests
import os

import firebase_admin
from firebase_admin import credentials, storage

# Autenticarnos en Firebase
cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred,{'storageBucket':'cipasajeros.appspot.com'})
bucket = storage.bucket()


# Registrat 7 entradas traseras con fotos al servidor
url="https://us-central1-cipasajeros.cloudfunctions.net/app/api/vehiculos/testvehicule"

for i in range(4):
  now = int(datetime.datetime.now().timestamp())+(i*60+60)
  fileName = '%s.png' % str(now)
  os.rename('%s.png' % str(i+1),fileName)
  blob = bucket.blob(fileName)
  blob.upload_from_filename(fileName)
  blob.make_public()
  urlFoto = blob.public_url
  data = {
        "sensor": "atras",
        "tipoRegistro":"entradas",
        "registro":now,
        "urlFoto":urlFoto,
  }
  res = requests.put(url,data)
  print(res)
  time.sleep(3)

