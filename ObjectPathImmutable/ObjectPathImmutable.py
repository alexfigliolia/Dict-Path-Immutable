import copy

# How to use me?

# Simply import me and call one of my first two methods!
# When calling set or delete, pass in an object, a path to a key (that may or may not exist), and your desired value (for set)
# And I'll return you a new object with your desired updates
# Please refer to my tests for some examples


class Object_Path_Immutable:
    @staticmethod
    def set(src, path, value):
        dest = src.copy() if Object_Path_Immutable.isArray(src) else copy.deepcopy(src)
        if Object_Path_Immutable.isEmpty(path):
            return value
        return Object_Path_Immutable.changeImmutable(
            dest, src, path, Object_Path_Immutable.setCallBack, value
        )

    @staticmethod
    def delete(src, path):
        dest = src.copy() if Object_Path_Immutable.isArray(src) else copy.deepcopy(src)
        if Object_Path_Immutable.isEmpty(path):
            return None
        return Object_Path_Immutable.changeImmutable(
            dest, src, path, Object_Path_Immutable.deleteCallBack, None
        )

    @staticmethod
    def changeImmutable(dest, src, path, callback, value):
        if Object_Path_Immutable.isNumber(path):
            path = [path]
        if Object_Path_Immutable.isEmpty(path):
            return src
        if Object_Path_Immutable.isString(path):
            return Object_Path_Immutable.changeImmutable(
                dest,
                src,
                list(map(Object_Path_Immutable.getKey, path.split("."))),
                callback,
                value,
            )
        current_path = path[0]
        if not bool(dest):
            dest = Object_Path_Immutable.clone(
                src, True, Object_Path_Immutable.isNumber(current_path)
            )
        elif (
            not isinstance(src, list)
            and not isinstance(dest, list)
            and not isinstance(src, dict)
            and not isinstance(dest, dict)
            and src == dest
        ):
            dest = Object_Path_Immutable.clone(
                src, True, Object_Path_Immutable.isNumber(current_path)
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
        dest[current_path] = Object_Path_Immutable.changeImmutable(
            next_dest, src, path[1:], callback, value
        )
        return dest

    @staticmethod
    def setCallBack(clonedObj, finalPath, value):
        clonedObj[finalPath] = value
        return clonedObj

    @staticmethod
    def deleteCallBack(clonedObj, finalPath, value):
        if Object_Path_Immutable.isArray(clonedObj) and len(clonedObj) > finalPath:
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
        elif Object_Path_Immutable.isArray(obj):
            return obj.copy()
        return Object_Path_Immutable.assignToObj({}, obj)

    @staticmethod
    def assignToObj(target, source):
        for key in source:
            if hasattr(source, key):
                target[key] = source[key]
        return target

    @staticmethod
    def isEmpty(value):
        if Object_Path_Immutable.isNumber(value):
            return False
        if not bool(value):
            return False
        if Object_Path_Immutable.isArray(value):
            return len(value) == 0
        elif not Object_Path_Immutable.isString(value):
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
