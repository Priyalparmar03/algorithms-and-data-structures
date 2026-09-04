from solution import group_anagrams


def test_standard_case():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    grouped = sorted(sorted(g) for g in result)
    expected = sorted(sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert grouped == expected


def test_empty_string():
    assert sorted(group_anagrams([""])) == [[""]]


def test_single_word():
    assert group_anagrams(["abc"]) == [["abc"]]
