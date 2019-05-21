class A:
    def __init__(self,data):
        self.B_impl = self.B(data.get('B', ''))
        self.myList_impl = self.myList(data.get('List', []))

    class B:
        def __init__(self, data):
            self.B_data = data

    class myList:

        def __init__(self, data):
            list_impl = []
            if not isinstance(data, list):
                data = [data]

            for i in data:
                self.list_impl.append(self.ListInfo(i))

        class ListInfo:
            def __init__(self,data):
                self.age = data.get('age','')
                self.name = data.get('name', '')

    def __str__(self):
        result = "{"
        for i in self.__dict__:
            # print i
            temp_result = ''
            temp_result += i
            temp_result += ":"
            if i == 'myList_impl':
                temp_result += "["
                # print self.myList_impl.list_impl
                for j in self.myList_impl.list_impl:
                    temp_result += str(j.__dict__)
                    temp_result += ","
                temp_result = temp_result[:-1] + "]"
            else:
                temp_result += str(self.__dict__[i].__dict__)
                temp_result += ','
            result += temp_result

        result += "}"
        return result


if __name__ == '__main__':
    data = {"B": "b", "List": [{"age": 18, "name": "zcuy"}, {"age": 19, "name": "zcy"}]}
    a = A(data)
    print a  # {"B":'b', "List" :[{"age":18,"name":'zcuy'}]}