def revstring(S):
    if S == " ":
        return ""
    return revstring(S[1:]) + S[0]

S= input()
print(revstring(S))