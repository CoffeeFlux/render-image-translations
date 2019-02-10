from lxml import etree
import os, re

file_groups = [
    r'OP\[難易度説明\d+b?\]\.png',
    r'ST名前\d+b?\.png',
    r'アイテム入手文字\d+b?\.png',
    r'アプリ説明\d+b?\.png',
    r'アプリ説明n\d+b?\.png',
    r'イベント\[字\d+b?\]\.png',
    r'エリア\d+b?\.png',
    r'エリア名\d+b?\.png',
    r'ショップ\[商品説明\d+b?\]\.png',
    r'ショップ\[商品名\d+b?\]\.png',
    r'スキル説明\d+b?\.png',
    r'メッセ\[上書き\d+b?\]\.png',
    r'メッセ\[反芻\d+b?\]\.png',
    r'メニュー\[スキル用背景\d+b?\]\.png',
    r'メニュー\[操作説明\d+b?\]\.png',
    r'貴重品説明\d+b?\.png',
    r'貴重品説明n\d+b?\.png',
    r'消耗品説明\d+b?\.png',
    r'戦闘背景\d+b?\.png'
]

pic_subdir = 'Picture'
mask_subdir = 'masks'
output_file = 'light_tower_translations.xml'

translations = etree.Element('Translations')
num_re = re.compile(r'\d+')
image_count = 0

for i, group_re in enumerate(file_groups):
    group = etree.SubElement(translations, 'Group{0:0=3d}'.format(i), name=group_re, fill='', bitmap_mask='', ass_mask='')
    files = [f for f in os.listdir(pic_subdir) if re.match(group_re, f)]
    files.sort(key=lambda x: int(re.search(num_re, x).group(0)))
    for j, file_name in enumerate(files):
        etree.SubElement(group, 'Pic{0:0=3d}'.format(j), name=file_name).text = ''
        image_count += 1

print('Total images located: {}'.format(image_count))

tree = etree.ElementTree(translations)
tree.write(output_file, encoding='utf-8', pretty_print=True)
