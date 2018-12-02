import requests
from lxml import html
from collections import defaultdict
from open_graph_protocol import translate

def nested_set(working_dict, keys, value):
	for key in keys[:-1]:
		if key not in working_dict:
			working_dict[key] = {}
		working_dict = working_dict[key]
	key = keys[-1]
	if key in working_dict:
		old_value = working_dict[key]
		old_value_type = type(old_value)
		if any( old_value_type == value_type for value_type in value_types ):
			working_dict[key] = [old_value,value]
		elif old_value_type == list:
			working_dict[key].append(value)
		else:
			raise NotImplementedError('Data type unexpected')
	else:
		working_dict[key] = value

value_types = [str,int,float]

def get_graph_data(source_html):
	mydoc = html.fromstring(source_html)
	data = dict()
	for meta in mydoc.xpath('.//meta'):
		if 'property' in meta.attrib and meta.attrib['property'].startswith('og:'):
			tag = meta.attrib['property']
			tag = translate(tag)
			path = tag.split(':')[1:]
			nested_set(data,path,meta.attrib['content']) 
	return data
	    
def scraper(url):
	response = requests.get(url)
	response.raise_for_status()
	return get_graph_data(response.text)
	



