import webapp2
import os
import jinja2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CssiPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>GoodBye, World!</h1>')




class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')

        template_dic = {"country": "usa",
                       "region_name": "north east",
                       "region_num": 121,
                       "url": "http://images.ny-pictures.com/photo2/m/29248_m.jpg",
                       "philly_pic": "http://www.philaenergy.org/wp-content/uploads/2017/06/header-campaign.png",
                       "city": ["new york","boston", "philadelphia"],
	               "message": "welcome to: "
                       }

        self.response.write(welcome_template.render(template_dic))

class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("hello from ShowMemeHandler")

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        firstname = self.request.get('firstname')
        lastname = self.request.get('lastname')
        Age = self.request.get('Age')
        webform_dict = {"fn": firstname, "ln": lastname, "Age": Age,}
        self.response.write(results_template.render(webform_dict))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/showresults', ShowMemeHandler)],
    
 debug=True)
