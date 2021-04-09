class Biodata():
	"""docstring for Biodata"""
	def __init__(self, nama, alamat, hobi, jk, kelas, pesan, kesan):
		self.nama = nama
		self.alamat = alamat
		self.hobi = hobi
		self.jk = jk
		self.kelas = kelas
		self.pesan = pesan
		self.kesan = kesan
	# get data nama
	def getNama(self):
		return self.nama

	# get data alamat
	def getAlamat(self):
		return self.alamat

	# get data hobi
	def getHobi(self):
		return self.hobi

	# get data jenis kelamin
	def getJk(self):
		return self.jk

	# get data kelas
	def getKelas(self):
		return self.kelas

	# get data pesan
	def getPesan(self):
		return self.pesan

	# get data kesan
	def getKesan(self):
		return self.kesan
