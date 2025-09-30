
"""
Account creation and management
"""

from datetime import datetime
from eth_account import Account
from utils import get_cdp_client

# Hardcoded private key for Bob's account
BOB_PRIVATE_KEY = "0xb01fd5c36dc5d21e4e6ddeda1ea79183e483fd450d6a3077d47ede81d6319f17"


async def create_accounts():
    """
    Create Alice (new account) and Bob (imported account)
    Returns tuple of (alice, bob)
    """
    cdp = await get_cdp_client()
    
    # Create Alice - a new account
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    alice = await cdp.evm.get_account(name=f"demo-account-new-20251001002758")
    print(f"Alice: {alice.address}")
    
    # Import Bob - from private key
    bob_key = BOB_PRIVATE_KEY[2:] if BOB_PRIVATE_KEY.startswith('0x') else BOB_PRIVATE_KEY
    
    # Calculate the expected address from the private key
    eth_account = Account.from_key(BOB_PRIVATE_KEY)
    expected_address = eth_account.address
    
    try:
        bob = await cdp.evm.import_account(
            private_key=bob_key,
            name=f"bob-{timestamp}"
        )
        print(f"✓ Successfully imported Bob's account")
        print(f"Bob: {bob.address}")
    except Exception as e:
        # Check if this is a "key already exists" error (409)
        if "already_exists" in str(e) or "409" in str(e):
            print(f"ℹ Key already exists, retrieving existing account...")
            # Retrieve the existing account by address
            bob = await cdp.evm.get_account(address=expected_address)
            print(f"✓ Retrieved existing Bob's account")
            print(f"Bob: {bob.address}")
        else:
            # Re-raise unexpected errors
            raise
    
    return alice, bob