import xml.sax  
from datetime import datetime  
a=r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 14\go_obo.xml"
class GOHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        self.current_data = ""  
        self.namespace = ""    
        self.term_id = ""      
        self.is_a_count = 0    
        self.in_id = False     
        self.in_namespace = False 
        
        
        self.results = {
            'molecular_function': {'max_count': 0, 'term_id': ''},
            'biological_process': {'max_count': 0, 'term_id': ''},
            'cellular_component': {'max_count': 0, 'term_id': ''}
        }
    
    def startElement(self, tag, attributes):
        self.current_data = tag  
        
        
        if tag == "term":
            self.is_a_count = 0
            self.term_id = ""
            self.namespace = ""
        
        
        if tag == "id":
            self.in_id = True
            self.term_id = ""  
            
        if tag == "namespace":
            self.in_namespace = True
            self.namespace = ""  
    
    def characters(self, content):
        
        if self.in_id:
            self.term_id += content.strip()
            
        if self.in_namespace:
            self.namespace += content.strip()
    
    def endElement(self, tag):
        
        if tag == "is_a":
            self.is_a_count += 1
            
        
        elif tag == "term":
            if self.namespace in self.results:
                
                if self.is_a_count > self.results[self.namespace]['max_count']:
                    self.results[self.namespace]['max_count'] = self.is_a_count
                    self.results[self.namespace]['term_id'] = self.term_id
        
        
        if tag == "id":
            self.in_id = False
            
        if tag == "namespace":
            self.in_namespace = False
            
        self.current_data = ""

def sax_parser(xml_file):

    start_time = datetime.now()  
    
    
    handler = GOHandler()
    parser = xml.sax.make_parser()
    
   
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    

    parser.setContentHandler(handler)
    
    
    parser.parse(xml_file)
    
    end_time = datetime.now() 
    
    
    print("\nSAX result:")
    for ns, data in handler.results.items():
        print(f"{ns}: with most is_a is {data['term_id']}, the number is {data['max_count']}")
    print(f"SAX time: {end_time - start_time}")
    
    return handler.results, end_time - start_time
sax_parser(a)