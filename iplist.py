IPlist = ['209.85.238.4','216.239.51.98','64.233.173.198','64.3.17.208','64.233.173.238']


# for address in range(len(IPlist)):
#     IPlist[address] = '%3s.%3s.%3s.%3s' % tuple(IPlist[address].split('.'))
#     IPlist.sort(reverse=False)

# for address in range(len(IPlist)):
#     IPlist[address] = IPlist[address].replace(' ', '')

# IPlist.sort(key=lambda address: list(map(int, address.split('.'))))

IPlist.sort(key=lambda address: list(map(str, address.split('.'))))
print(IPlist)