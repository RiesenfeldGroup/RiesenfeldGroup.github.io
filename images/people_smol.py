import os

names = []
names.append("sam")
names.append("frank")
names.append("hanna")
names.append("hope")
names.append("ryan")
names.append("joy")
names.append("joey")


ext = ".jpg"
suffix = "_smol"

for name in names:
	old_file = name + ext
	new_file = name + suffix + ext
	os.system("convert "+old_file+" -resize 300x300 "+new_file)

print("DONE")
