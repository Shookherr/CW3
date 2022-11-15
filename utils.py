from json import load, JSONDecodeError


def get_data_from_json(path):
    """
    Возвращает все данные из файла json
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:     # открытие файла
            data = load(file)                               # загрузка данных
    except FileNotFoundError:
        print(f'ERROR: Not file {path} found.')
        return None
    except JSONDecodeError:
        print(f'ERROR: File {path} not JSON format.')
        return None
    else:
        return data


def load_all_posts(path):
    """
    Возврат всех считанных постов
    """
    return get_data_from_json(path)


def filter_str_posts(posts, key_post, search_word):
    """
    Возврат постов, отфильтрованных по строкам
    """
    fposts = []
    for post in posts:
        if search_word.lower() in post[key_post].lower():
            fposts.append(post)
    return fposts


def load_post(pk, path):
    """
    Возврат конкретного поста
    """
    posts = get_data_from_json(path)
    for post in posts:
        if post["pk"] == pk:
            return post


def load_comments_pk(pk, path):
    """
    Возвращает все комментарии к конкретному посту
    """
    total_comments = get_data_from_json(path)

    comments = []
    for comment in total_comments:
        if pk == comment["post_id"]:
            comments.append(comment)

    return comments
