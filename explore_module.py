class Explore:
        """Just a nice overview of the methods,
with view of most used methods based on Python site documentation
and  Github scrap"""
        def __init__(self, module):
                self.module = module
                try:
                        __import__(module)
                except ImportError as err:
                        print(err)

                #import table_display
                self.dirmo = dir(module)

        def print_list(self):
                for method in self.dirmo:
                        print(method)

        def connect_stackoverflow(self):
                pass
        def connect_github(self):
                pass

        def find_method(self, module):
                """use regex close_match method to find likely name"""
                pass

describe_os = Explore("os")

if __name__ == "__main__":
    describe_os.print_list()
