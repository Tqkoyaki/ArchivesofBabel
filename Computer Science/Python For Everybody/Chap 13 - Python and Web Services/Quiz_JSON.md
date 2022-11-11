### Who is credited with getting the JSON movement started?
a) Douglas Crockford

### Who is credited with the REST approach to web services?
a) Roy Fielding

### What Python library do you have to import to parse and handle JSON?
a) import json

### Which of the following is true about an API?
a) An API is a contract that defines how to use a software library

### What is the method used to parse a string containing JSON data so that you can work with the data in Python?
a) json.loads()

### Which of the following is a web services approach used by the Twitter API?
a) REST

### What kind of variable will you get in Python when the following JSON is parsed:
```
[ "Glenn", "Sally", "Jen" ]
```
a) A list with three items

### What kind of variable will you get in Python when the following JSON is parsed:
```
\{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
\}
```
a) A dictionary with three key/value pairs

### Which of the following is not true about the service-oriented approach?
a) An application runs together all in one place

### If the following JSON were parsed and put into the variable x,
```
\{
    "users": [
        \{
            "status": \{
                "text": "@jazzychad I just bought one .__.",
             \},
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver",
         \},
   ...
```
### what Python code would extract "Leah Culver" from the JSON?
a) x["users"][0]["name"]

### Which of these two web service approaches is preferred in most modern service-oriented applications?
a) REST - Representational State Transfer

### What library call do you make to append properly encoded parameters to the end of a URL like the following: 
```
http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI
```
a) urllib.parse.urlencode()

### What happens when you exceed the Google geocoding API rate limit?
a) You cannot use the API for 24 hours

### What protocol does Twitter use to protect its API?
c) OAuth

### What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?
a) x-rate-limit-remaining