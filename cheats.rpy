# DarkCheat for HornyCraft
screen cheat_button():
    zorder 100
 
    textbutton "ЧИТЫ" action ShowMenu("cheat_menu"):
        xalign 1.0 
        yalign 0.0 
        xoffset -90
        yoffset 10  
 
init python:
    config.overlay_screens.append('cheat_button')

init 999 python:
    renpy.notify("DarkCheat загружен")


init -1 python:
    s = style
    s.create("cheat_frame", "default")
    s.cheat_frame.background = Frame(Solid("#181818"), 1, 1, border_color="#00ddff")
    s.cheat_frame.padding = (25, 25)
    s.cheat_frame.xsize = 0.9
    s.cheat_frame.ysize = 0.9

    s.cheat_vbox = s.vbox
    s.cheat_vbox.box_spacing = 25

    s.cheat_hbox = s.hbox
    s.cheat_hbox.box_spacing = 10

    s.cheat_label = s.label
    s.cheat_label_text.color = "#00ddff"
    s.cheat_label_text.size = 28
    s.cheat_label_text.bold = True
    s.cheat_label_text.xalign = 0.5

    s.cheat_text = s.text
    s.cheat_text.color = "#E0E0E0"
    s.cheat_text.size = 20
    s.cheat_text.yalign = 0.5
    s.cheat_text.xalign = 0.5

    s.cheat_button = s.button
    s.cheat_button.xfill = True
    s.cheat_button.background = "#282828"
    s.cheat_button.hover_background = "#404040"
    s.cheat_button.padding = (10, 10)

    s.cheat_button_text = s.button_text
    s.cheat_button_text.color = "#FFFFFF"
    s.cheat_button_text.hover_color = "#00ddff"
    s.cheat_button_text.size = 18
    s.cheat_button_text.bold = False
    s.cheat_button_text.xalign = 0.5

    s.cheat_small_button = s.button
    s.cheat_small_button.background = "#333"
    s.cheat_small_button.hover_background = "#555"
    s.cheat_small_button.padding = (10, 5)
    s.cheat_small_button.xsize = 50

    s.cheat_small_button_text = s.button_text
    s.cheat_small_button_text.color = "#fff"
    s.cheat_small_button_text.size = 18
    s.cheat_small_button_text.xalign = 0.5

init python:
    # --- Списки для генерации кнопок чит-меню ---

    # Список ресурсов
    # Формат: (имя_переменной, текст_на_кнопке)
    resource_cheats = [
        ("", ""),
        ("emerald", "Изумрудов"),
        ("dimond", "Алмазов"),
        ("gold", "Золота"),
        ("", ""),
        ("iron", "Железа"),
        ("wood", "Деревья"),
        ("cobblestone", "Булыжников"),
    ]

    # Список прочности инструментов
    # Формат: (имя_переменной, текст_на_кнопке, максимальная прочность)
    durability_cheats = [
        ("", "", 0),
        ("diamond_sword_dur", "Алм. меч", 32),
        ("diamond_pickaxe_dur", "Алм. кирку", 32),
        ("diamond_axe_dur", "Алм. топор", 32),
        ("", "", 0),
        ("iron_sword_dur", "Жел. меч", 12),
        ("iron_pickaxe_dur", "Жел. кирку", 12),
        ("iron_axe_dur", "Жел. топор", 12),
        ("", "", 0),
        ("stone_sword_dur", "Кам. меч", 8),
        ("stone_pickaxe_dur", "Кам. кирку", 8),
        ("stone_axe_dur", "Кам. топор", 8),
        ("", "", 0),
        ("wooden_sword_dur", "Дерев. меч", 4),
        ("wooden_pickaxe_dur", "Дерев. кирку", 4),
        ("wooden_axe_dur", "Дерев. топор", 4),
    ]

    # Список предметов в инвентаре
    # Формат: (имя_переменной, имя_в_меню, тип_управления)
    # "toggle" - для предметов, которые можно иметь или не иметь (вкл/выкл)
    # "count" - для предметов, количество которых можно изменять
    inventory_cheats = [
        ("wooden_sword", "Деревянный меч", "toggle"),
        ("stone_sword", "Каменный меч", "toggle"),
        ("iron_sword", "Железный меч", "toggle"),
        ("diamond_sword", "Алмазный меч", "toggle"),
        ("fishing_rod", "Удочка", "toggle"),
        ("bucket", "Ведро", "toggle"),
        ("dildo", "Дилдо", "toggle"),
        ("weddingring", "Обручальное кольцо", "toggle"),
        ("totem1", "Тотем бессмертия", "toggle"),

        ("planks", "Доски", "count"),
        ("sti", "Палки", "count"),
        ("apple", "Яблоки", "count"),
        ("fish", "Рыба", "count"),
    ]

    # Список отношений с персонажами
    # Формат: (имя_переменной, имя_персонажа_для_кнопки)
    relationship_cheats = [
        ("al_rel", "Алекс"),
        ("cw_rel", "Коровой"),
        ("cr_rel", "Крипером"),
        ("end_rel", "Эндергёрл"),
        ("pig_rel", "Пиглеттой"),
        ("witch_rel", "Ведьмой"),
        ("wr_rel", "Варденом"),
        ("blaze_rel", "Блейзом"),
        ("zombie_rel", "Зомби"),
        ("slm_rel", "Слаймом"),
        ("jn_rel", "Дженни"),
    ]

screen cheat_menu():
    tag menu
    modal True
    zorder 200

    add Solid("#000000c0") 
  
    use screen_body

screen screen_body():
    style_group "cheat"

    frame:
        xalign 0.5
        yalign 0.5

        has vbox

        hbox:
            xfill True
            box_wrap False
            label "DARK CHEAT MENU"
            null width 0 xfill True
            textbutton "Вернуться в игру" action Return() style "button" xfill False

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                # --- Ресурсы ---
                label "Ресурсы"
                grid 4 2:
                    spacing 10
                    xfill True
                    for var, name in resource_cheats:
                        if name == '':
                            text ''
                        else:
                            textbutton f"+100 {name}" action SetVariable(var, getattr(store, var, 0) + 100)

                # --- Прочность ---
                label "Прочность инструментов"
                grid 4 4:
                    spacing 10
                    xfill True
                    for var, name, max_durability in durability_cheats:
                        if name == '':
                            text ''
                        else:
                            textbutton f"Починить {name}" action SetVariable(var, max_durability)

                # --- Инвентарь ---
                label "Предметы в инвентаре"
                grid 2 7: # (примерно)
                    xfill True
                    spacing 10
                    for var, name, type in inventory_cheats:
                        if type == "toggle":
                            hbox:
                                xfill True
                                text f"{name}:" style "text" xalign 0.5
                                textbutton ("Есть" if getattr(store, var, False) else "Нет") action ToggleVariable(var) style "button" xalign 0.5

                        elif type == "count":
                            hbox:
                                xfill True
                                text f"{name}:" style "text" xalign 0.5
                                hbox:
                                    xalign 0.5
                                    textbutton "-1" action SetVariable(var, max(0, getattr(store, var, 0) - 1)) style "small_button"
                                    text f"{getattr(store, var, 0)}" style "text" min_width 50
                                    textbutton "+1" action SetVariable(var, getattr(store, var, 0) + 1) style "small_button"

                # --- Отношения ---
                label "Отношения с персонажами"
                vbox:
                    xfill True
                    spacing 10
                    for var, name in relationship_cheats:
                        hbox:
                            xfill True
                            text f"Отношения с {name}:" style "text" xalign 0.0
                            hbox:
                                xalign 1.0
                                textbutton "-10" action SetVariable(var, getattr(store, var, 0) - 10) style "small_button"
                                textbutton "-1" action SetVariable(var, getattr(store, var, 0) - 1) style "small_button"
                                text f"{getattr(store, var, 0)}" style "text" min_width 60
                                textbutton "+1" action SetVariable(var, getattr(store, var, 0) + 1) style "small_button"
                                textbutton "+10" action SetVariable(var, getattr(store, var, 0) + 10) style "small_button"

        null height 15