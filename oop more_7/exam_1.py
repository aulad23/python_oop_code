class Triangle:
    sid=5
    @classmethod
    def line(cls):
        return cls.sid
   
    @staticmethod
    def info():
        return "Triangle has 5 sid."
   
print(Triangle.info())
print(Triangle.line())
