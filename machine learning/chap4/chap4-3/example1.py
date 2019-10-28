import urllib.request as req
import gzip, os, os.path
import ntpath

savepath=".mnist"
baseurl ="http://yann.lecun.com/exdb/mnist"
files = [
    "train-images-idx3-ubyte.gz",
"train-labels-idx1-ubyte.gz",
"t10k-images-idx3-ubyte.gz",
"t10k-labels-idx1-ubyte.gz"]

#download
#os.path.exist(" 있나 없다 검사할 폴더 경로)
#os.mkdir(path[,mode[) 경로 - 디렉토리생성, 모드 - 권한 디렉토리설정, 디렉토리생성
if not os.path.exists(savepath): os.mkdir(savepath)


for f in files:
    url = baseurl + "/" + f
    loc = savepath +"/" + f
    print("download:",url)
    if not os.path.exists(loc):
        # url에 해당하는 이미지 다운 후 지정이름으로
        req.urlretrieve(url,loc)

    # 압축해제하는 코드
for f in files:
    gz_file = savepath +"/" + f
    raw_file = savepath + "/" + f.replace(".gz","")
    print("gzip:",f)
    with gzip.open(gz_file,"rb") as fp:
        # read that jpg.file you need to use 'rb
        body = fp.read()
        with open(raw_file,"wb") as w:
            # file mode : write and binary.  since you are a writing a .jpg file
            w.write(body)
            '
    print("ok")
