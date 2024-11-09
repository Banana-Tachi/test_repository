from PIL import Image, ImageDraw
import random

def create_maze(width, height, cell_size):
    # 迷路の内部サイズ（実際の画像サイズはこれに壁の分が追加される）
    img_width = width * cell_size + cell_size
    img_height = height * cell_size + cell_size
    
    # 白い背景で画像を作成
    image = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(image)
    
    # 外枠を描画
    draw.rectangle([0, 0, img_width-1, img_height-1], outline='black')
    
    # 縦の壁を描画
    for x in range(cell_size, img_width-cell_size, cell_size):
        for y in range(0, img_height, cell_size):
            if random.random() < 0.4:  # 40%の確率で壁を描画
                draw.line([(x, y), (x, y+cell_size)], fill='black', width=40)
    
    # 横の壁を描画
    for y in range(cell_size, img_height-cell_size, cell_size):
        for x in range(0, img_width, cell_size):
            if random.random() < 0.4:  # 40%の確率で壁を描画
                draw.line([(x, y), (x+cell_size, y)], fill='black', width=40)
    
    # 画像を保存
    image.save('simple_maze.png')
    
# 迷路を生成（8x8のグリッド、各セル100ピクセル）
create_maze(8, 8, 100)