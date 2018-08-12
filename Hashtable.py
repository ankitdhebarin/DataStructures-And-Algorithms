class HashTable():

	def __init__(self):
		self.size = 9
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self,key,data):

		'''
		Adding a key-value pair by calculating remainder division hashtable formula
		'''

		hashvalue = self.hashFunction(key,len(self.slots))
		
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data

		else: 
			
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data

			else:
				nextvalue = self.rehash(hashvalue,len(self.slots))

				while self.slots[nextvalue] != None and self.slots[nextvalue] != key:
					nextvalue = self.rehash(nextvalue,len(self.slots))

				if self.slots[nextvalue] == None:
					self.slots[nextvalue] = key
					self.data[nextvalue] = data

				else: 

					self.data[nextvalue] = data

	def hashFunction(self,key,size):
		return key % size

	
	def rehash(self,key,size):
		return (key+1) % size

	
	def get(self,key):
		
		'''
		Special Dunder __getitem__() will call get()
		'''

		startslot = self.hashFunction(key,len(self.slots))

  		data = None
  		stop = False
  		found = False
  		position = startslot

		while self.slots[position] != None and not found and not stop:

			if self.slots[position] == key:
				found = True
				data = self.data[position]

			else:
				position=self.rehash(position,len(self.slots))
       			if position == startslot:
           			stop = True
  		
  		return data

	def __getitem__(self,key):
		'''
		Special dunder
		'''
		return self.get(key)

	def __setitem__(self,key,data):
		'''
		Special dunder
		'''
		self.put(key,data)

H = HashTable()

H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

print(H.slots)
print(H.data)

print(H[17])