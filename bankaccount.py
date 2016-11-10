class BankAccount(object):
	"""docstring for BankAccount"""
	balance = 0
	def __init__(self, name):
		self.name = name
		
	def __repr__(self):
		return "The account belongs to %s, and the balance is %.2f." % (self.name, self.balance)

	def show_balance(self):
		print "Balance is %.2f." % self.balance

	def deposit(self, amount):
		if amount <= 0:
			print "Error"
			return
		else:
			print "Depositing amount: %.2f" % amount
			self.balance += amount
			self.show_balance()

	def withdraw(self, amount):
		if amount > self.balance:
			print "Error"
			return
		else:
			print "Withdrawing amount: %.2f" % amount
			self.balance -= amount
			self.show_balance()

my_account = BankAccount("Tom")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account