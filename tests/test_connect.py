from pythonping import ping


res=ping('172.20.21.111', verbose=False, count=1)
print(res.stats_packets_returned)