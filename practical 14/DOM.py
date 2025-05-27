import xml.dom.minidom
import datetime
a = r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 14\go_obo.xml"
def dom_parse(Y):
    start_time = datetime.datetime.now()
    DOMTree = xml.dom.minidom.parse(Y)
    collection=DOMTree.documentElement
    terms=collection.getElementsByTagName("term")
    results={    'molecular_function': {'max_count': 0, 'term_id': ''},
        'biological_process': {'max_count': 0, 'term_id': ''},
        'cellular_component': {'max_count': 0, 'term_id': ''}
    }
    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].childNodes[0].data.strip()
        term_id=term.getElementsByTagName("id")[0].childNodes[0].data
        is_a_list=term.getElementsByTagName("is_a")
        count=len(is_a_list)
        if count > results[namespace]['max_count']:
                results[namespace]['max_count'] = count
                results[namespace]['term_id'] = term_id
    end_time=datetime.datetime.now()
    print(results, end_time-start_time) 
dom_parse(a)