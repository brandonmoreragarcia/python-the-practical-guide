import functools

MINING_REWARD = 10
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}



def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    if not verify_transaction(transaction):
        print('Not enough funds!')
        return

    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)
    print('Transaction Successfull')


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)

    return True


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_tx_amount(payload, participant):
    return [[tx['amount'] for tx in block['transactions'] if tx[payload] == participant] for block in blockchain]

def get_balance(participant):
    tx_sender = get_tx_amount('sender', participant)
    tx_recipient = get_tx_amount('recipient', participant)
    tx_open_from_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(tx_open_from_sender)
    amount_sent = functools.reduce(lambda total, currentTx: total + currentTx[0] if len(currentTx) > 0 else 0, tx_sender, 0)
    # amount_sent = 0
    amount_received = functools.reduce(lambda total, currentTx: total + currentTx[0] if len(currentTx) > 0 else 0, tx_recipient, 0)
    # amount_received = 0

    # for tx in tx_sender:
    #     if len(tx) == 0:
    #         continue

    #     amount_sent += tx[0]
    
    # for tx in tx_recipient:
    #     if len(tx) == 0:
    #         continue

    #     amount_received += tx[0]
    

    return amount_received - amount_sent

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

def check_validity():
    return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check Transaction Validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print('participants: ', participants)
    elif user_choice == '5':
        if check_validity():
            print('all transactions are valid')
        else :
            print('there are invalid transactions!')

    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recepient': 'Max', 'amount': 100.0}]
}
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain() :
         print_blockchain_elements()
         print('Invalid blockchain!')
         break

    print('balance: ', get_balance('Max'))
    print(f'Balance of {owner}: {get_balance(owner)}')
else:
    print('User left!')


print('Done!')
