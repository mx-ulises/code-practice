class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_address = "[.]".join(address.split("."))
        return defanged_address
