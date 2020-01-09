# 1/8/2020
# 练习 歌词解析

musicLrc = """[00:03.50]传奇
[01:04.31][01:05.32]只是因为在人群中多看了你一眼
[02:45.44][00:43.69]再也没有能忘掉你容颜"""

musicLrcList = musicLrc.splitlines()
print(musicLrcList)
licDict = {}

for lrcLine in musicLrcList:
    lrcLineList = lrcLine.split("]")
    print(lrcLineList)
    for index in range(len(lrcLineList) - 1):
        timeStr = lrcLineList[index][1:]
        timeList = timeStr.split(":")
        time = float(timeList[0]) * 60 + float(timeList[1])
        licDict[time] = lrcLineList[-1]

print(licDict)

