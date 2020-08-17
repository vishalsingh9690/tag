from bs4 import BeautifulSoup
import requests
scr2 = "google_tag.script"
match_url = "https://www.googletagmanager.com/gtm.js"

url_lists = [{"url":"https://hcp.galdermaaesthetics.com","key":"GTM-PDMJZSRvis"},{"url":"https://www.galdermaaesthetics.com","key":"GTM-TZH46DX"},{"url":"https://www.galdermaaesthetics.com.br","key":"GTM-PW8P8KC"},{"url":"https://www.galdermaaesthetics.com.au","key":"GTM-5KRXZFD"}]

for url_list in url_lists:
	url = url_list['url']
	code = url_list['key']
	url_list["status"] = "Unmatched"
	response = requests.get(url)
	soup = BeautifulSoup(response.content)
	scripts = soup.find_all('script')
	for script in scripts:
		find_tag = script.get('src')
		if find_tag:
			if (find_tag.find(scr2) != -1):
				new_response = requests.get(url+find_tag)
				soup2 = BeautifulSoup(new_response.content)
				p_tag = soup2.find('p')
				p_data = p_tag.string
				if (p_data.find(match_url) != -1) and (p_data.find(code) != -1):
					url_list["status"] = "Matched"

print(url_lists)


				# print(p_data.string)
		# else: 
			# print ("Doesn't contains given substring")


