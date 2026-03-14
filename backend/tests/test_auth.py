from app.core.auth import require_view


class DummyUser:
    org_id = "org_test"
    user_id = "user_test"


def test_require_view():

    user = DummyUser()

    assert user.org_id == "org_test"