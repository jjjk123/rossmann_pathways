import pickle, zlib, os
from functools import partial

cachedir = "./cache/"

FORCE = False

class cache(object):
	def __get__(self, obj, objtype):
	
		"""
		docs: https://stackoverflow.com/questions/48982832/understanding-a-technique-to-make-class-based-decorators-support-instance-method
		
		self.method = True
		return partial(self.__call__, obj)
		"""
		pass

	def __init__(self, func):
		self.func = func
		self.method = False
		self.verb = False

	def __call__(self, *args, **kw):
		#if self.method:
		#	keyraw = [str(args[0].__class__)]+list(args[1:])
		#else:
		
		keyraw = list(args)
		keyraw += kw.values()
					
		key = self.func.__name__+"_"+str(zlib.crc32(str.encode(str(keyraw))))
		file_name = os.path.join(cachedir, key)
	
		if os.path.isfile(file_name):
			data = pickle.load(open(file_name, 'rb'))
			if self.verb: print ('data for', self.func.__name__, 'read from cache')
			return data 
		else:
			value = self.func(*args, **kw)
			if self.verb: print ('data for', self.func.__name__, 'written to cache')
			pickle.dump(value, open(file_name, 'wb'))
			return value


