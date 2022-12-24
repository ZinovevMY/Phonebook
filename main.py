import view as v
import controller as contr


if __name__ == '__main__':
    while True:
        bd_type = contr.bd_type_selector()
        selected_bd = v.get_menu_choice(bd_type)
        if selected_bd == 1:
            FILE_TYPE = 1
        else:
            FILE_TYPE = 2
        options = contr.click()
        op_num = v.get_menu_choice(options)
        submenu_name, submenu_opt_count = v.submenus_navigation(op_num)
        match submenu_name:
            case 'sa':
                v.show_all_menu_navigation()
            case 'sm':
                op_num = v.get_menu_choice(submenu_opt_count)
                v.search_menu_navigation(op_num)
            case 'em':
                op_num = v.get_menu_choice(submenu_opt_count)
                v.edit_menu_navigation(op_num)
            case 'dm':
                op_num = v.get_menu_choice(submenu_opt_count)
                v.delete_menu_navigation(op_num)
