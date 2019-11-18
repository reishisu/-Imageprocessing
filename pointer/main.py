import tkinter  # GUIウィンドウを作成したいため
from PIL import Image, ImageTk  # Pillowの画像とtkinterの画像の読み込み用

# 元画像を読み込む
image = Image.open('../images/cafe.jpg')

# GUIウィンドウを作成
window = tkinter.Tk(className="pointer sample")

# Pillowの画像をtkinter用の画像に変換する
image_tk = ImageTk.PhotoImage(image)

# Pillowで読み込んだ画像をウィンドウサイズにセットしてCanvasを作成する
canvas = tkinter.Canvas(window, width=image.size[0], height=image.size[1])

# 作成したCanvasの中に画像をセットする(左上に画像の中心がくるので縦横半分ずつずらす)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

# windowsに作成したcanvas並べる
canvas.pack()

# 画像(Canvas)の上でマウスが移動したとき用のコールバック関数
def callback(event):
    # コンソールが荒れないように出力を常に上書きする
    print("\r{0}:x={1}, y={2}".format("マウスの座標", str(event.x).zfill(3), str(event.y).zfill(3)), end="")

# 第一引数の文字列で画像(Canvas)の上でマウスを動かした時に、第二引数のコールバック関数を呼ばれる
canvas.bind("<Motion>", callback)

# イベントのループを開始する
tkinter.mainloop()
