#!/usr/bin/env python3
import os, json, templates


print("Content-Type: text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

# print(os.environ)
# json_obj = json.dumps(dict(os.environ), indent=4)
# print(json_obj)

'''
for param in os.environ.keys():
    if (param == "QUERY_STRING"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if (param == "HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
'''

print(templates.login_page())
