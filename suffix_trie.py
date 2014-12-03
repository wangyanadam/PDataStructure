class SuffixNode:

	def __init__(self, suffix_link = None):
		self.children = {}
		if suffix_link is not None:
			self.suffix_link = suffix_link
		else:
			self.suffix_link = self

	def add_link(self, c, v):
		self.children[c] = v

def build_suffix_trie(s):

	assert len(s) > 0

	Root = SuffixNode()
	Longest = SuffixNode(Root)
	Root.add_link(s[0], Longest)

	if s[-1:] != "$":
		s = s + "$"

	for c in s[1:]:
		Current = Longest; Previous = None
		while c not in Current.children:	
			r1 = SuffixNode()
			Current.add_link(c, r1)

			if Previous is not None:
				Previous.suffix_link = r1

			Previous = r1
			Current = Current.suffix_link

		if (Current is Root) & (Current.children[c] is Previous):
			Previous.suffix_link = Root
		else:
			Previous.suffix_link = Current.children[c]
		Longest = Longest.children[c]

	return Root

def is_substring(r, s):

	if len(s) == 0:
		return True

	if r == None:
		return False

	Current = r
	for c in s[0:]:
		if c not in Current.children:
			return False
		Current = Current.children[c]

	return True

def is_suffix(r, s):

        if len(s) == 0:
                return True

        if r == None:
                return False

	if s[-1:] != "$":
                s = s + "$"

        Current = r
        for c in s[0:]:
                if c not in Current.children:
                        return False
                Current = Current.children[c]

	if len(Current.children) == 0:
		return True
        else:
		return False

def num_occurs(r, s):
	if len(s) == 0:
                return True

        if r == None:
                return False

        Current = r
        for c in s[0:]:
                if c not in Current.children:
                        return False
                Current = Current.children[c]

	return leaf_count(Current)

def leaf_count(r):
	
	if r == None:
		return 0

	if len(r.children) == 0:
		return 1

	sum = 0
	for v in r.children.values():
		sum += leaf_count(v)

	return sum
