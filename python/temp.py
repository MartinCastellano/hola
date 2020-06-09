#!python3
import io
import wx

imagen = wx.Image()
imagen.LoadFile('imagen.png')

# Tal vez procesarla...
# Y ahora guardar el resultado en memoria

f = io.BytesIO()
imagen.SaveFile(f, wx.BITMAP_TYPE_PNG)

# Los bytes los tenemos aqui:
data = f.getvalue()

# Comprobación de que la cosa va bien
print(data[:10])