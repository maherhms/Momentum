from flet import *
import uuid
from CustomCheckBox import CustomCheckBox

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#red50'
    width = 400
    height = 850

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment='center',
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=BG,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=FG,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                                )
                            )
                        )
                    ],
                ),
            ),
        ]
    )

    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0,
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 25
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.update()

    initial_route = '/'
    if not page.route:
        page.route = initial_route  # Set default route if none is set

    tasks_data = [{"id": str(uuid.uuid4()), "label": "first test"}]

    def add_task(e, task_input):
        task_id = str(uuid.uuid4())
        tasks_data.append({"id": task_id, "label": task_input.value})
        print(tasks_data)
        create_task()
        page.go('/')

    def delete_task(e, task_id):
        nonlocal tasks_data  # Ensure tasks_data is correctly referenced
        tasks_data = [task for task in tasks_data if task["id"] != task_id]
        create_task()
        page.update()
        print(f"Deleted task {task_id}")

    def create_task_view():
        return Container(
            width=width,
            height=height,
            bgcolor=FG,
            border_radius=30,
            alignment=alignment.center,
            padding=padding.only(top=20,),
            content=Column(
                controls=[
                    IconButton(on_click=lambda _: page.go('/'),
                               icon=icons.CLOSE,
                               height=40, width=40),
                    TextField(hint_text="Enter task description", width=300),
                    FloatingActionButton(
                        text="Add Task",
                        on_click=(lambda e: add_task(e, e.control.parent.controls[1])),
                        width=300,
                        height=35
                    ),
                ]
            )
        )

    tasks = Column(
        height=400,
        scroll='auto',
    )

    def create_task():
        tasks.controls.clear()
        for task in tasks_data:
            task_id = task["id"]
            task_label = task["label"]
            checkbox = CustomCheckBox(
                color='red50',
                label=task_label,
                taskDelete=lambda e, task_id=task_id: delete_task(e, task_id)  # Pass the task ID to delete_task
            )
            tasks.controls.append(
                Container(
                    height=70,
                    width=400,
                    bgcolor=BG,
                    border_radius=15,
                    padding=padding.only(left=20, top=25),
                    content=checkbox,
                )
            )

    categories_card = Row(scroll='auto')
    categories = ['Business', 'Family', 'Friends']

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
                            padding=padding.only(right=i * 30),
                            content=Container(
                                bgcolor=PINK,
                                border_radius=15
                            ),
                        )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                                  content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATION_ADD_OUTLINED)
                            ]
                        )
                    ]
                ),
                Text(value="What's up, Olivia!"),
                Text(value='CATEGORIES'),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                ),
                Container(height=5),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        
                    ]
                ),
                FloatingActionButton(
                            icon=icons.ADD, on_click=lambda _: page.go('/create_task')
                        ),
            ],
        ),
    )

    page_1 = Container(
        width=width,
        height=height,
        bgcolor=BG,
        border_radius=30,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row(alignment='end',
                    controls=[
                        IconButton(
                            icon=icons.KEYBOARD_DOUBLE_ARROW_LEFT,
                            padding=padding.only(top=13, left=13),
                            height=50,
                            width=50,
                            on_click=lambda e: restore(e),
                        )
                    ]
                ),
                Container(height=20),
                circle,
                Text('Olivia\nMitchel', size=32, weight='bold'),
                Container(height=25),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color='white60'),
                    Text('Templates', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL, color='white60'),
                    Text('Templates', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED, color='white60'),
                    Text('Templates', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Image(src=f"",
                      width=300,
                      height=200,
                      ),
                Text('Good', color=FG, font_family='poppins', ),
                Text('Consistency', size=22,)
            ]
        )
    )

    page_2 = Row(alignment='end',
                 controls=[
                     Container(
                         width=width,
                         height=height,
                         bgcolor=FG,
                         border_radius=30,
                         animate=animation.Animation(600, AnimationCurve.EASE_OUT),
                         animate_scale=animation.Animation(400, AnimationCurve.EASE_OUT),
                         padding=padding.only(top=50, left=20, right=20, bottom=5),
                         content=Column(controls=[first_page_contents])
                     )
                 ]
                 )

    container = Container(
        width=width,
        height=height,
        bgcolor=BG,
        border_radius=30,
        content=Stack(controls=[
            page_1,
            page_2]
        )
    )

    pages = {
        '/': container,
        '/create_task': create_task_view()
    }

    create_task()

    def route_change(route):
        page.controls.clear()  # Clear the current page controls
        if page.route in pages:
            page.add(pages[page.route])  # Add the new view based on the current route
        else:
            page.add(pages['/'])  # Fallback to the default view if the route is undefined
        page.update()

    page.on_route_change = route_change
    page.add(pages[page.route])  # Add the initial view based on the current route
    page.go(page.route)  # Navigate to the initial or current route

app(target=main)
