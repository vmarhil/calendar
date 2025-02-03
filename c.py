import calendar
from datetime import datetime, date

import flet
from flet import (
    IconButton,
    icons,
    transform,
    animation,
    Text,
    alignment,
    app,
    Page,
    Column,
    Row,
    Container,
    LinearGradient,
)


def main(page: Page):
    _content_dic = {}
    _year_now = int(date.today().strftime("%Y"))
    _month_now = int(date.today().strftime("%m"))
    _day_now = int(date.today().strftime("%d"))
    obj = calendar.Calendar()

    def DeleteAnimation(e):
        if e.data == 'true':
            e.control.content.controls[0].offset = transform.Offset(-0.5, 0)
            e.control.content.controls[0].update()
            e.control.content.controls[0].opacity = 1
            e.control.content.controls[0].update()
        else:
            e.control.content.controls[0].offset = transform.Offset(0, 0)
            e.control.content.controls[0].update()
            e.control.content.controls[0].opacity = 0
            e.control.content.controls[0].update()

    def _delete_entry(evt, row):
        _content_column.controls.remove(row)
        _content_column.update()

    def _create_entry(e):
        new_row = Row(
            controls=[
                Container(
                    border_radius=8,
                    padding=12,
                    expand=True,
                    gradient=LinearGradient(
                        begin=alignment.center_left,
                        end=alignment.center_right,
                        colors=["#1e293b", "shadow"],
                    ),
                    content=Text(
                        f"You have a task on\n{e.control.data}",
                        size=10,
                        color='white70',
                    ),
                ),
                Container(
                    alignment=alignment.center_right,
                    animate=animation.Animation(1000, "ease"),
                    on_hover=lambda e: DeleteAnimation(e),
                    content=Row(
                        alignment="end",
                        spacing=0,
                        controls=[
                            Text(
                                "DELETE",
                                color='white70',
                                opacity=0,
                                size=9,
                                offset=transform.Offset(0, 0),
                                animate_offset=animation.Animation(
                                    duration=900, curve="ease"
                                ),
                                animate_opacity=200,
                            ),
                            IconButton(
                                icon=icons.DELETE_ROUNDED,
                                icon_size=19,
                                icon_color="#dc2626",
                                on_click=lambda evt: _delete_entry(evt, new_row)
                            ),
                        ],
                    ),
                ),
            ]
        )

        _content_column.controls.append(new_row)
        _content_column.update()



    def _highligth_date(e):
        if e.control.bgcolor == "blue900":
            pass
        else:
            if e.data == 'true':
                e.control.bgcolor = 'white10'
                e.control.update()
            else:
                e.control.bgcolor = '#0c0f16'
                e.control.update()

    def _popup(e):
        _title.visible = False
        _title.update()
        if e.control.height != _main.height * 0.55:
            e.control.height = _main.height * 0.55
            e.control.update()

            for key in _content_dic:
                for month in _content_dic[key]:
                    if month == _month_now and key == _year_now:
                        _content_dic[key][month].visible = True
                        _content_dic[key][month].update()

        else:
            e.control.height = _main.height * 0.13
            e.control.update()

            for key in _content_dic:
                for month in _content_dic[key]:
                    if month == _month_now and key == _year_now:
                        _content_dic[key][month].visible = False
                        _content_dic[key][month].update()
            _title.visible = True
            _title.update()

    _main = Container(
        width=290,
        height=590,
        bgcolor='black',
        padding=8,
        border_radius=30,
        alignment=alignment.center,
    )

    _main_column = Column(
        spacing=2,
        scroll="auto",
        alignment="start",
    )

    _calendar_container = Container(
        width=_main.width,
        height=_main.height * 0.13,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#1e293b", "#0f172a"],
        ),
        border_radius=30,
        alignment=alignment.center,
        on_click=lambda e: _popup(e),
        animate=animation.Animation(duration=320, curve='decelerate')
    )

    _calendar_container.content = _main_column

    _title = Container(
        content=Text(
            "Календарь",
            color="white70",
            weight="bold",
        )
    )

    _main_column.controls.append(_title)

    _content_column = Column(
        scroll='auto',
        expand=True,
        alignment="start",
        controls=[
            Container(
                padding=15,
                content=Text(
                    'Scheduled',
                    color='white70',
                    weight='bold',
                    size=13,
                )
            )

        ]
    )

    _main.content = Column(
        # scroll="auto",
        alignment="end",
        controls=[
            Container(
                expand=True,
                content=_content_column,
            ),
            _calendar_container,
        ]
    )

    months = [
        "январь",
        "февраль",
        "март",
        "апрель",
        "май",
        "июнь",
        "июль",
        "август",
        "сентябрь",
        "октябрь",
        "ноябрь",
        "декабрь"
    ]

    weekday = [
        "ПН",
        "ВТ",
        "СР",
        "ЧТ",
        "ПТ",
        "СБ",
        "ВС"
    ]

    _row_weekday = Row(
        spacing=2,
        alignment='center',
    )

    for day in weekday:
        _row_weekday.controls.append(
            Container(
                width=32,
                height=32,
                border_radius=5,
                alignment=alignment.center,
                content=Text(
                    day,
                    size=9,
                    color="white70"
                )
            )
        )

    for year in range(2025, 2026):
        _content_dic[year] = {}
        for month in range(2, 3):
            _inner_column = Column(
                horizontal_alignment="center",
                spacing=2,
            )
            _inner = Container(
                visible=False,  # Изначально скрываем календарь
                content=_inner_column,
            )
            _main_column.controls.append(_inner)

            _row_year = Row(
                spacing=2,
                alignment="center",
                controls=[
                    Text(
                        f"{months[month - 1]} {year}",
                        size=15,
                        color='white70',
                    )
                ]
            )

            _inner_column.controls.append(_row_year)
            _inner_column.controls.append(_row_weekday)

            for days in obj.monthdayscalendar(year, month):
                _row = Row(
                    spacing=2,
                    alignment='center',

                )
                _inner_column.controls.append(_row)

                for day in days:
                    if day != 0:
                        __ = Container(
                            width=32,
                            height=32,
                            bgcolor="#0c0F16",
                            border_radius=5,
                            alignment=alignment.center,
                            content=Text(
                                f"{day}",
                                size=10,
                                color="white70",
                            ),
                            data=f"{months[month - 1]} {day}, {year}",
                            on_click=lambda e: _create_entry(e),
                            on_hover=lambda e: _highligth_date(e),
                        )

                        _row.controls.append(__)

                        if month == _month_now and day == _day_now and year == _year_now:
                            __.bgcolor = "blue900"
                    else:
                         _row.controls.append(
                            Container(
                                width=32,
                                height=32,
                                border_radius=5,
                            )
                        )

            _content_dic[year][month] = _inner


    page.add(_main)
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.update()


if __name__ == "__main__":
    app(target=main)