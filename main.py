# type: ignore
import os
from dotenv import load_dotenv
from poseidon.evm import Chain, Account, Contract, Utils

load_dotenv()

rpc_url = os.getenv("RPC_URL")
private_key = os.getenv("PRIVATE_KEY")
chain = Chain(rpc_url)
account = Account(chain, private_key)

account.send_transaction(to=account.address, data="0x", value=1)

Utils.set_solidity_version("0.8.28")
abi, bytecode = Utils.compile_solidity_contract("./contracts/Test.sol", "Test")
tx_receipt = account.deploy_contract(abi, bytecode)

contract: Contract = tx_receipt.contract
contract.read_only_call_function("readContent")
contract.call_function("writeContent", "test")
contract.read_only_call_function("readContent")
