from qbay.models import register, login


def test_r1_1_user_register():
    '''
    Testing R1-1: If either the email or password are empty,
    the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u1', '', '234567') is False
    assert register('u0', 'test2@test.com', '') is False
    assert register('u4', '', '') is False


def test_r1_2_user_register():
    '''
    Testing R1-2: If email has already been used, its not
    unique and the test fails
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''

    user = login('test0@test.com', 123456)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 1234567)
    assert user is None
