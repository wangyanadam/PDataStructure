from suffix_trie import * 

def __main__():
        bstr = input("base string: ")
	pstr = input("pattern string: ")
        suffix_tree_root = build_suffix_trie(bstr)

	print("substring? " + str(is_substring(suffix_tree_root, pstr)))
	print("suffix? " + str(is_suffix(suffix_tree_root, pstr)))
	print("#occurs? " + str(num_occurs(suffix_tree_root, pstr)))

if __name__ == "__main__":
        __main__()
