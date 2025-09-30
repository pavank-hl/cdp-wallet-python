# CDP Wallet Python Demo

A comprehensive demonstration of the Coinbase Developer Platform (CDP) SDK for Python, showcasing wallet creation, transaction management, policies, gas sponsorship, and security best practices.

## Features

This demo application demonstrates:

1. **SDK Setup** - Secure configuration with environment variables
2. **Account Management** - Creating new and importing existing Ethereum accounts
3. **Transactions** - Sending transactions and fetching balances
4. **Policy Enforcement** - Attaching policies with failing/successful transaction examples
5. **Gas Sponsorship** - Enabling gasless transactions using Smart Accounts
6. **Secret Rotation** - Production security practices for credential management

## Prerequisites

- Python 3.8 or higher
- CDP API credentials (API Key ID, API Key Secret, Wallet Secret)
- Access to Base Sepolia testnet

## Installation

1. Clone this repository or download the files

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your CDP credentials:
```env
CDP_API_KEY_ID=your_api_key_id_here
CDP_API_KEY_SECRET=your_api_key_secret_here
CDP_WALLET_SECRET=your_wallet_secret_here
```

## Getting CDP Credentials

1. Visit the [CDP Portal](https://portal.cdp.coinbase.com)
2. Create a new project or select an existing one
3. Navigate to **Settings > API Keys**
4. Click **Create API Key**
5. Download the credentials and add them to your `.env` file

## Usage

Run the demo application:

```bash
python main.py
```

The application will execute all demonstrations in sequence:

### 1. SDK Setup
- Loads environment variables securely
- Initializes the CDP client
- Verifies credentials

### 2. Account Creation & Import
- Creates a new Ethereum account
- Demonstrates importing an existing account
- Shows account addresses and metadata

### 3. Transactions & Balances
- Requests testnet ETH from the CDP faucet
- Fetches account balances
- Sends a test transaction
- Shows updated balances after transaction

### 4. Policy Attachment
- Explains policy concepts
- Demonstrates a failing transaction (exceeds policy limits)
- Shows a successful transaction (within policy limits)
- Provides guidance on implementing real policies

### 5. Gas Sponsorship
- Creates a Smart Account (ERC-4337)
- Demonstrates gasless transactions
- Shows how paymasters cover gas fees
- Explains user operation flow

### 6. Secret Rotation
- Explains secret rotation importance
- Shows best practices for credential management
- Provides step-by-step rotation instructions
- Displays current secret status (masked)

## Project Structure

```
wallet-python/
├── main.py              # Main demo application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Key Concepts

### EVM Accounts
- Private/public key pairs for signing transactions
- Generated and stored in CDP's Trusted Execution Environment (TEE)
- Same address works across all EVM-compatible networks

### Smart Accounts
- ERC-4337 compliant smart contract wallets
- Enable account abstraction features
- Support gasless transactions via paymasters
- Allow batched operations

### Policies
- Control transaction permissions
- Set spending limits and allowed recipients
- Enforce security rules at the protocol level
- Managed via CDP Portal

### Gas Sponsorship
- Paymasters pay gas fees on behalf of users
- Users don't need native tokens for transactions
- Improves user experience significantly
- Requires Smart Account setup

## Networks Supported

This demo uses **Base Sepolia** testnet, but CDP supports:

- **Ethereum** (Mainnet & Sepolia)
- **Base** (Mainnet & Sepolia)
- **Polygon** (Mainnet & Amoy)
- **Arbitrum** (Mainnet & Sepolia)
- **Optimism** (Mainnet & Sepolia)
- **Avalanche** (Mainnet & Fuji)
- **Solana** (Mainnet & Devnet)

## Security Best Practices

1. **Never commit `.env` files** - Use `.gitignore`
2. **Rotate secrets regularly** - Every 90 days minimum
3. **Use secret management services** - AWS Secrets Manager, HashiCorp Vault, etc.
4. **Monitor API usage** - Check CDP Portal for unusual activity
5. **Implement policies** - Restrict transaction permissions
6. **Test on testnet first** - Always verify on testnet before mainnet

## Troubleshooting

### Faucet Requests Failing
- Check if you've exceeded daily limits
- Manually fund accounts via [Base Sepolia Faucet](https://www.coinbase.com/faucets/base-ethereum-sepolia-faucet)

### Transaction Errors
- Ensure account has sufficient balance
- Verify network is correct (base-sepolia)
- Check gas prices aren't too low

### Authentication Errors
- Verify all environment variables are set
- Check API key hasn't expired
- Ensure Wallet Secret is correctly formatted

## Resources

- [CDP Documentation](https://docs.cdp.coinbase.com)
- [CDP Portal](https://portal.cdp.coinbase.com)
- [CDP Python SDK](https://github.com/coinbase/cdp-sdk-python)
- [Base Sepolia Explorer](https://sepolia.basescan.org)
- [CDP Discord](https://discord.gg/cdp)

## API Reference

Key CDP SDK methods used in this demo:

```python
# Client initialization
cdp = CdpClient()

# Account management
account = await cdp.evm.create_account(name="my-account")
imported = await cdp.evm.import_account(private_key="0x...")

# Faucet
faucet = await cdp.evm.request_faucet(address="0x...", network="base-sepolia", token="eth")

# Balances
balances = await cdp.evm.list_token_balances(address="0x...", network="base-sepolia")

# Transactions
tx = await cdp.evm.send_transaction(
    address="0x...",
    network="base-sepolia",
    to="0x...",
    value="1000000000000000"
)

# Smart Accounts
smart_account = await cdp.evm.create_smart_account(
    owner_address="0x...",
    network="base-sepolia",
    name="my-smart-account"
)

# User Operations (gasless)
user_op = await cdp.evm.send_user_operation(
    smart_account_address="0x...",
    network="base-sepolia",
    calls=[{"to": "0x...", "value": "1000", "data": "0x"}]
)
```

## License

This demo is provided as-is for educational purposes.

## Support

For questions or issues:
- Check the [CDP Documentation](https://docs.cdp.coinbase.com)
- Join the [CDP Discord](https://discord.gg/cdp)
- Open an issue in this repository

---

Built with ❤️ using [Coinbase Developer Platform](https://www.coinbase.com/cloud)