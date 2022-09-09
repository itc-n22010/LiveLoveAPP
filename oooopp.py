from urllib import request, response
import pandas as pd                                                   
import webbrowser

                                                                      
uri = "http://lcsious.com/other/lovelive_cupsize.php"                       
table = pd.read_html(uri, match="身長")[4]                                  
table = table.drop(columns=['学年',"TU差","推定アンダー","予想体重","予想BMI","予想-BMI22",'星座',"計算","声優","トップ加味","カップTU" ])           
table = table.rename(columns={"μ's＋ｱｸｱ＋SS＋虹": '名前'})
table = table.replace(' ', '', regex=True)


while True:
    print('\n1,キャラ名  2,詳細情報')
    suu = input('どちらが知りたい？')
    if suu == '1':
        name = input('名前入力してくれ：')
        namepuls = 'https://dic.pixiv.net/a/{}'.format(name) 
        url = namepuls
        webbrowser.open(url, new=0, autoraise=True) 
        sube = table.loc[table.名前 == name]
        print(sube) 
    elif suu == '2':
        print('1,グループ 2,年齢 3,血液型 4,カップサイズ')
        syo = input('どちらがしりたい？')
        if syo == '1':
            print("μ's, Aqours, 虹ヶ咲")
            guru = input('グループ名を入力して：')
            guru_name = table.loc[table.グループ == guru]
            print(guru_name)
        elif syo == '2':
            print("17歳, 16歳, 15歳, 14歳")
            tosi = input('知りたい年齢を入力してください：')
            nen = table.loc[table.年齢 == tosi]
            print(nen)
        elif syo == '3':
            print("A, B, O, AB")
            ketu = input('知りたい血液型を入力してください：')     
            ketu_name = table.loc[table.血液型 == ketu]
            print(ketu_name)
        elif syo == '4':
            print("A, AA, B, C, D, E, F")
            mune = input('知りたいカップ数を入力してください：')     
            nume_name = table.loc[table.カップ計算 == mune]
            print(nume_name)

        



