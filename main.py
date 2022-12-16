import controller as contr

if __name__ == '__main__':
    while True:
        options = contr.click()
        op_num = contr.get_menu_choice(options)
        submenu_name, submenu_opt_count = contr.submenus_navigation(op_num)
        match submenu_name:
            case 'sa':
                pass
            case 'sm':
                op_num = contr.get_menu_choice(submenu_opt_count)
                contr.search_menu_navigation(op_num)
            case 'em':
                op_num = contr.get_menu_choice(submenu_opt_count)
                contr.edit_menu_navigation(op_num)
            case 'dm':
                op_num = contr.get_menu_choice(submenu_opt_count)
                contr.delete_menu_navigation(op_num)
            case 'fm':
                print('пока делаем!')
