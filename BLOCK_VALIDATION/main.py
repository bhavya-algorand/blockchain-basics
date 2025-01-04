import hashlib

# Helper function to calculate SHA256 hash
def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Example transaction structure
transactions = [
    {"sender": "Ram", "receiver": "Krishna", "amount": 10},
    {"sender": "Sandeep", "receiver": "Narendra", "amount": 5},
    {"sender": "Satish", "receiver": "Gopal", "amount": 2},
]

class Block:
    def __init__(self, block_number, previous_hash, transactions, difficulty=4):
        self.block_number = block_number
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = self.compute_merkle_root()
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    # Compute Merkle Root
    def compute_merkle_root(self):
        current_level = [sha256_hash(str(tx)) for tx in self.transactions]
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else current_level[i]
                next_level.append(sha256_hash(left + right))
            current_level = next_level
        return current_level[0]

    # Mining block using Proof of Work
    def mine_block(self):
        target = "0" * self.difficulty
        while True:
            block_data = f"{self.block_number}{self.previous_hash}{self.merkle_root}{self.nonce}"
            block_hash = sha256_hash(block_data)
            if block_hash.startswith(target):
                return block_hash
            self.nonce += 1

# Validate a block
def validate_block(block, previous_block):
    # Check hash consistency
    recalculated_hash = sha256_hash(
        f"{block.block_number}{block.previous_hash}{block.merkle_root}{block.nonce}"
    )
    if recalculated_hash != block.hash:
        return False

    # Check Merkle Root consistency
    if block.merkle_root != block.compute_merkle_root():
        return False

    # Check previous hash link
    if block.previous_hash != previous_block.hash:
        return False

    # Proof of Work validation
    if not block.hash.startswith("0" * block.difficulty):
        return False

    return True

# Simulate the blockchain
if __name__ == "__main__":
    # Genesis block
    genesis_block = Block(0, "0", transactions)
    print("Genesis Block Mined:", genesis_block.hash)

    # Next block
    next_transactions = [
        {"sender": "Jashwanth", "receiver": "Punesh", "amount": 15},
        {"sender": "Akash", "receiver": "Satish", "amount": 8},
    ]
    next_block_1 = Block(1, genesis_block.hash, next_transactions)
    print("Next Block Mined:", next_block_1.hash)

    # Validate blocks
    print("Is Next Block Valid?", validate_block(next_block_1, genesis_block))

    # Next block
    next_transactions = [
        {"sender": "Satish", "receiver": "Narendra", "amount": 19},
        {"sender": "Nikhil", "receiver": "Rahul", "amount": 12},
    ]
    next_block_2 = Block(2, next_block_1.hash, next_transactions)
    print("Next Block Mined:", next_block_2.hash)

    # Validate blocks
    print("Is Next Block Valid?", validate_block(next_block_2, next_block_1))
