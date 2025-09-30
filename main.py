"""
CDP Wallet Python Demo
======================
Main orchestration file that demonstrates:
1. Creating accounts (Alice and Bob)
2. Funding accounts
3. Sending transactions between accounts
"""

import asyncio
from accounts import create_accounts
from send_transaction import send_tokens
from utils import fund_account_from_faucet, fetch_balance, close_cdp_client


async def main():
    """
    Main orchestration function
    """
    try:
        # Create accounts
        alice, bob = await create_accounts()
        
        # Fund Alice
        # await fund_account_from_faucet(alice.address)
        
        # Initial balances
        print("\nInitial Balances:")
        await fetch_balance(alice.address)
        await fetch_balance(bob.address)
        
        # Send transaction
        print("\nSending Transaction:")
        await send_tokens(alice, bob, amount_eth=0.001)
        
        # Final balances
        print("\nFinal Balances:")
        await fetch_balance(alice.address)
        await fetch_balance(bob.address)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        await close_cdp_client()


if __name__ == "__main__":
    asyncio.run(main())