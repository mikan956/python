import glob
import ModStamp

#すべての画像ファイルのパスを取得する
files = glob.glob("images/*.jpg")

#先頭の画像のみを表示して確認
#パスの画像ファイルを読み込み
image = ModStamp.imread(files[0])

#確認用に縮小
image = ModStamp.resize(image, (500,200))

#画像データを表示
ModStamp.imshow("image", image)

#キーが押されるまで待機
key = ModStamp.waitkey(10000)
#エラー吐くので非推奨