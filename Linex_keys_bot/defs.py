from keyboardsru import MenuRu, AdminMenuRu, InlineKeyboardMarkup, InlineKeyboardButton
from keyboardsua import MenuUa, AdminMenuUa


def get_menuRu(user_id):
    if 1433760480 != user_id != 5440056373:
        return MenuRu
    else:
        return AdminMenuRu
    
def get_menuUa(user_id):
    if 1433760480 != user_id != 5440056373:
        return MenuUa
    else:
        return AdminMenuUa