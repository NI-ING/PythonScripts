import wget


def download (url) :

	print('Beginning file download ... ')

	url = 'https://cdn.fbsbx.com/v/t59.3654-21/87450003_1639177669553590_2010244504996544512_n.mp4/audioclip-1582890800000-1811.mp4?_nc_cat=111&_nc_sid=7272a8&_nc_oc=AQlUotLwguWrYzy02baKW-BcCfzKxgkm5oMVTD9hvXnZgRn0dbDTmR3NkLa34770zpOvLkl0rBHvL4VAqeV1xW92&_nc_ht=cdn.fbsbx.com&oh=9194d968611723d7c81467aa1e5e84c2&oe=5E5B967D'
	wget.download(url, 'audio_file.wav')


url_link = data.get('entry')[0].get('messaging')[0].get(
            'message').get('attachments')[0].get('payload').get('url')
        print (url_link)
	print('Beginning file download ... ')
	wget.download(url_link, 'audio_file.wav')
