### What is "serialization" when we are talking about web services?
a) The act of taking data stored in a program and formatting it so it can be sent across the network

### What is the name of the Python library to parse XML data?
a) xml.etree.ElementTree

### Which of the following are not commonly used serialization formats?
[x] TCP
[] XML
[] JSON
[x] HTTP
[x] Dictionaries

### What is the method to cause Python to parse XML that is stored in a string?
b) fromstring()

### In this XML, which are the "complex elements"? 
```XML
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>
```
[] phone
[x] people
[x] person
[] Noah
[] name

### In this XML, which are the "simple elements"?
```XML
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>
```
[x] phone
[] people
[] person
[] Noah
[x] name

### In the following XML, which are attributes? 
```XML
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
```
[] name
[x] type
[x] hide
[] email
[] person

### In the following XML, which node is the parent node of node e
```XML
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```
a) c

### Looking at the following XML, what text value would we find at path "/a/c/e"
```XML
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```
b) Z

### What is the purpose of XML Schema?
a) To establish a contract as to what is valid XML

### If you were building an XML Schema and wanted to limit the values allowed in an xs:string field to only those in a particular list, what XML tag would you use in your XML Schema definition?
b) xs:enumeration

### For this XML Schema:
```XML
<xs:complexType name=”person”>
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:integer"/>
    <xs:element name="dateborn" type="xs:date"/>
  </xs:sequence>
</xs:complexType>
```
### And this XML,
```XML
<person>
   <lastname>Severance</lastname>
   <Age>17</Age>
   <dateborn>2001-04-17</dateborn>
</person>
```
### Which tag is incorrect?
b) Age

### What does the "Z" mean in this representation of a time: 
```
2002-05-30T09:30:10Z
```
a) This time is in the UTC timezone

### What is a good time zone to use when computers are exchanging data over APIs?
a) Universal Time / GMT

### Which of the following dates is in ISO8601 format?
a) 2002-05-30T09:30:10Z