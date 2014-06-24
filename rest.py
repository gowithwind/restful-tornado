import tornado.web
import re

map={}

def register(type,path):
	'''
	register a service
	'''
	def method(f):
		key=type.upper()+' '+path
		if not map.get(key):
			map[key]={'type':type.upper(),'pattern':re.compile(key),'method':f}
	return method

class RestHandler(tornado.web.RequestHandler):
	'''a simple restful handler'''
	def get(self):
		self._exe()
	def post(self):
		self._exe()
	def delete(self):
		self._exe()
	def put(self):
		self._exe()
	def _exe(self):
		request_path =self.request.method+' '+self.request.path
		try:
			for path in map:
				item=map.get(path)
				match=re.match(item['pattern'],request_path)
				if match:
					method=item['method']
					params= match.groups()
					result=method(*params)
					#print method.__name__,params,result
					self.write(result)
					break
		except:
			raise

