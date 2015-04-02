#coding:utf-8
from editablefactory import EditableFactory 
from editablesafetyshoes import EditableSafetyShoes 
class EditableSafetyShoesFactory(EditableFactory):
	def createEditable(self,master):
		safetyshoes=EditableSafetyShoes(master)
		return  safetyshoes
