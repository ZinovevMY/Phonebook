import controller as contr


if __name__ == '__main__':
    options = contr.click()
    op = contr.get_menu_choice(options)
    submenu_op = contr.submenus_navigation(op)