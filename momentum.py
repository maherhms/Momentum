from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    width = 400
    height = 850

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    container
                ],
            ),
        )

    create_task_view = Container()

    tasks= Column()

    categories_card= Row(
        scroll='auto',
    )

    categories=['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=15,
                bgcolor=BG,
                height=110,
                width=170,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=15,
                            padding=padding.only(right=i*30,),
                            content=Container(
                                bgcolor=PINK,
                                border_radius=15
                            ),
                        )
                    ]
                )
            )
        )

    first_page_contents= Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                
                    controls=[
                        Container(
                            content=Icon(
                                icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATION_ADD_OUTLINED)
                            ]
                        )
                    ]
                ),
                Text(
                    value='What\'s up, Olivia!'
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10,bottom=20,),
                    content=categories_card
                ),
                Container(height=5),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(icon=icons.ADD, on_click=lambda _: pages.go
                                             ('/create_task')
                        )
                    ]
                )
            ],
        ),
    )
    

    # page_1 = container()
    page_2 = Row(
        controls=[
            Container(
                width=width,
                height=height,
                bgcolor = FG,
                border_radius=30,
                padding= padding.only(top =50, left =20,right =20, bottom =5),
                content= Column(controls=[
                    first_page_contents
                ])
            )
        ]
    )
    container = Container(width=width, 
                          height=height , 
                          bgcolor=BG,
                          border_radius = 30,
                          content = Stack(
                              controls=[
                                #   page_1,
                                  page_2,
                              ])
    )

    pages={
        '/':View(
                "/",
                [
                    container
                ],
            ),
            '/create_task': View(
                '/Create_task',
                [
                    create_task_view
                ],
            )
    }

    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)

app(target=main)