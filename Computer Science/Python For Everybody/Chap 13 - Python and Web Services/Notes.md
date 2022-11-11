### eXtensible Markup Language (XML)
- Each pair of opening and closing tags represents an element or node.
- Each element can have text, attributes, and other elements.
- If the element is empty, it may be depicted by a self-closing tag.
- Think of XML documents as having a tree structure.
```XML
<!-- Example of XML -->
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>
```
- You can use the xml.etree.ElementTree module to work with XML data. fromstring() takes a string and produces an XML tree.
- Use find() to look for a specific tag and .text after to get the text content.
- Use get() after find() to get the attribute value.
- Tripe ''' and """ are used to denote multi-line strings.
- You can use findall() to get a list of elements.

### JavaScript Object Notation (JSON)
- JSON is a very natural way to represent data in a programming language because it is a combination of lists and dictionaries.
- Python has a json module that takes a string and parses it into a Python object.
```python
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
```
- json.loads() takes a string and parses it into a Python object.
- json.dumps() takes a Python object and produces a string.

### Application Programming Interfaces (APIs)
- APIs are a set of protocols to help two software applications talk to each other.
- Usually there is a program that has a set of services and publishes an API to be used by other applications. The other applications use the API to access the services.
- Service-Oriented Architecture (SOA) is where the overall application makes use of services offered by other applications. A non-SOA application is where the overall application is a single program.
- It is quite common that you need an API key to make use of a vendor's API.
- Sometimes you can include the key as part of your POST data other times you need to send cryptographic signed messages using shared keys and secrets. A common way to do this is to use OAuth.
- There are many Oauth libraries for Python you can use.