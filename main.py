import webapp2
import caesar

form="""
<form method="get" action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hello World!"
        encrypted_message = caesar.encrypt(message, 13)
        self.response.write(message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
