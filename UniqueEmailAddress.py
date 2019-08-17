from typing import *


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for i in emails:
            local, domain = i.split("@")
            newLocal = local.replace(".", "")
            if "+" in newLocal:
                newLocal = newLocal[:newLocal.index("+")]

            ans.add(newLocal + "@" + domain)

        return len(ans)