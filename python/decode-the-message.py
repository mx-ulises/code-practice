class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapper = {' ': ' '}
        i = ord('a')
        for c in key:
            if c not in mapper:
                mapper[c] = chr(i)
                i += 1
        decoded_message = []
        for c in message:
            decoded_message.append(mapper[c])
        return "".join(decoded_message)
