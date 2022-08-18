import os
from collections import OrderedDict

with open("happenings.txt", "r") as file:
	happenings_str = file.read()

begin = "BEGIN_EVENT"
end = "END_EVENT"
n_displayed = 4

n_events = happenings_str.count(begin)

events_pre = []
temp_str = happenings_str
for j in range(n_events):
	ind = temp_str.rfind(begin)
	events_pre.append(temp_str[ind:])
	temp_str = temp_str[:ind]

months = {}
months[1] = "January"
months[2] = "February"
months[3] = "March"
months[4] = "April"
months[5] = "May"
months[6] = "June"
months[7] = "July"
months[8] = "August"
months[9] = "September"
months[10] = "October"
months[11] = "November"
months[12] = "December"

class Event:
	def __init__(self, month, year, text):
		assert isinstance(month, int)
		assert isinstance(year, int)

		self.month = month
		self.year = year
		self.text = text

	def __eq__(self, other):
		return (self.month == other.month) and (self.year == other.year) and (self.text == other.text)

	def __lt__(self, other):
		if self.year < other.year:
			return True
		elif self.year > other.year:
			return False
		else:
			if self.month < other.month:
				return True
			else:
				return False

	def __gt__(self, other):
		return (other < self)

events = []
for pre in events_pre:
	month_ind = pre.find("MONTH")
	if month_ind == -1:
		pass
	temp_str = pre[month_ind:]
	newline_ind = temp_str.find("\n")
	temp_str = temp_str[:newline_ind]
	eq_ind = temp_str.find("=")
	month_str = temp_str[(eq_ind + 1):].replace('"', '')
	month = int(month_str)

	year_ind = pre.find("YEAR")
	if year_ind == -1:
		pass
	temp_str = pre[year_ind:]
	newline_ind = temp_str.find("\n")
	temp_str = temp_str[:newline_ind]
	eq_ind = temp_str.find("=")
	year_str = temp_str[(eq_ind + 1):].replace('"', '')
	year = int(year_str)

	text_ind = pre.find("DESCRIPTION")
	if text_ind == -1:
		pass
	temp_str = pre[text_ind:]
	newline_ind = temp_str.find("\n")
	temp_str = temp_str[:newline_ind]
	eq_ind = temp_str.find("=")
	text = temp_str[(eq_ind + 1):].replace('"', '')

	events.append(Event(month, year, text))

events.sort(reverse=True)

event_dict = OrderedDict()
for event in events:
	date = (event.month, event.year)
	if date not in event_dict:
		event_dict[date] = [event]
	else:
		event_dict[date].append(event)

### For index.html
export_str = ""

for date in event_dict.keys()[:n_displayed]:
	month, year = date
	month_str = months[month]
	year_str = str(year)
	export_str += "<h2>"+month_str+" "+year_str+"</h2>\n"
	for event in event_dict[date]:
		export_str += "<p>"+event.text+"</p>\n"

with open("index_pre.html", "r") as file_pre:
	with open("index.html", "w") as file:
		file.write(file_pre.read().replace("<!-- REPLACE ME -->", export_str))

### For happenings.html
export_str = ""

for date in event_dict.keys():
	month, year = date
	month_str = months[month]
	year_str = str(year)
	export_str += "<h2>"+month_str+" "+year_str+"</h2>\n"
	for event in event_dict[date]:
		export_str += "<p>"+event.text+"</p>\n"

with open("happenings_pre.html", "r") as file_pre:
	with open("happenings.html, "w"") as file:
		file.write(file_pre.read().replace("<!-- REPLACE ME -->", export_str))
