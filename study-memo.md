## pythonバージョン管理
pyenvを使う。

## pythonの公式サイト関係
- [公式にチュートリアルあった。](https://docs.python.org/ja/3.6/tutorial/index.html#tutorial-index)
- [言語の仕様リファレンス](https://docs.python.org/ja/3.6/reference/index.html)
  - [pythonの公式リファレンスはBNF記法で書かれているので初見だとちょっと読めない。](https://qiita.com/RiSE_blackbird/items/8c3ea32bc2cb9b4fc00e)
    - [これも正規表現に似てるらしい。](https://hirogl-python.hatenadiary.org/entry/20100506/1273158693)

## パッケージ管理
pipを使う。
https://gammasoft.jp/python/python-library-install/
https://qiita.com/yuta-38/items/730bf91526f92fe0b41a
ちなみにpipでインスコされるパッケージがあるリポジトリpypiの呼び名はパイパイらしい。
https://pypi.org/

## 仮想環境構築方法
python標準でvenvっていうコマンドがあるのでそれを使う。
なぜこれを使うというと、普通に[pip installするとグローバルにパッケージがインスコされてしまい](https://qiita.com/overflowfl/items/1db8746b9831bb15e9b5)全てのプロジェクトでパッケージが導入されてしまうが、venvで仮想環境を作ってあげるとpip instalでインスコされるパッケージのパスがグローバルから仮想環境用に変更されるので、特定のプロジェクト毎にパッケージがインスコできるようになるため。
[venvをactivateすると内部的に$PATHを書き換えてくれている。](https://cod-sushi.com/python-venv/)
実際の流れは[python-japanが分かりやすい。](https://www.python.jp/install/macos/virtualenv.html)

## phperがpython入門するための文法とかの記事
記事内ではpythonのバージョンが2.7らしいのであくまで参考。
https://qiita.com/odoku/items/97100c9fa20449b72588
- python3ではソースがutf-8で保存されている場合はエンコード不要
  - https://qiita.com/KEINOS/items/6efc1147b917d7811b5b
  - https://www.haya-programming.com/entry/2018/04/23/163159
  - pythonのコードスタイルガイドにはpep8とかいうのがある。phpでいうところのpsr-2だと思われた。
    - https://pep8-ja.readthedocs.io/ja/latest/#
    - https://python.ms/pep8/
  - インデントはスペース4つがpep8準拠なのでvscodeの設定を調整する。
    - [この記事の](https://qiita.com/ksh-fthr/items/7cf8b5f2fde82d1c6bf7#visual-studio-code-%E3%81%AE%E4%BD%9C%E6%A5%AD%E7%94%A8%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E7%B7%A8%E9%9B%86)tabSize指定を4に変えたら良き。

## anaconda VS 公式版python
[公式サイト](https://www.python.jp/install/docs/pypi_or_anaconda.html)見たらわかる
