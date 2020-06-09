import xml.sax

# se crea un clase que me recorre una lista de auto y me devuelve sos nombre modelos y velocidad 

class XMLHandler(xml.sax.ContentHandler):

    def __init__(self):
        
        self.CurrentData =''
        self.model = ''
        self.speed = ''

    def startElement(self, tag,attr):
        self.CurrentData = tag 
        if tag == 'car':

            print ('CAR')
            name = attr['name']

            print('name',name)
    def endElement(self, name):
        if self.CurrentData == 'model':

            print('modelo ',self.model)

        elif self.CurrentData == 'speed':

            print('speed ',self.speed) 
        
        self.CurrentData = ''


    def characters(self, content):

        if self.CurrentData == 'model':


            self.model = content

        elif self.CurrentData == 'speed':

            self.speed = content

if __name__ == "__main__":

    parse = xml.sax.make_parser()

    parse.setFeature(xml.sax.handler.feature_namespaces,0)

    Handler = XMLHandler()

    parse.setContentHandler(Handler)

    parse.parse('simple.xml')            












        