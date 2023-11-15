class env(Enum):
    dev = 1
    test = 2
    prod = 3

class timeframe(Enum):
    HISTORICAL = 1
    REALTIME = 2

class blockchain(Enum):
    eth = 1
    solana = 2
    bnb = 3
    polygon = 4
    aptos = 5
    arb = 6
    arb_nova = 7
    avax = 8
    base = 9
    bitcoin = 10
    celo = 11
    xrp = 12
    soroban = 13
    near = 14
    op = 15
    dot = 16
    poly_zk = 17
    scroll = 18
    stacks = 19
    zksync = 20
    
class ortege:
    
    def extract_chain(blockchain):
        print("Pedro to complete")
        
    def set_vm_type(blockchain):
        if blockchain == "eth":
            config["vm_type"] = "evm"
        elif blockchain == "solana":
            config["vm_type"] = "svm"
        elif blockchain == "bnb":
            config["vm_type"] = "evm"
        elif blockchain == "polygon":
            config["vm_type"] = "evm"
        elif blockchain == "aptos":
            config["vm_type"] = "move"
        elif blockchain == "arb":
            config["vm_type"] = "evm"
        elif blockchain == "arb_nova":
            config["vm_type"] = "evm"
        elif blockchain == "avax":
            config["vm_type"] = "evm"
        elif blockchain == "base":
            config["vm_type"] = "evm"
        elif blockchain == "bitcoin":
            config["vm_type"] = "utxo"
        elif blockchain == "celo":
            config["vm_type"] = "evm"
        elif blockchain == "xrp":
            config["vm_type"] = "custom"
        elif blockchain == "soroban":
            config["vm_type"] = "custom"
        elif blockchain == "near":
            config["vm_type"] = "custom"
        elif blockchain == "op":
            config["vm_type"] = "evm"
        elif blockchain == "dot":
            config["vm_type"] = "substrate"
        elif blockchain == "poly_zk":
            config["vm_type"] = "evm"
        elif blockchain == "stacks":
            config["vm_type"] = "custom"
        elif blockchain == "scroll":
            config["vm_type"] = "evm"
        else: #zksync
            config["vm_type"] = "evm"