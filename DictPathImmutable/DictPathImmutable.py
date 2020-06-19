import copy

# How to use me?

# Simply import me and call one of my first 3 methods!
# When calling get, set or delete, pass in an object, a path to a key (that may or may not exist), and your desired value (for set)
# And I'll return you a new object with your desired updates (or the value at the given path for get)
# Please refer to my tests for some examples


class Dict_Path_Immutable:
    @staticmethod
    def get(src, path):
        if Dict_Path_Immutable.isNumber(path):
            path = [path]
        if Dict_Path_Immutable.isEmpty(path):
            return src
        if Dict_Path_Immutable.isString(path):
            path = list(map(Dict_Path_Immutable.getKey, path.split(".")))
        value = src
        for token in path:
            if isinstance(value, dict):
                value = value.get(token, None)
            elif isinstance(value, list):
                if Dict_Path_Immutable.isNumber(token) and token < len(value):
                    value = value[token]
                else:
                    value = None
            else:
                value = None
            if value is None:
                break
        return value
        

    @staticmethod
    def set(src, path, value):
        dest = src.copy() if Dict_Path_Immutable.isArray(src) else copy.deepcopy(src)
        if Dict_Path_Immutable.isEmpty(path):
            return value
        return Dict_Path_Immutable.changeImmutable(
            dest, src, path, Dict_Path_Immutable.setCallBack, value
        )

    @staticmethod
    def delete(src, path):
        dest = src.copy() if Dict_Path_Immutable.isArray(src) else copy.deepcopy(src)
        if Dict_Path_Immutable.isEmpty(path):
            return None
        return Dict_Path_Immutable.changeImmutable(
            dest, src, path, Dict_Path_Immutable.deleteCallBack, None
        )

    @staticmethod
    def changeImmutable(dest, src, path, callback, value):
        if Dict_Path_Immutable.isNumber(path):
            path = [path]
        if Dict_Path_Immutable.isEmpty(path):
            return src
        if Dict_Path_Immutable.isString(path):
            return Dict_Path_Immutable.changeImmutable(
                dest,
                src,
                list(map(Dict_Path_Immutable.getKey, path.split("."))),
                callback,
                value,
            )
        current_path = path[0]
        if not bool(dest):
            dest = Dict_Path_Immutable.clone(
                src, True, Dict_Path_Immutable.isNumber(current_path)
            )
        elif (
            not isinstance(src, list)
            and not isinstance(dest, list)
            and not isinstance(src, dict)
            and not isinstance(dest, dict)
            and src == dest
        ):
            dest = Dict_Path_Immutable.clone(
                src, True, Dict_Path_Immutable.isNumber(current_path)
            )
        if len(path) == 1:
            return callback(dest, current_path, value)
        if src != None:
            if isinstance(src, list) and len(src) > current_path:
                src = src[current_path]
            elif isinstance(src, dict) and current_path in src:
                src = src[current_path]
            else:
                src = None
        if isinstance(dest, list) and len(dest) > current_path:
            next_dest = dest[current_path]
        elif isinstance(dest, dict) and current_path in dest:
            next_dest = dest[current_path]
        else:
            next_dest = None

        if isinstance(dest, list) and len(dest) <= current_path:
            dest.append(None)
        dest[current_path] = Dict_Path_Immutable.changeImmutable(
            next_dest, src, path[1:], callback, value
        )
        return dest

    @staticmethod
    def setCallBack(clonedObj, finalPath, value):
        clonedObj[finalPath] = value
        return clonedObj

    @staticmethod
    def deleteCallBack(clonedObj, finalPath, value):
        if Dict_Path_Immutable.isArray(clonedObj) and len(clonedObj) > finalPath:
            del clonedObj[finalPath]
        elif finalPath in clonedObj:
            del clonedObj[finalPath]
        return clonedObj

    @staticmethod
    def clone(obj, createIfEmpty, assumeArray):
        if obj == None:
            if createIfEmpty:
                if assumeArray:
                    return []
                return {}
            return obj
        elif Dict_Path_Immutable.isArray(obj):
            return obj.copy()
        return Dict_Path_Immutable.assignToObj({}, obj)

    @staticmethod
    def assignToObj(target, source):
        for key in source:
            if hasattr(source, key):
                target[key] = source[key]
        return target

    @staticmethod
    def isEmpty(value):
        if Dict_Path_Immutable.isNumber(value):
            return False
        if not bool(value):
            return False
        if Dict_Path_Immutable.isArray(value):
            return len(value) == 0
        elif not Dict_Path_Immutable.isString(value):
            for key in value:
                if hasattr(value, key):
                    return False
            return True
        return False

    @staticmethod
    def isNumber(value):
        return isinstance(value, int)

    @staticmethod
    def isString(value):
        return isinstance(value, str)

    @staticmethod
    def isArray(value):
        return isinstance(value, list)

    @staticmethod
    def getKey(key):
        try:
            int_key = int(key)
        except ValueError:
            int_key = None
            pass
        if str(int_key) == key:
            return int_key
        return key
