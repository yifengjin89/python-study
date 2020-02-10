# 1/8/2020
# 练习 歌词解析

musicLrc = """[00:03.50]传奇
[01:04.31][01:05.32]只是因为在人群中多看了你一眼
[02:45.44][00:43.69]再也没有能忘掉你容颜"""

musicLrcList = musicLrc.splitlines()  # 分割每一行的字符串
print(musicLrcList)  # output: ['[00:03.50]传奇', '[01:04.31][01:05.32]只是因为在人群中多看了你一眼',
# '[02:45.44][00:43.69]再也没有能忘掉你容颜']
licDict = {}

for lrcLine in musicLrcList:
    lrcLineList = lrcLine.split("]")  # 分割 “]”
    print(lrcLineList)  # output： ['[00:03.50', '传奇']  ['[01:04.31', '[01:05.32', '只是因为在人群中多看了你一眼']
    # ['[02:45.44', '[00:43.69', '再也没有能忘掉你容颜']
    for index in range(len(lrcLineList) - 1):  # 只取到 （lrcList 长度 -1） ， 这表示 ['[00:03.50', '传奇'] length = 2，
        # length - 1 = '[00:03.50' ； 最后的歌词不取
        timeStr = lrcLineList[index][1:]  # output: 从下标1开始取  '[00:03.50'， 得到 '00:03.50'
        timeList = timeStr.split(":")  # 再次分割字符串 '00:03.50' ， 得到 ['00', '03.50']
        time = float(timeList[0]) * 60 + float(timeList[1])  # 因为要得到秒数，让字符串变成浮点数后相加，得到 3.50;
        licDict[time] = lrcLineList[-1]  # 存入字典， lrcLineList[-1] = ['[00:03.50', '传奇'] 的 下标-1 = '传奇'

print(licDict)
allTimeList = []
for t in licDict:  # 把所有的key 从licDict中取出，放入list 中 ；；或者可以用 allTimeList = list(licDict)
    allTimeList.append(t)
allTimeList.sort()
print(allTimeList)  # output: [3.5, 43.69, 64.31, 65.32, 165.44]

while 1:
    getTime = float(input("Enter time: "))
    for n in range(len(allTimeList)):
        tempTime = allTimeList[n]
        print("t %s" % tempTime)  # output tempTime = 3.5
        if getTime < tempTime:  # if getTime = 3;;  3  <  3.5;;  if get = 5，n = 1, tempTime = 43.69, then break loop
            break
    print("n = %d " % n)  # set getTime = 4, < 43.69 ,  in allTimeList, 43.69 is (n = 1)
    if n == 0:
        print("It's too small")
    else:  # n = 1
        print(licDict[allTimeList[n - 1]])  # allTimeList[n - 1] = 3.5 == licDict[3.5] == '传奇'
        break

