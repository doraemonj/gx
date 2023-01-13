import os

# path1 = r"D:\qycache\download\欧美电影解说，陌陌说电影，包你听的过瘾"
path1 = r"D:\QLDownload"
f = os.listdir(path1)
# print(f)
path2 = r"D:\handle_video"
f2 = os.listdir(path2)
# print(f2)
for o in f:
    # print(o)
    s = o.split('480')[0]
    # print(s)
    # print(s)
    for j in f2:
        print(j)
        m = j.split('480P')[0]
        print(m)
        if s == m:
            print('YYY')
            os.remove(path1 + '\\' + o)
