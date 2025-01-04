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
    transaction = "Tx2: Bhavya pays Aasritha 500"

    # Example Merkle Root (calculated previously)
    merkle_root = "f78c3c0cea02203ae1c58cfa4294eba3e475cd3956550f2ca0481fcceecf176a"

    # Example Merkle Path for the transaction
    # Format: (sibling hash, direction)
    merkle_path = [
        ("9889a8ffda9c5f9d6788f02253f2947bb5e2d13f4d51abb91f6755f1251cb3d8", "left"),
        ("525495b835308cad5bad4dc0ed6210375afeace36951ca62316223837aaa31c7", "right")
    ]

    # Validate the transaction
    is_valid = validate_transaction(transaction, merkle_root, merkle_path)
    print("Is the transaction valid?", is_valid)
