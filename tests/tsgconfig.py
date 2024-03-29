from django_rest_typescript_generator.build import build
from tests.models import PermissionFlag, User
from tests.serializers import ParentSerializer, PathSerializer, ChildSerializer, DepartmentSerializer

BUILD_TASKS = [
    build(PathSerializer),
    build(ParentSerializer, options={"alias": "FoobarParent"}),
    build(ChildSerializer, options={"alias": "FoobarChild"}),
    build(PermissionFlag, options={"enforce_uppercase": True}),
    build(User),
    build(DepartmentSerializer),
]
