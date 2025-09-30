"""
Utility functions for CDP Wallet operations
"""

import os
import asyncio
from dotenv import load_dotenv
from cdp import CdpClient

# Load environment variables
load_dotenv()

# Constants
NETWORK = "base-sepolia"

# Singleton CDP client instance
_cdp_instance = None


async def get_cdp_client() -> CdpClient:
    """
    Get or create a singleton CDP client instance
    """
    global _cdp_instance
    
    if _cdp_instance is None:
        # Verify environment variables
        api_key_id = os.getenv('CDP_API_KEY_ID')
        api_key_secret = os.getenv('CDP_API_KEY_SECRET')
        wallet_secret = os.getenv('CDP_WALLET_SECRET')
        
        if not all([api_key_id, api_key_secret, wallet_secret]):
            raise ValueError("Missing required environment variables. Please check your .env file.")
        
        _cdp_instance = CdpClient()
    
    return _cdp_instance


async def fund_account_from_faucet(address: str):
    """
    Request testnet funds from the CDP faucet
    """
    cdp = await get_cdp_client()
    
    try:
        await cdp.evm.request_faucet(
            address=address,
            network=NETWORK,
            token="eth"
        )
        await asyncio.sleep(10)  # Wait for funds to confirm
    except Exception as e:
        print(f"Faucet failed: {str(e)}")


async def fetch_balance(address: str):
    """
    Fetch and display the balance of an account
    """
    cdp = await get_cdp_client()
    
    try:
        balances = await cdp.evm.list_token_balances(
            address=address,
            network=NETWORK
        )
        
        if balances:
            balance_list = balances.balances if hasattr(balances, 'balances') else balances
            
            print(f"{address}:")
            for balance in balance_list:
                symbol = balance.token.symbol if hasattr(balance, 'token') else 'ETH'
                if hasattr(balance, 'amount') and hasattr(balance.amount, 'amount'):
                    amount = balance.amount.amount
                    decimals = balance.amount.decimals if hasattr(balance.amount, 'decimals') else 18
                    readable_amount = amount / (10 ** decimals)
                    print(f"  {symbol}: {readable_amount}")
        
        return balances
    except Exception as e:
        print(f"⚠ Balance fetch failed: {str(e)}")
        return None


async def close_cdp_client():
    """
    Close the CDP client connection
    """
    global _cdp_instance
    
    if _cdp_instance:
        await _cdp_instance.close()
        _cdp_instance = None