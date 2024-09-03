from services import get_insta_data
from database import create_table, create_connection, save_data_profile


def main():
    """
    Основная функция для выполнения поиска и сохранения данных
    """

    conn = create_connection('insta.db')
    create_table(conn)

    with open('usernames.txt') as file:
        usernames_src = [line.strip() for line in file]

    for username in usernames_src:
        data = get_insta_data(username)

        if data:
            save_data_profile(conn, data)
            print(f'Данные пользователя {username} сохранены!')

    conn.close()


if __name__ == '__main__':
    main()
