import os
from pathlib import Path 

SUBDIRECTORIES ={
	
	"DOCUMENTS":['.pdf', '.rtf','.txt', '.doc', '.docx'],
	"AUDIO":['.m4a','.m4b', '.mp3'],
	"VIDEOS":['.mov','.avi','.mp4'],
	"IMAGES":['.jpg','.jpeg','.png']
}

def pickDir(value):
	for category, suffixes in SUBDIRECTORIES.items():
		for suffix in suffixes:
			if suffix == value:
				return category
	return 'MISC'
				
def organizeDir():
	for item in os.scandir():
		if item.is_dir():
			continue
		filePath = Path(item)
		filetype = filePath.suffix.lower()
		directory = pickDir(filetype)
		directoryPath = Path(directory)
		if directoryPath.is_dir() == False:
			directoryPath.mkdir()
		filePath.rename(directoryPath.joinpath(filePath))

organizeDir()
