import instaloader
import os


def get_insta_data(username):
    """
    Функция, которая забирает данные пользователя с его профиля
    Данные: биография, имя, кол-во постов, кол-во подписчиков, кол-во подписок, путь до аватарки пользователя
    """

    il = instaloader.Instaloader()

    user = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    il.login(user=user, passwd=password)

    try:
        profile = instaloader.Profile.from_username(il.context, username=username)

        bio = profile.biography
        name = profile.full_name
        media = profile.mediacount
        followers = profile.followers
        followees = profile.followees
        avatar_url = profile.profile_pic_url

        return {
            'username': username,
            'bio': bio,
            'name': name,
            'media': media,
            'followers': followers,
            'followees': followees,
            'avatar_url': avatar_url
        }
    except instaloader.ProfileNotExistsException:
        print(f'Профиль {username} не найден')

    except Exception as e:
        print(f'Ошибка {e} при получении данных из профиля {username}')