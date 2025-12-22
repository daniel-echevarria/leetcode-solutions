class Solution:
    def maskPhoneNumber(self, phoneNumber):
        clean = "".join([n for n in phoneNumber if n.isnumeric()])
        local = clean[-10:]
        country = clean[:-10]
        mask = ""
        if country:
            mask += f"+{'*'*len(country)}-"
        mask += "***-***-"
        return mask + local[-4:]

    def maskEmail(self, email):
        email = email.lower()
        name, domain = email.split("@")
        return name[0] + "*****" + name[-1] + "@" + domain

    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            return self.maskEmail(s)
        else:
            return self.maskPhoneNumber(s)


st = "LeetCode@LeetCode.com"
st = "491(234)567-890"
s = Solution()
print(s.maskPII(st))
