#!/usr/bin/env python3
import os, secret, templates
import cgi, cgitb


def check_login(username, password):
    user, pwd = secret.username, secret.password
    if (username == user and password == pwd):
        return True
    else:
        return False


def check_cookie():
    if os.environ.get("HTTP_COOKIE"):
        return True
    else:
        return False


form = cgi.FieldStorage()
username, password = form.getvalue("username"), form.getvalue("password")
login_correct = check_login(username, password)
cookie_found = check_cookie()

if login_correct is True and cookie_found is False:
    print("Set-Cookie: %s=%s" % (username, password))

print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Second CGI Program</title>")
print("</head>")
print("<body>")
if login_correct is True and cookie_found is True:
    print(templates.secret_page(username, password))
    
elif login_correct is False:
    print(templates.after_login_incorrect())

print("</body>")
print("</html>")
