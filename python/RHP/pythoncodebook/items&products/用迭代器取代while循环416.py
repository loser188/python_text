#
def reader(s):
    for chunk in iter(lambda :s.recv(CHUNKSIZE),b''):
        process_data(data)
