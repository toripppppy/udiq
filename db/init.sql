-- データベースとテーブルの作成
CREATE DATABASE IF NOT EXISTS test;
USE test;
CREATE TABLE IF NOT EXISTS `knowledges` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `word` VARCHAR(45) NULL,
  `meaning` TEXT NULL,
  PRIMARY KEY (`id`)
);

-- 既存の root ユーザーのパスワード設定
ALTER USER 'root'@'localhost' IDENTIFIED BY 'udiqpass';
FLUSH PRIVILEGES;