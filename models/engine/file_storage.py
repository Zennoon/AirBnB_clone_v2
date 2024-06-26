#!/usr/bin/python3
"""
contains

classes:
    FileStorage - Responsible for serializing and deserializing
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file, and deserializes JSON strings to
    instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the objects belonging to a given class or all objects if cls
        is not given

        Args:
            cls: The class whose instances are returned

        Returns:
            dict: A dictionary whose values are objects
        """
        if cls is None:
            return (FileStorage.__objects)
        objs = FileStorage.__objects
        return {key: val for key, val in objs.items() if type(val) is cls}

    def new(self, obj):
        """
        Inserts an instance in the __objects private attribute.

        Args:
            obj: The object to insert in the dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the instances in the __objects attributes and stores them in
        the file '__file_path'.
        """
        to_store = FileStorage.__objects.copy()
        for key in to_store.keys():
            to_store[key] = to_store[key].to_dict()
        with open(FileStorage.__file_path, 'wt', encoding="utf-8") as f:
            json.dump(to_store, f)

    def reload(self):
        """
        Deserializes the json file and inserts the instances to __objects.
        """
        from models import base_model, user, state
        from models import city, amenity, place, review

        classes = {
            "BaseModel": base_model.BaseModel,
            "User": user.User,
            "State": state.State,
            "City": city.City,
            "Amenity": amenity.Amenity,
            "Place": place.Place,
            "Review": review.Review
        }
        try:
            with open(FileStorage.__file_path, "rt", encoding="utf-8") as f:
                FileStorage.__objects = {}
                file_dict = json.load(f)
                for key in file_dict.keys():
                    cls = classes[file_dict[key]["__class__"]]
                    FileStorage.__objects[key] = cls(**(file_dict[key]))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes a given object from __objects if it exists

        Args:
            obj: The object to remove from the __objects dictionary
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if FileStorage.__objects.get(key) is not None:
                del FileStorage.__objects[key]

    def close(self):
        """
        Update our __objects to reflect all the recently made transactions,
        and newly saved objects
        """
        self.reload()
