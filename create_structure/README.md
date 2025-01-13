# ディレクトリ構造作成スクリプト

このプロジェクトは、指定されたディレクトリ構造とファイルを自動的に作成するスクリプトを提供します。`structure.txt`ファイルに基づいて、ディレクトリとファイルを作成します。

## 機能

- `structure.txt`ファイルを読み取り、指定されたディレクトリとファイルを作成します。

## 使用方法

1. このリポジトリをクローンまたはダウンロードします。
2. プロジェクトのルートディレクトリに`structure.txt`ファイルを作成し、以下のような内容を記述します。

    ```plaintext
    ../../pet_vision/data/train/cats/
    ../../pet_vision/data/train/dogs/
    ../../pet_vision/data/validation/cats/
    ../../pet_vision/data/validation/dogs/
    ../../pet_vision/models/saved_model/
    ../../pet_vision/scripts/train.py
    ../../pet_vision/scripts/predict.py
    ../../pet_vision/requirements.txt
    ```

3. 必要なライブラリをインストールします（特に追加のライブラリは必要ありませんが、Pythonがインストールされていることを確認してください）。
4. ターミナルを開き、スクリプトを保存したディレクトリに移動します。
5. 以下のコマンドを実行してスクリプトを実行します。

    ```sh
    python create_structure.py
    ```

6. スクリプトが実行されると、`structure.txt`ファイルに基づいて指定されたディレクトリ構造とファイルが作成されます。

## 依存関係

- Python 3.x