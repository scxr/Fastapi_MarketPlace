from generate_user_btc_address import BitcoinWallet, KeyGenerator
from bit import Key
kg = KeyGenerator()
kg.seed_input('test this fucking thing')
key = kg.generate_key()
address = Key('cd098e897c507fd8dd85844eeaa2461c4a26c91dba8f69153545c27d446bbcde')