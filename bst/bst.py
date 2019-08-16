#!/usr/bin/env python

class BST_node(object):

	def __init__(self):
		self.left = None
		self.right = None
		self.info = None

		
class BST_ops(object):
	
	def __init__(self):
		pass

	def maketree(self, val):
		bst_node = BST_node()
		bst_node.info = val

		return bst_node

	def setleft(self, bst, val):
		if bst == None:
			print('Null insertion')
		elif bst.left != None:
			print('Invalid insertion')
		else:
			bst.left = self.maketree(val)

		return bst

	def setright(self, bst, val):
		if bst == None:
			print('Null insertion')
		elif bst.right != None:
			print('Invalid insertion')
		else:
			bst.right = self.maketree(val)

		return bst

	def add_node(self, bst, val):
		p = q = bst

		while p.info != val and q != None:
			p = q
			
			if val > p.info:
				q = q.right
			elif val < p.info:
				q = q.left

		if p.info == val:
			print('Duplicate')
		elif val > p.info:
			self.setright(p, val)
		elif val < p.info:
			self.setleft(p, val)
	
	def intrav(self, bst):
			if bst == None:
				return

			print bst.info
			self.intrav(bst.left)
			self.intrav(bst.right)


if __name__ == '__main__':

	bst_ops = BST_ops()

	print('Input val')
	val = int(input())

	bst = bst_ops.maketree(val)

	while True:

		print('Input val')
		val = int(input())
	
		if val == -1:
			break

		bst_ops.add_node(bst, val)

	bst_ops.intrav(bst)
