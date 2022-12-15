import controller as contr


if __name__ == '__main__':
    options = contr.click()
    op_num = contr.get_menu_choice(options)
    submenu_name, submenu_opt_count = contr.submenus_navigation(op_num)
    match submenu_name:
        case 'sa':
            pass
        case 'sm':
            contr.search_menu_navigation(submenu_opt_count)
        case 'em':
            contr.edit_menu_navigation(submenu_opt_count)
        case 'dm':
            contr.delete_menu_navigation(submenu_opt_count)
        case 'fm':
            print('пока делаем!')