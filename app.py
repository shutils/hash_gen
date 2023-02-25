import flet as ft
import hashlib


def main(page: ft.Page):
    page.title = "Hash generator"
    page.window_height = 500
    page.window_width = 500

    hash_type_list = ["md5", "sha256", "sha512"]
    dd = ft.Dropdown()
    for hash_type in hash_type_list:
        dd.options.append(ft.dropdown.Option(hash_type))
    dd.value = hash_type_list[0]
    str_field = ft.TextField()
    created_hash = ft.Text("ここに生成されたハッシュが表示されます")
    created_hash.selectable = True

    def create_hash(e) -> None:
        hash_type = dd.value
        string = str_field.value
        result = ""
        if hash_type == "md5":
            result = hashlib.md5(string.encode()).hexdigest()
        if hash_type == "sha256":
            result = hashlib.sha256(string.encode()).hexdigest()
        if hash_type == "sha512":
            result = hashlib.sha512(string.encode()).hexdigest()
        created_hash.value = result
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("生成アルゴリズム"),
                dd,
                ft.Text("元の文字列"),
                str_field,
                ft.ElevatedButton("生成", on_click=create_hash),
                ft.Text("ハッシュ"),
                created_hash,
            ]
        )
    )


ft.app(target=main)
