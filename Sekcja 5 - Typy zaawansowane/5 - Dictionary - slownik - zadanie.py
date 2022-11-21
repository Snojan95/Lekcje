channels = {'Google':'1480','Email':'300','Natural Traffic':'440','TV Spot':'700'}
print(channels)
print(channels.get('Email'))
channels_update = {'Natural Traffic':'520','News':'600'}
channels.update(channels_update)
print(channels)
print(channels.keys())
print(channels.pop('Email'))
print(channels)