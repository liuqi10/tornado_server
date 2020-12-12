# -*- encoding: utf-8 -*-
"""
@File    : run_server.py
@Time    : 2020/8/12 0:14
@Author  : LIUQI
@Email   : 17611682976@163.com
@Softw
"""
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

settings = {
    "debug": True,
    "template_path": "templates",
    "static_path": "static"
}
define("port", default=8800, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class PoemPageHandler(tornado.web.RequestHandler):
    # def get(self):
    #     self.render('poem.html')
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                    difference=noun3)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler), (r'/poem', PoemPageHandler)],
        **settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
