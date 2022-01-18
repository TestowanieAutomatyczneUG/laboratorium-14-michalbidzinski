import re
class ISBN:


    def validate(s):
        d = re.findall(r'\d', s)
        if len(d) != 13:
            return False
        if not re.match(r'97[89](?:-\d+){3}-\d$', s):
            return False
        odd = [int(x) for x in d[::2]]
        even = [int(x) * 3 for x in d[1::2]]
        return (sum(odd) + sum(even)) % 10 == 0