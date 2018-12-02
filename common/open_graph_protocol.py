
translate_exceptions = {
	'og:image':'og:image:url'
}

def translate(path):
	return translate_exceptions.get(path,path)