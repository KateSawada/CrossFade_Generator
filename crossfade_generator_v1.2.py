#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from binascii import hexlify

def initialize_dir():
    mkdir_songs()
    mkdir_jacket()
    mkdir_logos()

def mkdir_songs():
    """
    プログラムと同じディレクトリにsongsフォルダを生成
    """
    path_songs = os.path.abspath("songs")
    if not os.path.isdir(path_songs):
        os.mkdir(path_songs)

def mkdir_jacket():
    """
    プログラムと同じディレクトリにjacketsフォルダを生成
    """
    path_jacket = os.path.abspath("jacket")
    if not os.path.isdir(path_jacket):
        os.mkdir(path_jacket)

def mkdir_logos():
    """
    プログラムと同じディレクトリにlogosフォルダを生成
    """
    path_logos = os.path.abspath("logos")
    if not os.path.isdir(path_logos):
        os.mkdir(path_logos)



def make_exo():
    """
    exoファイルを出力する本体
    """

    #すでにout.exoが存在するか確認
    if os.path.isfile("out.exo"):
        is_overwrite = ""
        #存在する場合, 上書きして良いか確認
        while is_overwrite != "yes":
            is_overwrite = input("out.exo is already exist. dou you wish to overwrite exo file?(yes/no): ")
            if is_overwrite == "no":
                print("program will exit")
                exit()
    #生成する動画の時間(秒)
    video_length = input("enter the video duration(sec): ")
    while True:
        try:
            video_length = int(video_length)
            break
        except:
            video_length = input("enter the video duration(sec): ")

    #フレームレート
    rate = int(input("enter the video fps(frame per second): "))
    while True:
        try:
            rate = int(rate)
            break
        except:
            rate = input("enter the video fps(frame per second): ") 

    #オープニングカットを入れるかどうか
    op_include = ""
    while op_include != "yes" and op_include != "no":
            op_include = input("do you wish to add opening cut?(yes/no): ")

    #エンディングカットを入れるかどうか
    ed_include = ""
    while ed_include != "yes" and ed_include != "no":
            ed_include = input("do you wish to add ending cut?(yes/no): ")


    print("now writing... please wait")
    #書き込む文字列を生成

    #共通部分
    #[exedit]
    exo_exedit = "[exedit]\nwidth=1280\nheight=720\nrate=" + str(rate) + "\nscale=1\naudio_rate=44100\naudio_ch=2\n"

    section = 0
    exo_op = ""

    op_frame = {"yes": rate * 4, "no": 0}
    ed_frame = {"yes": rate * 2, "no": 0}
    if op_include == "yes":

        #op
        exo_op += "[" + str(section) + "]\nstart=1\nend=" + str(rate * 4) + "\nlayer=1\noverlay=1\ncamera=0\n"
        exo_op += "[" + str(section) + ".0]\n_name=図形\nサイズ=100\n縦横比=0.0\nライン幅=4000\ntype=0\ncolor=ffffff\nname=\n"
        exo_op += "[" + str(section) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00\nblend=0\n"
        section += 1

        exo_op += "[" + str(section) + "]\nstart=" + str(int(rate * 1.2)) + "\nend=" + str(rate * 4) + "\nlayer=2\noverlay=1\ncamera=0\n"
        exo_op += "[" + str(section) + ".0]\n_name=図形\nサイズ=506\n縦横比=0.0\nライン幅=4000\ntype=2\ncolor=000000\nname=\n"
        exo_op += "[" + str(section) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00\nblend=0\n"
        section += 1

        exo_op += "[" + str(section) + "]\nstart=" + str(int(rate * 1.2)) + "\nend=" + str(int(rate * 2.2)) + "\nlayer=3\noverlay=1\n"
        exo_op += "[" + str(section) + ".0]\n_name=マスク\nX=0.0\nY=0.0\n回転=45.00\nサイズ=748,330,1\n縦横比=0.0\nぼかし=0\nマスクの反転=1\ntype=2\nname=\nmode=0\n"
        section += 1

        exo_op += "[" + str(section) + "]\nstart=1\nend=" + str(int(rate * 0.3)) + "\nlayer=4\noverlay=1\ncamera=0\n"
        exo_op += "[" + str(section) + ".0]\n_name=図形\nサイズ=0,476,1\n縦横比=0.0\nライン幅=4000\ntype=2\ncolor=000000\nname=\n"
        exo_op += "[" + str(section) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00,360.00,1\nblend=0\n"
        section += 1

        exo_op += "[" + str(section) + "]\nstart=" + str(int(rate * 0.3 + 1)) + "\nend=" + str(rate * 4) + "\nlayer=4\noverlay=1\ncamera=0\n"
        exo_op += "[" + str(section) + ".0]\n_name=画像ファイル\nfile="+ os.path.abspath("logos") + "\\logo_small.png\n"
        exo_op += "[" + str(section) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00\nblend=0\n"
        section += 1

        exo_op += "[" + str(section) + "]\nstart=" + str(int(rate * 0.3)) + "\nend=" + str(int(rate * 1.2)) + "\nlayer=6\ngroup=1\noverlay=1\ncamera=0\n"
        exo_op += "[" + str(section) + ".0]\n_name=図形\nサイズ=476\n縦横比=0.0\nライン幅=4000\ntype=2\ncolor=000000\nname=\n"
        exo_op += "[" + str(section) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00\nblend=7\n"
        section += 1

        exo_op += "[" + str(section) + "]\nstart=" + str(int(rate * 0.3)) + "\nend=" + str(int(rate * 1.2)) + "\nlayer=7\ngroup=1\noverlay=1\n"
        exo_op += "[" + str(section) + ".0]\n_name=マスク\nX=0.0\nY=0.0\n回転=0.00,90.00,1\nサイズ=0,476,1\n縦横比=0.0\nぼかし=0\nマスクの反転=1\ntype=2\nname=\nmode=0\n"
        section += 1

        exo_op += "[" + str(section) + "]\nstart=" + str(int(rate * 3.3)) + "\nend=" + str(int(rate * 4.5)) + "\nlayer=10\n"
        exo_op += "[" + str(section) + ".0]\n_name=シーンチェンジ\n調整=0.00\ntrack1=0.00\n反転=0\ncheck0=0\ntype=15\nfilter=0\nname=\nparam=*\n"
        section += 1



    exo_common = ""
    #カメラ
    exo_common += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1) + "\nend=" + str(video_length * rate - ed_frame[ed_include]) + "\nlayer=1\n"
    exo_common += "[" + str(section) + ".0]\n_name=カメラ制御\nX=0.0\nY=0.0\nZ=-2000.0\n目標X=0.0\n目標Y=0.0\n目標Z=0.0\n目標ﾚｲﾔ=0\n傾き=0.00\n深度ぼけ=0.0\n視野角=60.00\nZバッファ/シャドウマップを有効にする=1\nrange=6\n"
    section += 1
    #影
    exo_common += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1) + "\nend=" + str(video_length * rate - ed_frame[ed_include]) + "\nlayer=2\n"
    exo_common += "[" + str(section) + ".0]\n_name=シャドー(カメラ制御)\n光源X=0.0\n光源Y=-2000.0\n光源Z=-2000.0\n濃さ=24.3\n精度=55\n"
    section += 1
    #背景
    exo_common += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1) + "\nend=" + str(video_length * rate - ed_frame[ed_include]) + "\nlayer=3\noverlay=1\ncamera=1\n"
    exo_common += "[" + str(section) + ".0]\n_name=画像ファイル\nfile=" + os.path.abspath("jacket") + "\\jacket.png\n"
    exo_common += "[" + str(section) + ".1]\n_name=ぼかし\n範囲=183\n縦横比=0.0\n光の強さ=60\nサイズ固定=0\n"
    exo_common += "[" + str(section) + ".2]\n_name=拡張描画\nX=0.0\nY=0.0\nZ=1339.8\n拡大率=650.92\n透明度=0.0\n縦横比=0.0\nX軸回転=0.00\nY軸回転=0.00\nZ軸回転=0.00\n中心X=0.0\n中心Y=0.0\n中心Z=0.0\n裏面を表示しない=0\nblend=0\n"
    section += 1
    #波形
    exo_common += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1) + "\nend=" + str(video_length * rate - ed_frame[ed_include]) + "\nlayer=4\noverlay=1\ncamera=1\n"
    exo_common += "[" + str(section) + ".0]\n_name=音声波形表示\n横幅=621\n高さ=240\n音量=400.0\nn再生位置=0.00\n編集全体の音声を元にする=1\nfile=\ntype=2\nmode=1\nres_w=32\nres_h=40\npad_w=25\npad_h=25\ncolor=8e7616\nnsample_n=0\nmirror=0\n"
    exo_common += "[" + str(section) + ".1]\n_name=極座標変換\n中心幅=350\n拡大率=100.0\n回転=180.0\n渦巻=0.00\n"
    exo_common += "[" + str(section) + ".2]\n_name=拡張描画\nX=800.0\nY=-100.0\nZ=-400.0\n拡大率=100.00\n透明度=0.0\n縦横比=0.0\nX軸回転=0.00\nY軸回転=0.00\nZ軸回転=0.00\n中心X=0.0\n中心Y=0.0\n中心Z=0.0\n裏面を表示しない=0\nblend=0\n"
    section += 1
    #左側のジャケット
    exo_common += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1) + "\nend=" + str(video_length * rate - ed_frame[ed_include]) + "\nlayer=5\noverlay=1\ncamera=1\n"
    exo_common += "[" + str(section) + ".0]\n_name=画像ファイル\nfile=" + os.path.abspath("jacket") + "\\jacket.png\n"
    exo_common += "[" + str(section) + ".1]\n_name=拡張描画\nX=-1000.0\nY=0.0\nZ=500.0\n拡大率=190.00\n透明度=0.0\n縦横比=0.0\nX軸回転=0.00\nY軸回転=-35.00\nZ軸回転=0.00\n中心X=0.0\n中心Y=0.0\n中心Z=0.0\n裏面を表示しない=0\nblend=0\n"
    section += 1
    #右側のジャケット
    exo_common += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1) + "\nend=" + str(video_length * rate - ed_frame[ed_include]) + "\nlayer=6\noverlay=1\ncamera=1\n"
    exo_common += "[" + str(section) + ".0]\n_name=画像ファイル\nfile=" + os.path.abspath("jacket") + "\\jacket_back.png\n"
    exo_common += "[" + str(section) + ".1]\n_name=拡張描画\nX=1000.0\nY=0.0\nZ=500.0\n拡大率=190.00\n透明度=0.0\n縦横比=0.0\nX軸回転=0.00\nY軸回転=35.00\nZ軸回転=0.00\n中心X=0.0\n中心Y=0.0\n中心Z=0.0\n裏面を表示しない=0\nblend=0\n"
    section += 1
    #下の画像
    exo_common += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1) + "\nend=" + str(video_length * rate - ed_frame[ed_include]) + "\nlayer=7\noverlay=1\ncamera=1\n"
    exo_common += "[" + str(section) + ".0]\n_name=画像ファイル\nfile=" + os.path.abspath("logos") + "\\bottom.png\n"
    exo_common += "[" + str(section) + ".1]\n_name=拡張描画\nX=0.0\nY=1145.6\nZ=601.9\n拡大率=302.91\n透明度=0.0\n縦横比=0.0\nX軸回転=-90.00\nY軸回転=0.00\nZ軸回転=0.00\n中心X=0.0\n中心Y=0.0\n中心Z=0.0\n裏面を表示しない=0\nblend=0\n"
    section += 1


    #songsフォルダから曲の情報を取得
    songs_file = os.listdir(os.path.abspath("songs"))
    songs_filename = [f for f in songs_file if os.path.isfile(os.path.join(os.path.abspath("songs"), f))]

    if len(songs_filename) == 0:
        print("Error: songs file could not found...")
        input("press enter to exit")
        exit()


    songs_filename = sorted(songs_filename, key=lambda s: int(re.search(r'\d+', s).group())) #トラック番号の順に並び替え
    songs_data = [i.split("[exo]") for i in songs_filename] #[トラック番号, 作曲者, 曲名(拡張子つき)] のリスト
    songs_num = len(songs_data)
    song_length = (video_length * rate - op_frame[op_include] - ed_frame[ed_include]) // songs_num #1曲あたりのフレーム数

    exo_songs = ""
    for track_num in range(songs_num):
        #テキスト
        hex_str = (hexlify((songs_data[track_num][0] + " " + songs_data[track_num][1] + " - " + songs_data[track_num][2][:-4]).encode('utf-16'))).decode("ascii")[4:]
        for _ in range(len(hex_str),4096,4):
            hex_str += "0000"
        exo_songs += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1 + song_length * track_num) + "\nend=" + str(op_frame[op_include] + song_length * (track_num + 1)) + "\nlayer=8\noverlay=1\ncamera=0\n"
        exo_songs += "[" + str(section) + ".0]\n_name=テキスト\nサイズ=41\n表示速度=0.0\n文字毎に個別オブジェクト=0\n移動座標上に表示する=0\n自動スクロール=0\nB=0\nI=0\ntype=0\nautoadjust=0\nsoft=1\nmonospace=0\nalign=0\nspacing_x=0\nspacing_y=0\nprecision=1\ncolor=000000\ncolor2=000000\nfont=SimSun-ExtB\ntext=" + hex_str + "\n"
        exo_songs += "[" + str(section) + ".1]\n_name=フェード\nイン=0.50\nアウト=0.50\n"
        exo_songs += "[" + str(section) + ".2]\n_name=標準描画\nX=-582.0\nY=281.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00\nblend=0\n"
        section += 1

        #音声
        exo_songs += "[" + str(section) + "]\nstart=" + str(op_frame[op_include] + 1 + song_length * track_num) + "\nend=" + str(op_frame[op_include] + song_length * (track_num + 1)) + "\nlayer=9\noverlay=1\naudio=1\n"
        exo_songs += "[" + str(section) + ".0]\n_name=音声ファイル\n再生位置=0.00\n再生速度=100.0\nループ再生=0\n動画ファイルと連携=0\nfile=" + os.path.abspath("songs")+ "\\" + songs_filename[track_num] + "\n"
        exo_songs += "[" + str(section) + ".1]\n_name=音量フェード\nイン=0.50\nアウト=0.50\n"
        exo_songs += "[" + str(section) + ".2]\n_name=標準再生\n音量=100.0\n左右=0.0\n"
        section += 1


    exo_ed = ""
    if ed_include == "yes":
        #背景
        exo_ed += "[" + str(section) + "]\nstart=" + str(video_length * rate - ed_frame[ed_include] + 1) + "\nend=" + str(video_length * rate) + "\nlayer=1\noverlay=1\ncamera=0\n"
        exo_ed += "[" + str(section) + ".0]\n_name=図形\nサイズ=100\n縦横比=0.0\nライン幅=4000\ntype=0\ncolor=ffffff\nname=\n"
        exo_ed += "[" + str(section) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=100.00\n透明度=0.0\n回転=0.00\nblend=0\n\n"
        section += 1
        #画像
        exo_ed += "[" + str(section) + "]\nstart=" + str(video_length * rate - ed_frame[ed_include] + 1) + "\nend=" + str(video_length * rate) + "\nlayer=2\noverlay=1\ncamera=0\n"
        exo_ed += "[" + str(section) + ".0]\n_name=画像ファイル\nfile=" + os.path.abspath("logos") + "\\logo_small.png\n"
        exo_ed += "[" + str(section) + ".1]\n_name=標準描画\nX=0.0\nY=0.0\nZ=0.0\n拡大率=46.60\n透明度=0.0\n回転=0.00\nblend=0\n\n"
        section += 1

        #シーンチェンジ
        exo_ed += "[" + str(section) + "]\nstart=" + str(video_length * rate - ed_frame[ed_include] - int(rate * 0.3)) + "\nend=" + str(video_length * rate - ed_frame[ed_include] + int(rate * 0.3)) + "\nlayer=10\n"
        exo_ed += "[" + str(section) + ".0]\n_name=シーンチェンジ\n調整=0.00\ntrack1=0.00\n反転=0\ncheck0=0\ntype=15\nfilter=0\nname=\nparam=*\n"





    





    #ファイルを上書き
    f = open("out.exo", "w", encoding="shift_jis")
    f.write(exo_exedit)
    f.write(exo_op)
    f.write(exo_common)
    f.write(exo_songs)
    f.write(exo_ed)
    f.close()


    #曲の情報


    print("exported successfully!")
    input("press enter to exit")
    




if __name__ == "__main__":
    initialize_dir()
    make_exo()