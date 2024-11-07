from contextvars import ContextVar


island_num: ContextVar[int] = ContextVar("island_num", default=0)

images_fletcher = [
    (
        "C:\\AO_labour_bot\\images\\t8_fletcher_journal.png",
        (96, 356, 1500, 608),
        "Putted t8 fletcher journals",
    ),
    (
        "C:\\AO_labour_bot\\images\\t7_fletcher_journal.png",
        (105, 419, 1500, 608),
        "Putted t7 fletcher journals",
    ),
    (
        "C:\\AO_labour_bot\\images\\t6_fletcher_journal.png",
        (97, 514, 1500, 608),
        "Putted t6 fletcher journals",
    ),
]

images_imbuer = [
    (
        "C:\\AO_labour_bot\\images\\t8_imbuer_journal.png",
        (212, 331, 1605, 614),
        "Putted t8 imbuer journals",
    ),
    (
        "C:\\AO_labour_bot\\images\\t7_imbuer_journal.png",
        (199, 408, 1605, 614),
        "Putted t7 imbuer journals",
    ),
    (
        "C:\\AO_labour_bot\\images\\t6_imbuer_journal.png",
        (204, 524, 1605, 614),
        "Putted t6 imbuer journals",
    ),
]

images_blacksmith = [
    (
        "C:\\AO_labour_bot\\images\\t8_blacksmith_journal.png",
        (316, 321, 1709, 612),
        "Putted blacksmith t8 journals",
    ),
    (
        "C:\\AO_labour_bot\\images\\t7_blacksmith_journal.png",
        (298, 425, 1709, 612),
        "Putted blacksmith t7 journals",
    ),
    (
        "C:\\AO_labour_bot\\images\\t6_blacksmith_journal.png",
        (309, 514, 1709, 612),
        "Putted blacksmith t6 journals",
    ),
]

labours = [
    (
        "C:\\AO_labour_bot\\images\\fletcher_labour.png",
        (1589, 544, 101, 665),
        "Fletcher",
    ),
    (
        "C:\\AO_labour_bot\\images\\imbuer_labour.png",
        (1665, 538, 101, 665),
        "Imbuer",
    ),
    (
        "C:\\AO_labour_bot\\images\\blacksmith_labour.png",
        (1749, 534, 101, 665),
        "BlackSmith",
    ),
]

labour_coordinates = [
    (986, 331),  # Labour 1
    (1103, 342),  # Labour 2
    (1103, 342),  # Labour 3
    (1103, 342),  # Labour 4
    (1103, 342),  # Labour 5
    (1103, 342),  # Labour 6
    (1103, 342),  # Labour 7
    (1103, 342),  # Labour 8
    (1343, 744),  # Labour 9
    (1102, 723),  # Labour 10
    (999, 797),  # Labour 11
    (901, 780),  # Labour 12
    (833, 795),  # Labour 13
    (833, 795),  # Labour 14
    (833, 795),  # Labour 15
]

inventory_coords = [
    (1834, 537, 86, 351),
    (1589, 624, 165, 353),
    (1666, 618, 244, 354),
    (1752, 620, 328, 349),
    (1829, 620, 406, 352),
    (1589, 701, 81, 431),
    (1671, 699, 168, 430),
    (1751, 701, 244, 435),
    (1827, 700, 324, 434),
    (1589, 783, 409, 430),
    (1668, 781, 80, 514),
    (1750, 785, 166, 510),
    (1830, 779, 248, 518),
]
