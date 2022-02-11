import tornado.web 
import tornado.ioloop 


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hola!")
    def post(self):
        self.write("Hello")
   
application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
