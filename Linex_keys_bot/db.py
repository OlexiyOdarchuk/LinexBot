import sqlite3


class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exist(self, user_id):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.conn:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def get_users(self):
        with self.conn:
            return self.cursor.execute("SELECT `user_id` FROM `users`").fetchall()

    def get_categories(self):
        with self.conn:
            return self.cursor.execute("SELECT `title` FROM `categories`").fetchall()

    def get_order_price(self, title):
        with self.conn:
            result = self.cursor.execute("SELECT `price` FROM `tovars` WHERE `title` = ?", (title,)).fetchone()
            return int(result[0])

    def get_orders(self, category):
        with self.conn:
            return self.cursor.execute("SELECT `title`, `price` FROM `tovars` WHERE `category`= ?", (category,)).fetchall()

    def add_category(self, title, photo):
        with self.conn:
            return self.cursor.execute("INSERT INTO `categories` (`title`, `photo`) VALUES (?,?)", (title, photo,))

    def add_order(self, category, title, price, photo):
        with self.conn:
            return self.cursor.execute("INSERT INTO `tovars` (`category`, `title`, `price`, `photo`) VALUES (?,?,?,?)", (category, title, price, photo,))

    def delete_category(self, title):
        with self.conn:
            return self.cursor.execute("DELETE FROM `categories` WHERE `title` = ?", (title,))

    def delete_order(self, title):
        with self.conn:
            return self.cursor.execute("DELETE FROM `tovars` WHERE `title` = ?", (title,))

    def set_category_title(self, title, new_title):
        with self.conn:
            return self.cursor.execute("UPDATE `categories` SET `title` = ? WHERE `title` = ?", (new_title, title,))

    def set_order_price(self, title, price):
        with self.conn:
            return self.cursor.execute("UPDATE `tovars` SET `price` = ? WHERE `title` = ?", (price, title,))

    def get_category_photo(self, title):
        with self.conn:
            result = self.cursor.execute("SELECT `photo` FROM `categories` WHERE `title` = ?", (title,)).fetchone()
            return result[0]

    def get_order_photo(self, title):
        with self.conn:
            result = self.cursor.execute("SELECT `photo` FROM `tovars` WHERE `title` = ?", (title,)).fetchone()
            return result[0]

    def get_order_category(self, title):
        with self.conn:
            result = self.cursor.execute("SELECT `category` FROM `tovars` WHERE `title` = ?", (title,)).fetchone()
            return result[0]

    def set_photo(self, title, photo):
        with self.conn:
            return self.cursor.execute("UPDATE tovars SET photo = ? WHERE title = ?", (photo, title,))