# hiddencatch-differ
找碴比較器，可以抓取程序名稱，調整位置遊玩找碴...
這裡以爆爆王為例子

## Install
**Use CMD**
```
> git clone https://github.com/urayoru113/bnb-hiddencatch-differ
> pip install pillow opencv-python numpy pywin32
> python diff.py
```


**想直接下載的話**
<br/>
[download](https://github.com/urayoru113/bnb-hiddencatch-differ/releases)

## explain

請先打開遊戲，建議使用視窗化(alt+enter)執行，並確保視窗在前景，可以被別的視窗蓋住，但不能最小化

然後點選diff.exe(或執行```python diff.py```)

打開setting.ini調整參數讓框框對齊如下圖

![](https://i.imgur.com/geLJrBx.png)

原理為截取rect框框內的Pixel並相減，將結果取決對值後印在diff視窗
