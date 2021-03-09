import argparse

class opts(object):
	def __init__(self):
		self.parser = argparse.ArgumentParser()
		
		self.parser.add_argument('--num_classes', default='80')
		self.parser.add_argument('--reg_offset', default='2')
		self.parser.add_argument('--wha', default='3')

		print(self.parser)
		args = self.parser.parse_args()
		print(args)

	def get_heads(self, opt):
		opt.heads = {"hm":opt.num_classes,
					"wha":opt.wha,
					"reg":opt.reg_offset}

		return opt

opt = opts()
# opt.get_heads(opt)
# print(opt.num_classes)
