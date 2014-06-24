from rest import register,RestHandler
print RestHandler.__doc__
class FoodResource(object):
	'''demo resource'''
	@register('get','/food/(\w+)')
	def get(id):
		return 'food %s'%id
class ShopResource(object):
	'''demo resource'''
	@register('get','/shop')
	def list():
		return 'shop list'
	@register('get','/shop/(\w+)/food')
	def shop_foods(id):
		return 'shop %s food list'%id
	@register('get','/shop/(\w+)')
	def get(id):
		return 'shop %s'%id
	@register('delete','/shop/(\w+)')
	def delete(id):
		return 'delete shop %s'%id
class OrderResource(object):
	'''demo resource'''
	@register('get','/order/(\w+)')
	def get(id):
		return 'order %s'%id
	@register('get','/order')
	def list():
		return 'order list'

import tornado.httpserver
import tornado.ioloop
if __name__ == '__main__':
	http_server = tornado.httpserver.HTTPServer(tornado.web.Application([('.*',RestHandler)],debug=True))
	http_server.listen(1234)
	tornado.ioloop.IOLoop.instance().start()