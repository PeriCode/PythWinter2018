import json

music = {
	'genre': ['Rap', 'Rock', 'Pop', 'Neo-classic'],
	'singers': ['Eminem', 'Till Lindelman', 'Karmin', 'Howard Shore'],
	'country':['USA', 'German', 'Austria', 'British']
}

music_json = json.dumps(music) # метод dupms преобразует словарь в json-формат
f = open('Music.json', 'w')
f.write(music_json)
f.close()

f = open('Music.json', 'r')
json_file_read = f.read()
music_json = json.loads(json_file_read) # метод loads преобразует структуру json в python-словарь
print(music_json['country'])
