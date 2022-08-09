from models.user import users


class AuthService:
    
    def get_users(self):
        return users.query.all()
