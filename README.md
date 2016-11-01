Rest API
=======

Make HTTP requests from a client

Usage
-----

### Making a basic request: ###

```API
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/sort?array=34,7,8,9,1
```
In this example, the rest api takes an argument of "array" which is a string data type by using either GET or POST HTTP verbs. Then the results are returned as plain text in JSON format
```Result
HTTP/1.1 200 OK
Date: Mon, 31 Oct 2016 17:23:48 GMT
Server: Apache/2.4.18 (Ubuntu)
Content-Length: 24
Content-Type: application/json

{"result":[1,7,8,9,34]}

```
```API
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/prime?number=17
```
```Result
HTTP/1.1 200 OK
Date: Mon, 31 Oct 2016 18:52:33 GMT
Server: Apache/2.4.18 (Ubuntu)
Content-Length: 26
Content-Type: application/json

{"result":"Prime Number"}
```
