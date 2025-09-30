"""
Send transaction from Alice to Bob
"""

import asyncio
from cdp.evm_transaction_types import TransactionRequestEIP1559
from web3 import Web3
from utils import get_cdp_client, NETWORK


async def send_tokens(alice, bob, amount_eth: float = 0.001):
    """
    Send tokens from Alice to Bob
    
    Args:
        alice: The sender account
        bob: The recipient account
        amount_eth: Amount in ETH to send (default: 0.001)
    """
    cdp = await get_cdp_client()
    w3 = Web3()
    
    try:
        tx_response = await cdp.evm.send_transaction(
            address=alice.address,
            transaction=TransactionRequestEIP1559(
                to=bob.address,
                value=w3.to_wei(amount_eth, "ether"),
            ),
            network=NETWORK,
        )
        
        tx_hash = tx_response if isinstance(tx_response, str) else (
            tx_response.transaction_hash if hasattr(tx_response, 'transaction_hash') else str(tx_response)
        )
        
        print(f"Transaction: {tx_hash}")
        print(f"Explorer: https://sepolia.basescan.org/tx/{tx_hash}")
        
        await asyncio.sleep(5)
        
        return tx_hash
    except Exception as e:
        print(f"Transaction failed: {str(e)}")
        return None