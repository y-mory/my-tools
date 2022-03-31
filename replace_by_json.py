#! /usr/bin/env python3

import json, shutil, os, datetime
global_bk_dir = './bk'

# bkフォルダを作り、置換対象ファイルのバックアップを複製
def make_buckup(bk_dir, target_file_name):
    dt = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    os.makedirs(bk_dir, exist_ok=True)
    shutil.copy(target_file_name, f'{bk_dir}/{target_file_name}.{dt}.bk')

# jsonをdict型で取得
def convet_json2dict(replace_dict_json_path):
    json_file = open(replace_dict_json_path, 'r', encoding='utf-8')
    json_dict = json.load(json_file)
    return json_dict

# 入力されたテキストに対し置換リストで置換後のテキストに上書き
def replace_by_dict(target_str, replace_dict):
    for key, val in replace_dict.items():
        target_str = target_str.replace(key, val)
    return target_str

# 置換リストに従って対象ファイルを一括置換
def export_replaced_file(target_file_name, replace_dict_json_path):
    
    # 置換対象ファイルのバックアップを作成
    make_buckup(global_bk_dir, target_file_name)
    
    # 置換リストをdict型で取得
    replace_words = convet_json2dict(replace_dict_json_path)
    
    # 置換対象ファイルを読み込みし置換後の文字列を取得
    with open(target_file_name, 'r', encoding='utf-8') as f:
        file_str = f.read()
        replace_by_dict(file_str, replace_words)
        file_str = replace_by_dict(file_str, replace_words)

    # 置換後の文字列を同一ファイル名で出力し上書き
    with open(target_file_name, 'w', encoding='utf-8') as f:
        f.write(file_str)

# 標準入力からファイルパスを取得
print('置換対象ファイルのパス入力してください')
tareget_file_name = input()

print('置換リスト.jsonのパスを入力してください')
replace_dict_json_path = input()

export_replaced_file(tareget_file_name, replace_dict_json_path)