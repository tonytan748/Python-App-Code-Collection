#coding:utf-8
from editablefactory import EditableFactory 
from editabletshirt import EditableTShirt 
class EditableTShirtFactory(EditableFactory):
	def createEditable(self,master):
		tshirt=EditableTShirt(master)
		return tshirt