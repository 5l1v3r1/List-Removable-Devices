import win32file, win32api

list_removable_drives = []
def get_removable_drives():
	drive_list = win32api.GetLogicalDriveStrings()
	drive_list = drive_list.split('\x00')[0:-1]
	for letter in drive_list:
		if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:
			list_removable_drives.append(letter)
	return list_removable_drives
