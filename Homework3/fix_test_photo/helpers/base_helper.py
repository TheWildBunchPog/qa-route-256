from fix_test_photo.clients.api_client import ApiClient


def get_filtered_animal_name(pet_list: list) -> list:
    # get all name for animal in category
    count = list()
    for pet in pet_list:
        category = pet.get('category', None)
        if category and 'string' not in category.get('name'):
            count.append(category.get('name'))
    print(count)
    return count


def get_animal_with_photo(pet_list: list) -> dict:
    # get pet with photo in description
    count = dict()
    for pet in pet_list:
        for url in pet.get('photoUrls'):
            if url.startswith('http'):
                id_with_photo = {
                                 pet.get('id'): pet.get('photoUrls', None)
                             }
                count.update(id_with_photo)

    return count
