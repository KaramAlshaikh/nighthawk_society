class Projects:
    def __init__(self):
        self.list, self.filters = project_data()

    @property
    def list(self):
        return self._list

    @property
    def filters(self):
        return self.filters


if __name__ = '__main__':
    projects_object = Projects()

    print("Filters")
    for filter_tag in projects_object.filters:
        print(filter_tag)

    print("Project Data")
   # for project in projects_object.list