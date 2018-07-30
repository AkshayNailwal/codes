def tr(A,B):
	if A==None:
		return []
	if A.right==None and A.left==None and B==A.val:
		return [[A.val]]
	elif A.right==None and A.left==None and B!=A.val:
		return []
	l_subtree=tr(A.left,B-A.val)
	r_subtree=tr(A.right,B-A.val)
	subtree=l_subtree+r_subtree
        
	for i in subtree:
		i.insert(0,A.val)
	return subtree
