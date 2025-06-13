
def is_subsequence(source: str, target: str) -> bool:

    if target == "":
        return True

    if len(source) < len(target): 
        return False

    t_idx = 0
    for s_idx in range(len(source)):
        # print(f"j: {s_idx} {source[s_idx]}")
        if source[s_idx] == target[t_idx]:
            t_idx += 1
            if t_idx == len(target):
                return True
            # print(f"i: {t_idx} {target[t_idx]}")
    return False

# Example usage:
def test_subsequence():
    assert is_subsequence("abcde", "ace") == True
    assert is_subsequence("abcde", "aec") == False
    assert is_subsequence("abc", "abcd") == False
    assert is_subsequence("", "") == True
    print("All test cases passed!")

if __name__ == "__main__":
    test_subsequence()
