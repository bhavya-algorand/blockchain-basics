import hashlib

# Helper function to calculate SHA256 hash
def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to validate a transaction in a Merkle Tree
def validate_transaction(transaction, merkle_root, merkle_path):
    """
    Validate a transaction using its Merkle Path.

    Args:
    - transaction (str): The transaction to validate.
    - merkle_root (str): The root hash of the Merkle Tree.
    - merkle_path (list): A list of tuples where each tuple contains:
      - The sibling hash.
      - A direction ('left' or 'right') indicating whether the sibling is on the left or right.

    Returns:
    - bool: True if the transaction is valid, False otherwise.
    """
    # Compute the hash of the transaction
    current_hash = sha256_hash(transaction)

    # Traverse the Merkle Path to compute the Merkle Root
    for sibling_hash, direction in merkle_path:
        if direction == 'left':
            current_hash = sha256_hash(sibling_hash + current_hash)
        elif direction == 'right':
            current_hash = sha256_hash(current_hash + sibling_hash)
        else:
            raise ValueError("Invalid direction in Merkle Path. Must be 'left' or 'right'.")

    # Compare the computed root with the given Merkle Root
    return current_hash == merkle_root

# Example Usage
if __name__ == "__main__":
    # Example transaction
    transaction = "Tx2: Bob pays Carol 5"

    # Example Merkle Root (calculated previously)
    merkle_root = "ee6d71f9ea5275db0f5663df61f0590fb99a0f8d452c9b97cf4a95ee1c3e0201"

    # Example Merkle Path for the transaction
    # Format: (sibling hash, direction)
    merkle_path = [
        ("6e9310005d4c5fe024aa49e3e9e02d214320c0ba7280f7fcc37a21384b903cde", "left"),
        ("231f5ac0c0f6f1139a5bff89d358620d85a0eaf767608d23f83a07e8479bc94c", "right")
    ]

    # Validate the transaction
    is_valid = validate_transaction(transaction, merkle_root, merkle_path)
    print("Is the transaction valid?", is_valid)
