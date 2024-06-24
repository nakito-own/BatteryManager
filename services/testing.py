def has_common_repeated_chars(str1: str, str2: str) -> bool:
    def find_repeated_substrings(s: str, length: int) -> set:
        repeated_substrings = set()
        for i in range(len(s) - length + 1):
            if all(c == s[i] for c in s[i:i + length]):
                repeated_substrings.add(s[i:i + length])
        return repeated_substrings

    repeated_subs_str1 = find_repeated_substrings(str1, 4)
    repeated_subs_str2 = find_repeated_substrings(str2, 4)

    # Проверяем, есть ли пересечение множеств
    return not repeated_subs_str1.isdisjoint(repeated_subs_str2)

print(has_common_repeated_chars('Пресненская набережная, 10 с2', 'Пресненская'))