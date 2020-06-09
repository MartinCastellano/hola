import pandas as pd 
import xml.etree.ElementTree as et 

import xml.sax


def intr_docs(xml_doc):
    att =xml_doc.attrib


    for xml in xml_doc.iter('breakfast_menu'):

        doc_dict = att.copy()
        doc_dict.update(xml.attrib)
        doc_dict['food'] = xml.text 

        yield doc_dict

etree = et.parse('simple.xml')
doc_df = pd.DataFrame(list(intr_docs(etree.getroot())))

print(doc_df.iloc[0,:])