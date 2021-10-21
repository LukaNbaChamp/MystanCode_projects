"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakout_extension import BreakoutGraphics

"""
EXTENSION below
"""
# from breakout_extension import BreakoutGraphics
FRAME_RATE = 1000 / 120     # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:
        graphics.ball.move(graphics.getter_dx(), graphics.getter_dy())
        pause(FRAME_RATE)                               # pause

        graphics.wall_bounce()                          # check reach wall
        graphics.object_check()                         # check paddle or brick

        if graphics.ball.y > graphics.window_height:    # the ball exceed the lower boundary
            graphics.reset_ball()                       # reset the ball to starting position
            lives -= 1                                  # lives minus one

        if graphics.ball.y == 188 and graphics.getter_dy() == 0:    # win condition
            print("YOU WIN !!!")
            break
        elif lives == 0:                                            # lose condition
            graphics.lose()
            break

if __name__ == '__main__':
    main()
"""
「Week2 - 物件導向」的重點有下列八點：
(1.) 製造小小兵的「constructor 部門」其實就是
def  __init__
而它的功能是將所有 instance variables (attributes) 存到 graphics, 並讓所有透過它製造出來的小小兵 (instance/object) 擁有所有的 methods & attributes!
-
(2.) Methods 會根據「有沒有使用到 graphics」而分成 Instance Methods 以及 Static Methods. 前者的表現會因為小小兵不同而有些許不同，後者則表現完全一模一樣。因此，Static Methods 可以透過 class 來呼叫！
-
(3.) 想要承襲一個 class, 只要將該 class 放到定義後方的括弧、並在 def __init__ 裡面呼叫「super( ).__init__ 」啟動 Super Class 的所有 attributes＆methods
-
(4.) 我們透過承襲的上課範例想讓大家了解「attributes」與「parameters」之間的差別～ 前者是放在 graphics 的箱子名稱📦 後者則是接收使用者傳入 def __init__ 的箱子📦 舉例來說：
def __init__(graphics, weights):
        graphics.w = weights
w 是我們這個 class 的 attribute, 而 weights 則是 parameter 
-
(5.) 我們發現 __name__ 其實是每個 Python 檔案都有的系統變數！系統會根據一個檔案到底是「被執行」還是「被 import」去丟入 '__main__' 的文字或是 'filename' 的文字
-
(6.) 我們在 pypal.py 的檔案發現：把 keyword arguments 的 default value 數值存入檔案上方的常數可以讓程式碼維護/修改變得更加便利 🔥 也可以透過這個方法，讓使用者在呼叫您的 class 多了很多客製化的選項～（不給改的就不提供 😌 大家可以參考 zone.py 裡面我們 MAX_SPEED 常數的例子）
-
(7.) 通常在 class 內部的 instance variables/attributes 都會以 private 的型式儲存！在 Python，我們會使用 _var 以及 __var 來表示 private 的概念：前者我會稱它為「非強制性的 private」後者我則會稱之為「強制性的 private」！請同學們在寫作業二的時候務必將 attributes 都寫成 private 🔥
-
(8.) 在 class 內部建造時若要使用內部 method, 要記得使用 graphics.method 來呼叫！就好像是使用端要使用 method 時需要透過 object.method 的概念 🤓
-
最後希望大家都待在家寫打磚塊作業、防疫拯救台灣 😆 
期待看到大家作品 🤩 見證 ++ 獎學金的誕生！
-
Sincerely,
Jerry"""