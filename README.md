# nikki

## 手順
1. `nikki-server`下に`.env`ファイルを作成
2. Docker　Desktopのインストール
3. pipenvのインストール
   ```bash
   pip install pipenv
   ```
4. ライブラリをインストール
   ```bash
   pipenv install
   ```
5. データベースサーバーの起動
   `nikki-server`下で操作する
   ```bash
    docker-compose up
    ```

6. テーブル作成
   `docker-compose up`されている状態で別のコンソールを開き`nikki-server`下で操作する
    ```bash
    pipenv run create_tables
    ```
7. [Swagger UI](http://localhost:8000/docs) を開く
   