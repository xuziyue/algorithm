def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    else:
        older = countAndSay(n - 1) 
        result = ""
        index = 0
        count = 1
        while index < len(older):
            if index != len(older) - 1:
                if older[index] == older[index + 1]:
                    count += 1
                else:
                    result += str(count) + older[index]
                    count = 1
            else:
                result += str(count) + older[index]
            index += 1
        return result