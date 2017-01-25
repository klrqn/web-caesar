import webapp2
import caesar


class MainHandler(webapp2.RequestHandler):

    def get(self):
        message = "Helloooo World!"
        encrypted_message = caesar.encrypt(message, 13)
        encrypted_line = "<textarea style='width:60%;height:15%'>" + encrypted_message + "</textarea>"
        submit = "<input type='submit'/>"
        form = "<form>" + encrypted_line + "<br>" + submit + "</form>"
        self.response.write(form)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
