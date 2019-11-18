import tkinter  # GUIウィンドウを作成したいため
import numpy as np  # 行列の計算用
from PIL import Image, ImageTk  # Pillowの画像とtkinterの画像の読み込み用

# 元画像を読み込む
image = Image.open('../images/cafe.jpg')
# 読み込んだ画像を3次元配列に変換する
image_array = np.array(image)

# GUIウィンドウを作成
window = tkinter.Tk(className="get rgb")

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
    # 読み込んだ画像は、[ 横[ 画素値[R, G, B, α(pngのみ)], ・・・ ],
    #                  横[ 画素値[R, G, B, α(pngのみ)], ・・・ ],
    #                        ・
    #                        ・
    #                        ・
    #                ]
    # ↑のような多次元配列になっているのでimage_array[y][x]とすれば、そのマウスのポインタの画素値が取得できる。
    r, g, b = image_array[event.y][event.x]
    # ゼロパディングする
    r = str(r).zfill(3)
    g = str(g).zfill(3)
    b = str(b).zfill(3)
    # コンソールが荒れないように出力を常に上書きする
    print("\rR={0}, G={1}, B={2}".format(r, g, b), end="")

# 第一引数の文字列で画像(Canvas)の上でマウスを動かした時に、第二引数のコールバック関数を呼ばれる
canvas.bind("<Motion>", callback)

# イベントのループを開始する
tkinter.mainloop()
