from lxml import objectify


def xml_reader(xmlFile, factory):
    with open(xmlFile, 'r', encoding='utf-8') as f:
        xml = f.read().encode('utf-8')
    root = objectify.fromstring(xml)
    for appt in root.getchildren():
        data = []
        for e in appt.getchildren():
            data.append(e.text)
        print(data)
        yield factory.create_product(data)
