The API can be accessed at http://yoursite/api

It is assumed that the API will be used in the following way (on the client side)
...this determines how the API is set up on the server side (in this software)

1.) User "taps a keg" or adds a beer type by inputting a beer name in the form
2.) Javascript in the form accesses http://yoursite/api/beers/?name=[user input]&format=json
3.) API returns subset of database, where values contain the [user input] string, to the client form for client choice
4.) When client completes a valid input, or chooses a choice from (3), the client backend does the following:
   a.) Reads http://yoursite/api/brewer/?id=[brewer id as determined by API results from (4)]&format=json and stores all brewer data in the client brewer table
   b.) Reads http://yoursite/api/beer-styles/?id=[beer-style id as determined by API results from (4)]&format=json and stores all beer-style data in the client beer-style table
   c.) Reads http://yoursite/api/pictures/?id=[picture id as determined by API results from (4)]&format=json and stores all picture data in the client picture table
      i.) It also fetches the picture file from the remote server, and stores it locally for the client

Potential issue is that client software currently requires existing brewer & beer-style entries before a particular beer type can be entered.
Workaround would be to either fetch all necessary data, populate the tables, and refresh the form OR
...change the client software to work based on the assumptions laid out here.