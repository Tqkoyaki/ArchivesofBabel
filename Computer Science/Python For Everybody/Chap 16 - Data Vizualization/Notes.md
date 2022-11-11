### Visualizing Data
- The first issue is that the geocoding API is rate-limited. To solve this issue you can store the data retrieved in a sqlite database. This way if the same input is given, the input can be retrieved from the database instead of making a new API call.
- The geoload program reads the where.data and checks if it is stored in the database, if not it calls the API and stores the data in the database.
- There is also a counter to limit the number of API calls.
- You can visualize the data once it is in the database using the geodump program.
- The program writes the location, latitude, and longitude to a file called where.js.
- The where.html is used to see the locations on a browser.