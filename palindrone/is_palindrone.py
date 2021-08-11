def is_palindrone(s: str) -> bool:
    # return input == input[::-1]
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# def longest_palindrone(s: str) -> str:
#     res = ""
#     for i in range(len(s) - 1):
#         step, cur = 1, s[i]
#         while is_palindrone(cur) and i - step >= 0 and i + step < len(s) - 1:
#             if len(cur) > len(res):
#                 res = cur
#             cur = s[i-step] + cur + s[i+step]
#             step += 1

#         step, cur = 1, ""
#         while is_palindrone(cur) and i - step >= -1 and i + step < len(s) - 1:
#             if len(cur) > len(res):
#                 res = cur
#             cur = s[i] + cur + s[i+step]
#             step += 1
        
#     return res


def longest_palindrone(s: str) -> int:
    if not s: return ""
    if len(s) == 1: return s

    res = s[0]
    for i in range(len(s) - 1):
        step, cur = 1, s[i]
        while i - step >= 0 and (i + step) <= (len(s) - 1):
            cur = s[i-step] + cur + s[i+step]
            step += 1
            if not is_palindrone(cur):
                break
            if len(cur) > len(res):
                res = cur

        step, cur = 0, ""
        while i - step >= 0 and (i + step) <= (len(s) - 1):
            cur = s[i-step] + cur + s[i+step+1]
            step += 1
            if not is_palindrone(cur):
                break
            if len(cur) > len(res):
                res = cur
        
    return len(res)


print(longest_palindrone("avkesekjhkj"))
print(longest_palindrone("foobar"))
print(longest_palindrone("ovo"))
