How do I:
--Edit any of the site pages?
----The site pages are contained in:
------index.html (home page)
------people.html
------projects.html
------publications.html
------happenings.html
----Most of the site page .html files can be edited directly, however, it is IMPORTANT that index.html and happenings.html NOT be edited directly. In lieu of editing index.html, one should edit index_pre.html. And in lieu of editing happenings.html, one should either edit happenings_pre.html for aesthetic changes OR edit happenings.txt for adding events (see below)
--Add new events to the newsfeed?
	1) Open happenings.txt
	2) Create a new entry in this .txt file. It should begin with "BEGIN_EVENT" and "END_EVENT" tags, and include "MONTH", "YEAR", and "DESCRIPTION" tags. The "MONTH" and "YEAR" tags are just used to sort the events and to display the month of the event; the "DESCRIPTION" field should be formatted HTML to be injected into a paragraph environment (i.e., <p>DESCRIPTION</p>).
	3) Run the following commands from the terminal:
		./format_happenings.sh
		git pull
		git add index.html happenings.html happenings.txt
		git commit -m "routine newsfeed update"
		git push
----It is IMPORTANT to note the following about the newsfeed:
------The events in happenings.txt do not have to be sorted in chronological order. Events are sorted and displayed in chronological order. This way, new events (even ones from long ago) can be appended to the end of happenings.txt without much thought.
------Only a few of the events are displayed on the home page (the exact number is determined by the variable "n_displayed" in format_events.py). However, all events are displayed on the Happenings page on the site.


The rest of this document is dedicated to credits for the Escape Velocity template by HTML5 UP.

==============================================================================================

Escape Velocity by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)


A new responsive template featuring a flat (but not too flat) minimalistic design, spacious
layout, and styling for all basic page elements. Its demo images* are courtesy of the supremely
talented photographer Felicia Simion. If you like photography or just enjoy being blown away by
awesome stuff, check out her portfolio for more stunning images:

http://ineedchemicalx.deviantart.com/

(* = Not included! Only meant for use with my own on-site demo, so please do NOT download
and/or use any of Felicia's work without her explicit permission!)

Feedback, bug reports, and comments are not only welcome, but strongly encouraged :)

AJ
aj@lkn.io | @ajlkn

PS: Not sure how to get that contact form working? Give formspree.io a try (it's awesome).


Credits:

	Demo Images:
		Felicia Simion (ineedchemicalx.deviantart.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Responsive Tools (github.com/ajlkn/responsive-tools)
