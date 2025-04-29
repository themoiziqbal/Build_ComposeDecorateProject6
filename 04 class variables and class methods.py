# Class variables and class methods

# The program creates instances of a class Bank
# Then the program changes the name of the bank
# Then it displays that all instances have been affected

class Bank:
    name : str = "MCB"
    def __init__(self,branch : str):
        self.branch = branch
    
    @classmethod
    def change_bank_name(cls,name : str):
        cls.name = name

def main():
    # Create three branches of MCB bank as follows:
    # * Chorangi
    # * Gali
    # * Highway
    banks : list[Bank] = []
    for branch in ['Chorangi','Gali','Highway']:
        banks.append(Bank(branch))

    for bank in banks:
        print(f"{Bank.name} Bank branch: {bank.branch}")

    # Change bank name to 'UBL'
    Bank.change_bank_name('UBL')

    # Show that all banks have their bank name changed
    for bank in banks:
        print(f"{Bank.name} Bank branch: {bank.branch}")

if __name__ == '__main__':
    main()