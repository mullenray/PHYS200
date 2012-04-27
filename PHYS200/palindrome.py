def first(word):
	return word[0]
	
def last(word):
	return word[-1]
	
def middle(word):
	return word[1:-1]
	
def is_palindrome(word):
    if len(word)<3:
        return False
    elif len(word)==3 and first(word)==last(word):
        return True
    elif len(word)==3 and first(word)!=last(word):
        return False
    elif first(word)==last(word):
        return is_palindrome(middle(word))
    else:
        return False
