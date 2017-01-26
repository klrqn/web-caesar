import webapp2
import caesar
import cgi

def build_page(textAreaContent):
    # message variables
    mes_label = '<label>What would you like to encrypt: </label><br>'
    textArea = "<textarea name='message' style='width:40%;height:15%'>"+textAreaContent+"</textarea>"
    # rotation variables
    rot_label = '<label>By how many would you like to rotate:</label>'
    rotation_input = "<input name='rotation' type='number' style='margin-left:2em; width:50px'/>"
    # submit button
    submit = "<input type='submit'/>"

    # form action=which page it goes to
    # form method=get or post
    form = "<form action='.' method='post'>" + mes_label + textArea + "<br><br>" + rot_label + rotation_input + "<br><br>" + submit + "</form>"

    header = "<h2>Web Caesar</h2>"

    return header + form

class MainHandler(webapp2.RequestHandler):

    # initial build page of '/'
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        if self.request.get("rotation") == '':
            rotation = 0
        else:
            rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_encrypted = cgi.escape(encrypted_message)
        content = build_page(escaped_encrypted)

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
