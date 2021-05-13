import re
import sys
import requests


if __name__ == "__main__":
	fp = sys.argv[1]
	bad_links = []
	with open(fp) as f:
		try:
			for x in re.findall('(?:http|ftp|https):\/\/[\w_-]+(?:(?:\.[\w_-]+)+)[\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]?', f.read()):
				print(x)
				if(re.match('404',requests.get(x).text)):
					bad_links.append(x)
		except requests.RequestException as e:
			bad_links.append(x)
	sys.exit(1 if len(bad_links) != 0 else 0)
