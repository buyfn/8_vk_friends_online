import vk
import getpass


APP_ID = 6068898


def get_user_login():
    return input('Enter email: ')


def get_user_password():
    return getpass.getpass('Enter password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    return api.users.get(user_ids=api.friends.getOnline())


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('%s %s' % (friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()

    print('Waiting for vk to respond...')
    friends_online = get_online_friends(login, password)

    print('\nFriends online:')
    output_friends_to_console(friends_online)
